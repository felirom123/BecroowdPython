"""Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.

Entrada
O arquivo de entrada contém 2 números inteiros e 1 número com duas casas decimais, representando o número, quantidade de horas trabalhadas e o valor que o funcionário recebe por hora trabalhada, respectivamente.

Saída
Imprima o número e o salário do funcionário, conforme exemplo fornecido, com um espaço em branco antes e depois da igualdade. No caso do salário, também deve haver um espaço em branco após o $.
"""
num = input()
ho1 = input()
sal = input()
n1 = int(num)
hora = int(ho1)
salario = float(sal)

salario1 =  hora * salario
linha1 = f'NUMBER = {n1}'
linha2 = f'SALARY = U$ {salario1:.2f}'

print(linha1)
print(linha2)



