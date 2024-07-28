import requests
import smtplib
import base64
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime

class BysatApiClient:
    def __init__(self):
        self.urlbysat = 'https://api.bysat.com.br/'
        self.userbysat = 'comlurb'
        self.passbysat = 'comlurbrj'
        self.urlproxy = 'http://proxypcrj.comlurb.rio.rj.gov.br:8080'
        self.token = None

    def authenticate_and_get_token(self):
        login_url = f"{self.urlbysat}login"
        proxies = {"http": self.urlproxy, "https": self.urlproxy}

        response = requests.post(login_url, data={
            'usuario': self.userbysat,
            'senha': self.passbysat,
        }, proxies=proxies, verify=False)

        if response.status_code != 200:
            raise Exception(f"Erro ao fazer a requisição: {response.text}")

        response_json = response.json()
        if 'token' in response_json:
            self.token = response_json['token']
        else:
            raise Exception(f"Token não encontrado na resposta: {response.text}")

        return self.token

    def get_ultima_posicao(self, status=None, placa=None, paginate=False):
        url = f"{self.urlbysat}getUltimaPosicao"
        proxies = {"http": self.urlproxy, "https": self.urlproxy}

        headers = {
            'Authorization': f'Bearer {self.token}',
        }

        response = requests.get(url, headers=headers, proxies=proxies, verify=False)

        if response.status_code != 200:
            raise Exception(f"Erro ao fazer a requisição: {response.text}")

        response_json = response.json()
        if not response_json:
            raise Exception(f"Nenhum dado retornado pela API: {response.text}")

        return response_json

    def send_ultima_posicao_as_csv_email(self, status=None, placa=None, paginate=False, recipient_email=None):
        result = self.get_ultima_posicao(status, placa, paginate)

        if result and isinstance(result, list):
            message_str = '<!DOCTYPE html><html><head><meta charset="UTF-8"></head><body>'
            message_str += '<div><p>Dados da BySat.</p>'
            message_str += '<table border="1" style="width: 100%; border-collapse: collapse; text-align: center;">'
            message_str += '<thead><tr style="background: lightgray;">'
            fields = [
                'id_veiculo', 'placa', 'veiculo', 'frota', 'modelo', 'cliente', 'empresa', 'orgao', 
                'velocidade', 'rpm', 'hodometro', 'horimetro', 'status_ignicao', 'status_lacre', 
                'low_power', 'status_instalacao', 'modelo_comunicador', 'data', 'motivo_transmissao', 
                'nome_condutor', 'matricula_condutor', 'orgao_condutor', 'latitude', 'longitude', 
                'localizacao', 'link_localizacao_google_maps'
            ]
            for field in fields:
                message_str += f"<th>{field}</th>"
            message_str += '</tr></thead><tbody>'

            for row in result:
                message_str += '<tr>'
                for field in fields:
                    value = row.get(field, '')
                    message_str += f"<td>{value}</td>"
                message_str += '</tr>'

            message_str += '</tbody></table></div></body></html>'

            subject = "Dados BySat"
            self.send_csv_by_email(recipient_email, message_str, subject)
        else:
            raise Exception('Nenhum dado retornado para enviar por e-mail.')

    def send_csv_by_email(self, email, message_str, subject):
        file_path = self.criando_excel(message_str)

        from_addr = "sistemas.lgg@rio.rj.gov.br"
        to_addr = email
        cc_addr = "desenvolvimento_comlurb@rio.rj.gov.br"

        msg = MIMEMultipart()
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Cc'] = cc_addr
        msg['Subject'] = subject

        msg.attach(MIMEText(message_str, 'html'))

        part = MIMEBase('application', "octet-stream")
        with open(file_path, "rb") as file:
            part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(file_path)}"')
        msg.attach(part)

        server = smtplib.SMTP('smtp.seuservidor.com', 587)
        server.starttls()
        server.login("seuemail@seuservidor.com", "suasenha")
        server.sendmail(from_addr, [to_addr, cc_addr], msg.as_string())
        server.quit()

        print("Email enviado com sucesso!")

    def criando_excel(self, message_str):
        file_name = f"dadosBySat_{datetime.now().strftime('%d-%m-%Y')}.xls"
        dir_path = "/Extranet/UPLOAD_WEB/Temporario/dadosBySat/"

        if not os.path.exists(dir_path):
            os.makedirs(dir_path, exist_ok=True)

        file_path = os.path.join(dir_path, file_name)
        with open(file_path, 'w') as file:
            file.write(message_str)

        return file_path

bysat_api_client = BysatApiClient()
bysat_api_client.authenticate_and_get_token()
bysat_api_client.send_ultima_posicao_as_csv_email('a', None, True, 'rafaela.goncalves@prefeitura.rio')
