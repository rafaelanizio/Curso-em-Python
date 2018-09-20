#Faça um Programa que peça dois números e imprima o maior deles.
"""num1 =  float(input('Digite um numero \n'))
num2  = float(input('Digite outro numero \n '))
if num1 == num2 :
      print('Os numeros são iguais !0')

if num1 > num2:
    print(f'O numero {num1} é o maior')
else:
    print(f'O numero {num2} é o maior')
"""
#Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

"""num1 = float(input("Digite um numero :"))
if num1 >= 0:

      print('Positivo')
else:
      print('Negativo')"""
#Faça um Programa que verifique se uma letra digitada é "F" ou "M".
#  Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""letra = (input(' Digite uma letra :') .upper())
if letra =="F":
    print('Feminino')


elif letra =="M":
     print('Masculino')
else:
     print('Sexo invalido')

"""
#Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
def vogal(letra):
    vogais="aeiou"
    if letra.lower() not in  vogais:
    
        print("Consoante")
    else:
         print("Vogal")

letra = input("Digite uma letra: ")
print(vogal(letra))
"""
#Faça um programa para a leitura de duas notas parciais de um aluno.
#O programa deve calcular a média alcançada por aluno e apresentar:
#A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
#A mensagem "Reprovado", se a média for menor do que sete;
#A mensagem "Aprovado com Distinção", se a média for igual a dez.
"""nota1 = float(input('Digita a nota do 1º semestre : '))
nota2 = float(input('Digita a nota do 2º semestre : '))
media = (nota1+nota2)/2
if media == 10:
    print('Aprovado com distinção')
elif media >= 7:
    print('Aprovado')
else:
    print('Reprovado')
"""
#Faça um Programa que leia três números e mostre o maior deles.
"""num1 =  int(input("Digite um numero: "))
num2 =  int(input("Digite um numero: "))
num3 =  int(input("Digite um numero: "))
if num1 > num2 and num3:
    print(f'{num1} é o maior')
elif num2 > num1 and num3:
    print(f'{num2} é o maior')
else:
    print(f'{num3} é o maior')"""