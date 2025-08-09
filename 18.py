# Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores

lista= []

for i in range(5):
    n = int(input("Digite um numero: "))
    lista.append(n)
soma = sum(lista)

print(f"A soma dos numeros é {soma}")
print(f"Entre os numeros {lista} o maior é {max(lista)}")
print(f"Entre os numeros {lista} o menor é {min(lista)}")