# Altere o programa anterior para mostrar no final a soma dos números.

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro numero: "))

inicio = min(n1, n2)
fim = max(n1, n2)

lista = []

for i in range(inicio + 1, fim):
    lista.append(i)
    print(i)

soma = sum(lista)
print(soma)    