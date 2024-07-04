"""Leia os quatro valores correspondentes aos eixos x e y de dois pontos quaisquer no plano, p1(x1,y1) e p2(x2,y2) e calcule a distância entre eles, mostrando 4 casas decimais após a vírgula, segundo a fórmula:

Distancia = raiz quadrada de (x2-x1)²+ (y2 - y1)²

Entrada
O arquivo de entrada contém duas linhas de dados. A primeira linha contém dois valores de ponto flutuante: x1 y1 e a segunda linha contém dois valores de ponto flutuante x2 y2.

Saída
Calcule e imprima o valor da distância segundo a fórmula fornecida, com 4 casas após o ponto decimal.
"""
import math # importar essa biblioteca para funcionar a funcao math.sqrt() que calcula a raiz quadrada do numero dentro do parenteses
a1 = input().split()
b1 = input().split()
x1, y1 = float(a1[0]), float(a1[1])
x2, y2 = float(b1[0]), float(b1[1])

distancia = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 )
linha1 = f'{distancia:.4f}'
print(linha1)
