# Desempacotamento em chamadas de métodos e funções

string = 'ABCD'
lista = ['Maria', 'Helena', 'Eduarda']
tupla = 'Python', 'é', 'legal'
salas = [
    #0         1
    ['Maria', 'Helena'], #0
    #0
    ['Elaine'], #1
    #0           1       2
    ['Matheus', 'João', 'Eduarda', (0, 10, 20, 30, 40)] #2
]



# a, b, c = lista 
# print(a, c)

print(*lista)
print(*string)
print(*tupla)
print(*salas, sep='\n')