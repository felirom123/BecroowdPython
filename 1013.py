"""Faça um programa que leia três valores e apresente o maior dos três valores lidos seguido da mensagem “eh o maior”. Utilize a fórmula:



Obs.: a fórmula apenas calcula o maior entre os dois primeiros (a e b). Um segundo passo, portanto é necessário para chegar no resultado esperado.

Entrada
O arquivo de entrada contém três valores inteiros.

Saída
Imprima o maior dos três valores seguido por um espaço e a mensagem "eh o maior".

abs = valor absoluto, ou seja um numero que seja positivo ou zero, exemplo o numero absoluto de -5 e 5, 3 de5  tambem e 5
"""
a1 = input().split()
a, b, c = int(a1[0]), int(a1[1]), int(a1[2])
maiorAB = (a + b + abs (a - b)) / 2 # primeiro sera computado o absoluto que sempre retornara positivo, dps todas as somas divido por 2
maiorXC = (c + maiorAB + abs(c - maiorAB)) / 2 # fara a mesma coisa so que com o resultado da equacao de cima
linha1 = f'{maiorXC:.0f} eh o maior'
print(linha1)



