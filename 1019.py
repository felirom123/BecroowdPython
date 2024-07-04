"""Leia um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma fábrica, e informe-o expresso no formato horas:minutos:segundos.

Entrada
O arquivo de entrada contém um valor inteiro N.

Saída
Imprima o tempo lido no arquivo de entrada (segundos), convertido para horas:minutos:segundos, conforme exemplo fornecido.
"""
n = input()
n1 = int(n)

horas = n1 // 3600
n1 = n1 % 3600

minutos =  n1 // 60
n1 = n1 % 60

segundos = n1 // 1

print(f'{horas}:{minutos}:{segundos}')