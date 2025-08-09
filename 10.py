# Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

inicio = min(n1, n2)
fim = max(n1, n2)

for i in range(inicio + 1, fim):
    print(i)