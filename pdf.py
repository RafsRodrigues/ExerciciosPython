from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Título do PDF', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def gerar_pdf():
    pdf = PDF()
    pdf.add_page()
    pdf.chapter_title('Exemplo de Capítulo')
    pdf.chapter_body('Este é um exemplo de texto para o corpo do capítulo.')
    pdf.output('exemplo_fpdf.pdf')

if __name__ == "__main__":
    gerar_pdf()
