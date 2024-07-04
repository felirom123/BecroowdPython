"""Leia um valor inteiro. A seguir, calcule o menor número de notas possíveis (cédulas) no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2 e 1. A seguir mostre o valor lido e a relação de notas necessárias.

Entrada
O arquivo de entrada contém um valor inteiro N (0 < N < 1000000).

Saída
Imprima o valor lido e, em seguida, a quantidade mínima de notas de cada tipo necessárias, conforme o exemplo fornecido. Não esqueça de imprimir o fim de linha após cada linha, caso contrário seu programa apresentará a mensagem: “Presentation Error”.
"""
t = input()
t1 = int(t)
print(t1)

nota100 = t1 // 100
t1 = t1 % 100

nota50 = t1 // 50
t1 = t1 % 50

nota20 = t1 // 20
t1 = t1 % 20

nota10 = t1 // 10
t1 = t1 % 10

nota5 = t1 // 5
t1 = t1 % 5

nota2 = t1 // 2
t1 = t1 % 2

nota1 = t1 // 1


print(f'{nota100} nota(s) de R$ 100,00')
print(f'{nota50} nota(s) de R$ 50,00')
print(f'{nota20} nota(s) de R$ 20,00')
print(f'{nota10} nota(s) de R$ 10,00')
print(f'{nota5} nota(s) de R$ 5,00')
print(f'{nota2} nota(s) de R$ 2,00')
print(f'{nota1} nota(s) de R$ 1,00')


   

