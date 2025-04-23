"""
Exercicio
Exiba os índices da lista
0 Maria
1 Helena
2 Matheus
"""
lista = ['Maria', 'Helena', 'Matheus']
lista.append('Joao')
indices = range(len(lista))

for indice in indices:
    print(indice, lista[indice], type(lista[indice]))