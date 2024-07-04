"""Leia quatro valores inteiros A, B, C e D. A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).

Entrada
O arquivo de entrada contém 4 valores inteiros.

Saída
Imprima a mensagem DIFERENCA com todas as letras maiúsculas, conforme exemplo abaixo, com um espaço em branco antes e depois da igualdade.
"""
a1 = input()
b1 = input()
c1 = input()
d1 = input()

a = int(a1)
b = int(b1)
c = int(c1)
d = int(d1)

diferenca = ((a * b) - (c * d))
linha1 = f'DIFERENCA = {diferenca}'
print(linha1)