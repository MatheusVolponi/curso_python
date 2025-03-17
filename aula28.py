"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Se nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for gitiado em nome ou idade:
    exiba "Desculpe, voce deixou campos vazios."
"""
nome = input('Digite seu nome:')
idade = input('Digite sua idade:')
espaco = ' '

if nome and idade:
    print('Seu nome é', nome)
    print(f'Seu nome invertido é', nome[::-1])
    if espaco in nome:
        print('Seu nome contém espaços')
    else:
        print('Seu nome não contém espaços')
    print('Seu nome tem', len(nome), 'letras')
    print('A primeira letra do seu nome é', nome[0])
    print('A última letra do seu nome é:', nome[-1])
else:
    print('Desculpe, voce deixou campos vazios')