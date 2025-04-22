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