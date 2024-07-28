perguntas = [
    {
        'Pergunta': 'Quais o menor e o maior país do mundo?',
        'Opções': ['Vaticano e Rússia', 'Nauru e China', 'Mônaco e Canadá', 'Malta e Estados Unidos'],
        'Resposta': 'Vaticano e Rússia',
        'Texto': 'O Vaticano, sede da igreja católica, tem apenas 44 hectares (0,44 km2). A Rússia, localizada em dois continentes (Ásia e Europa), tem 17 milhões de km2.',
    },
    {
        'Pergunta': 'Qual o grupo em que todas as palavras foram escritas corretamente?',
        'Opções': ['Asterístico, beneficiente, meteorologia, entertido', 'Asterisco, beneficente, meteorologia, entretido', 'Asterisco, beneficente, metereologia, entretido', 'Asterístico, beneficiente, metereologia, entretido'],
        'Resposta': 'Asterisco, beneficente, meteorologia, entretido',
        'Texto': 'Estas palavras são exemplos de barbarismo, um vício de linguagem em que as palavras são pronunciadas ou escritas incorretamente.',
    },
    {
        'Pergunta': 'Em que período da pré-história o fogo foi descoberto?',
        'Opções': ['Neolítico', 'Idade dos Metais', 'Idade Média', 'Paleolítico'],
        'Resposta': 'Paleolítico',
        'Texto': 'Foi no Paleolítico que o fogo começou a ser utilizado, quando os homens aprenderam que era possível obter fogo por meio do atrito de pedaços de madeira e pedra.',
    },
]

qtd_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])
    print()

    opcoes = pergunta['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)
    print()

    escolha = input('Escolha um índice: ')

    acertou = False
    escolha_int = None
    qtd_opcoes = len(opcoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >= 0 and escolha_int < qtd_opcoes:
            if opcoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()
    if acertou:
        qtd_acertos += 1
        print('Acertou ✅')
        print('A resposta é:', pergunta['Resposta'])
        print(pergunta['Texto'])
    else:
        print('Errou ❌')
        print('A resposta era:', pergunta['Resposta'])

    print()


print('Você acertou', qtd_acertos, 'de', len(perguntas), 'perguntas.')