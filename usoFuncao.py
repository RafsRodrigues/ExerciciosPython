def multiplicar(*arqs):
    total = 1
    for numero in arqs:
        total *= numero
    return total

multiplicacao = multiplicar(1, 2, 3, 4, 5)

# print(multiplicacao)


def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f"{numero} é par"
    return  f"{numero} é ímpar"

# print(par_impar(3))

def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar

duplicar = criar_multiplicador(2)
print(duplicar(2))

