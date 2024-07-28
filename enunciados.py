# 1. Verificar se o número digitado é ímpar ou par.

entrada = input('Digite um número: ')

try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ímpar'

    if par_impar:
        par_impar_texto = 'par'

    print(f'O número {entrada_int} é {par_impar_texto}')
except:
    print('Você não digitou um número inteiro')


# 2. Digitar o horário e dizer se é bom dia, boa tarde ou boa noite.

entrada = input('Digite um horário inteiro: ')

try:
    entrada_int = int(entrada)

    if entrada_int >= 0 and entrada_int <= 11:
        print(f'Bom dia!')
    elif entrada_int >= 12 and entrada_int <= 17:
        print(f'Boa tarde!')
    elif entrada_int >= 18 and entrada_int <= 23:
        print(f'Boa noite!')
    else:
        print(f'Não conheço essa hora')
except:
    print('Horário inválido, digite apenas números inteiros.')

# 3. Pedir o primeiro nome do usuário 

nome = input('Digite seu nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print(f'Seu nome é curto!')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print(f'Seu nome é normal!')
    elif tamanho_nome >= 6:
        print(f'Seu nome é muito grande!')
else:
    print('Digite mais de uma letra!')