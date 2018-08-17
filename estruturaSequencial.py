# https://wiki.python.org.br/ListaDeExercicios
# https://wiki.python.org.br/EstruturaSequencial

# Faça um Programa que mostre a mensagem "Alo mundo" na tela. /*
"""
print("Alo mundo")
"""
# faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
from builtins import int, input

"""num = input("Digite um numero : ")
print('Seu numero é :',num)
 """
# Faça um Programa que peça dois números e imprima a soma.
"""num1 = input("Digite o primeiro numero :")
num2 = input("Digite o segundo numero :")
soma = int (num1)+int(num2)
print(soma)
"""
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
"""nota1 = input('Digite a nota : ')
nota2 = input('Digite a nota : ')
nota3 = input('Digite a nota : ')
nota4 = input('Digite a nota : ')
media =  (int (nota1)+int(nota2)+int(nota3)+int (nota4))/4
print ('A média desse aluno é: ', media)"""

#Faça um Programa que converta metros para centímetros.
"""metros = 100
cent = input('Digite a quantidade de metros para ser convertida em cm : ')

cm = int(cent) * int (metros)
print(cent ,'metros  tem ',cm,'cm')"""

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

# Formula A = pi  x  r^2
"""pi= 3.14
num = float(input('Digite o raio : '))
raio = num ** 2
area = pi*raio
print(area)
"""
# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
altura = float(input('Digite o valor do lado/altura  do quadrado: '))
area =  altura**2
print('A  area do quadrado é : ',area)
areaQuadrado = area ** 2
print('O dobro dessa área é : ', areaQuadrado)"""

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
#Calcule e mostre o total do seu salário no referido mês.
"""horaTrabalho = float(input('Quanto voce recebe por hora trabalhada? : R$ '))
horaMes =  int(input('Quantas horas você trabalha no mês ? :'))
salario  = horaTrabalho * horaMes
print('Seu salário é de R$',salario)"""

#Faça um Programa que peça a temperatura em graus Farenheit, transforme e
#mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9)
"""fnh = int(input('Digite a quantidade de Graus em Farenheit: '))
c = (5 * (fnh-32) / 9)
print(f'A quantidade convertida é {c:.2f}ºC')"""

#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Farenheit.

"""cel = int(input('Digite a temperatura : '))
fnh = (cel-32)/1.8
print(f'A quantidade é: {fnh:.2f}ºF')
"""
#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo
"""num1 = int(input('Digite um numero :'))
num2 = int(input('Digite outro numero :'))
numReal = float(input('Digite um nuemero real'))

dobro = num1*2
metade = num2/2
print('O  dobro do primeiro é ',dobro,' com metade do segundo é  ',metade)
soma = (num1*3)+numReal
print('a soma do triplo do primeiro com o terceiro é :',soma)
cubo = numReal*3
print('O terceiro elevado ao cubo é :',cubo)"""

#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
# usando a seguinte fórmula: (72.7*altura) - 58
"""
altura= float(input('Digite sua altura: '))
resultado = float(72.7*altura) - 58
print('Seu peso ideal é :',resultado)
"""

#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
#utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

"""altura= float(input('Digite sua altura: '))
resultadoHomem = float(72.7*altura) - 58
resultadoMulher = float (62.1*altura) - 44.7
print(f'O peso ideal para um homem é:{resultadoHomem:.2f}')
print(f'\n O peso ideal para uma mulher é:{resultadoMulher:.2f}')"""
#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo
#(50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você
#faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
#Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
#Imprima os dados do programa com as mensagens adequadas.

limite = 50
multa = 4
peso = float(input('Digite a quantidade de peixes: '))
if peso <= limite:
    print(f'O Senhor pescou {peso:.2f} de peixes hoje, até mais !')
else:
    excesso = (peso - limite)*4
    print(f'O Senhor passou do limite  de {limite}KG, \n'
          f'então vocé vai pagar uma multa de 4 reais por KG \n'
          f'No total você pescou {peso}KG de peixe,entao o valor da multa é \n'
          f'{excesso:.2f}')









