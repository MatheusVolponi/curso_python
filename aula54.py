"""
Faça uma lista de compras com lista
O usuário deve ter a possibilidade de inserir, apagar e listrar valores em sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
"""

lista = []
while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]
        except:
            print('Não foi possível apagar este índice')

    elif opcao == 'l':

        if len(lista) == 0:
            print('Nada para listar')
        
        for i, valor in enumerate(lista):
            print(i, valor)