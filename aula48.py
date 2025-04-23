"""
Listas em Python
Tipo List - Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend, +
Create Read Update   Delete
Criar, ler, alterar, apagar = lista[i] (CRUD) 
"""

lista = [10, 20, 30, 40]
lista.append('Matheus')
nome = lista.pop()
lista.append(1233)
del lista[-1]
# lista.clear()
lista.insert(0, 5)  
print(lista)

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b
lista_a.extend(lista_b)
print(lista_c)
print(lista_a)

"""
Cuidados com dados mutáveis
= - copiado o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
lista_x = ['Matheus', 'Maria', 1, True, 1.2]
lista_y = lista_x.copy()

lista_x[0] =  'Qualquer coisa'
print(lista_x)
print(lista_y)
