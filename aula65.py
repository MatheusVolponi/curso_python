"""
Introdução às funções (def) em Python
Funções são trechos de código usados para replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos) e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""
# def Print(a, b, c):
#     print('Várias')
#     print('Várias')
#     print('Várias')
#     print('Várias')

# def Imprimir(a, b, c):
#     print(a, b, c)

# Imprimir(1, 2, 3)
# Imprimir(4, 5, 6)

def saudacao(nome = 'Sem nome'):
    print(f'Olá, {nome}!')

saudacao('Matheus')
saudacao('Ana')
saudacao('Luiz')
saudacao()