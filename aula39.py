"""
Iterando strings com while
"""
#       0123456
nome = 'Matheus Volponi' #Iteráveis
#       7654321

indice = 0
novo_nome = ''
while indice < len(nome):
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)