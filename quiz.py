'''
Sistemas de perguntas e respostas com dicionários em Python
'''

print("Seja bem vindo ao quiz! Escolha apenas 1 alternativa correta, e o mais importante, DIVIRTA-SE!! ")
print("Você deseja: ")
print("[1] - Perguntas fáceis")
print("[2] - Perguntas médias")
print("[3] - Perguntas difíceis")
print()
escolha = int(input("Escolha uma das opções: "))
print()

if escolha == 1:
    num_respostas_certas = 0 # Contador de respostas certas
    perguntas = {
        'Pergunta 1': {
            'pergunta': "Qual o satélite natural da Terra?",
            'respostas': {"a": "Sol", "b": "Marte", "c": "Lua"},
            'resposta_certa': "c"
        },
        'Pergunta 2': {
            'pergunta': "Qual o maior oceano do mundo?",
            'respostas': {"a": "Atlântico", "b": "Pacífico", "c": "Índico"},
            'resposta_certa': "b"
        },
        'Pergunta 3': {
            'pergunta': "Quais o menor e o maior país do mundo??",
            'respostas': {"a": "índia e Inglaterra", "b": "Havaí e Rússia", "c": "Vaticano e Rússia"},
            'resposta_certa': "c"
        },
        'Pergunta 4': {
            'pergunta': "Quem pintou a Mona Lisa?",
            'respostas': {"a": "Pablo Picasso", "b": "Salvador Dalí", "c": "Leonardo da Vinci"},
            'resposta_certa': "c"
        },
        'Pergunta 5': {
            'pergunta': "Qual a montanha mais alta do mundo?",
            'respostas': {"a": "Everest", "b": "Kilimanjaro", "c": "Alpes"},
            'resposta_certa': "a"
        },
    }

    for pk, pv in perguntas.items():
        print(f"{pk}: {pv['pergunta']}")

        print("Escolha uma das opções abaixo: ")
        for rk, rv in pv['respostas'].items():
            print(f"[{rk}]: {rv}")

        resposta_do_usuario = input("Sua resposta é: ").lower()
        print()

        while resposta_do_usuario != "a" and resposta_do_usuario != "b" and resposta_do_usuario != "c":
            print("Você precisa digitar uma alternativa válida!")
            break

        if resposta_do_usuario == pv["resposta_certa"]:
            num_respostas_certas += 1
            print(f"Parabéns, você acertou! Você tem {num_respostas_certas} resposta(s) certa(s)!")
        else:
            print("Que pena, você errou! Mas tente novamente que vai dar tudo certo!")

    #    print('\n' * 100) - Limpar console
        print()

    qtd_perguntas = len(perguntas)
    porcentagem_de_acerto = num_respostas_certas / qtd_perguntas * 100

    print(f"Você acertou {porcentagem_de_acerto}% das perguntas!")

elif escolha == 2:
    num_respostas_certas = 0  # Contador de respostas certas
    perguntas = {
        'Pergunta 1': {
            'pergunta': "Qual das alternativas contém apenas nomes de rios?",
            'respostas': {"a": "Amazonas e Cáspio", "b": "Morto, Jordão", "c": "Azul e Amarelo"},
            'resposta_certa': "c"
        },
        'Pergunta 2': {
            'pergunta': "Quantos tentáculos tem um polvo?",
            'respostas': {"a": "6", "b": "7", "c": "8"},
            'resposta_certa': "c"
        },
        'Pergunta 3': {
            'pergunta': "Quais as respectivas invenções dos inventores Alexander Graham Bell e Galileu Galilei?",
            'respostas': {"a": "Telefone e termômetro", "b": "Lâmpada e avião", "c": "Futebol e celular"},
            'resposta_certa': "a"
        },
        'Pergunta 4': {
            'pergunta': "De que são constituídos os diamantes?",
            'respostas': {"a": "Vidro", "b": "Rocha", "c": "Carbono"},
            'resposta_certa': "c"
        },
        'Pergunta 5': {
            'pergunta': "Qual dessas aves não voa?",
            'respostas': {"a": "Condor", "b": "Pinguim", "c": "Pombo"},
            'resposta_certa': "b"
        },
    }

    for pk, pv in perguntas.items():
        print(f"{pk}: {pv['pergunta']}")

        print("Escolha uma das opções abaixo: ")
        for rk, rv in pv['respostas'].items():
            print(f"[{rk}]: {rv}")

        resposta_do_usuario = input("Sua resposta é: ").lower()
        print()

        while resposta_do_usuario != "a" and resposta_do_usuario != "b" and resposta_do_usuario != "c":
            print("Você precisa digitar uma alternativa válida!")
            break

        if resposta_do_usuario == pv["resposta_certa"]:
            num_respostas_certas += 1
            print(f"Parabéns, você acertou! Você tem {num_respostas_certas} resposta(s) certa(s)!")
        else:
            print("Que pena, você errou! Mas tente novamente que vai dar tudo certo!")

    #    print('\n' * 100) - Limpar console
        print()

    qtd_perguntas = len(perguntas)
    porcentagem_de_acerto = num_respostas_certas / qtd_perguntas * 100

    print(f"Você acertou {porcentagem_de_acerto}% das perguntas!")

elif escolha == 3:
    num_respostas_certas = 0  # Contador de respostas certas
    perguntas = {
        'Pergunta 1': {
            'pergunta': "Quem escreveu o livro O Guarani?",
            'respostas': {"a": "Machado de Assis", "b": "José de Alencar", "c": "Paulo Freire"},
            'resposta_certa': "b"
        },
        'Pergunta 2': {
            'pergunta': "Qual o maior país do mundo sem saída para o mar?",
            'respostas': {"a": "Bolívia", "b": "Cazaquistão", "c": "Mongólia"},
            'resposta_certa': "b"
        },
        'Pergunta 3': {
            'pergunta': "Em que cidade nasceu Michael Jackson?",
            'respostas': {"a": "Gary", "b": "Indianapolis", "c": "Los Angeles"},
            'resposta_certa': "a"
        },
        'Pergunta 4': {
            'pergunta': "Qual cientista descobriu os elementos rádio e polônio?",
            'respostas': {"a": "Marie Curie", "b": "Albert Einstein", "c": "Nikola Tesla"},
            'resposta_certa': "a"
        },
        'Pergunta 5': {
            'pergunta': "Qual era o ramo das indústrias de John Rockefeller?",
            'respostas': {"a": "Ouro", "b": "Veículos", "c": "Petróleo"},
            'resposta_certa': "c"
        },
    }

    for pk, pv in perguntas.items():
        print(f"{pk}: {pv['pergunta']}")

        print("Escolha uma das opções abaixo: ")
        for rk, rv in pv['respostas'].items():
            print(f"[{rk}]: {rv}")

        resposta_do_usuario = input("Sua resposta é: ").lower()
        print()

        while resposta_do_usuario != "a" and resposta_do_usuario != "b" and resposta_do_usuario != "c":
            print("Você precisa digitar uma alternativa válida!")
            break

        if resposta_do_usuario == pv["resposta_certa"]:
            num_respostas_certas += 1
            print(f"Parabéns, você acertou! Você tem {num_respostas_certas} resposta(s) certa(s)!")
        else:
            print("Que pena, você errou! Mas tente novamente que vai dar tudo certo!")

    #    print('\n' * 100) - Limpar console
        print()

    qtd_perguntas = len(perguntas)
    porcentagem_de_acerto = num_respostas_certas / qtd_perguntas * 100

    print(f"Você acertou {porcentagem_de_acerto}% das perguntas!")
else:
    print("Escolha uma das três categorias, por favor!")