"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se esse número é par ou ímpar. Caso o usuário não digite um número inteiro, informe que não é
um número inteiro.
"""
numero = input('Digite um Número Inteiro:')

try:
    numero_int = int(numero)
    if numero_int % 2 == 0:
        print('O número digitado é par')
    else:
        print('O número digitado é ímpar')
except:
    print('O número digitado não é um inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no hórario descrito, 
exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
hora = input('Digite a hora atual:')

try:
    hora_int = int(hora)
    
    if hora_int >= 0 and hora_int <= 11: 
        print('Bom dia')

    elif hora_int >= 12 and hora_int <= 17:
        print('Boa tarde')

    elif hora_int >= 18 and hora_int <= 23:
        print('Boa noite')

    else:
        print('Hora não reconhecida')
except:
    print('Por favor digite apenas números inteiros.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos 
escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior
que 6 escreva "Seu nome é muito grande".
"""
nome = input('Digite seu primeiro Nome: ')
tamanho_nome = len(nome)

if tamanho_nome > 1:
    if tamanho_nome <= 4:
        print('Seu nome é curto')
    elif tamanho_nome >= 5 and tamanho_nome <= 6:
        print('Seu nome é normal') 
    elif tamanho_nome > 6:
        print('Seu nome é muito grande')
else:
    print('Digite mais de uma letra.')