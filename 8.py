# Faça um programa que leia 5 números e informe a soma e a média dos números.
'''
n1 = int(input('Digite a primeira nota: '))

n2 = int(input('Digite a segunda nota: '))

n3 = int(input('Digite a terceira nota: '))

n4 = int(input('Digite a quarta nota: '))


med = (n1 + n2 + n3 + n4) / 4

if med < 5 and med > 1:
    print(f'Sua média é {med} e você está reprovado!')

elif med >= 5:
    print(f'Sua média é {med} e você está aprovado!')

else:
    print(f'Sua média é ZERO e você tá fudido')
'''
lista= []

for i in range(5):
    n = int(input("Digite um numero: "))
    lista.append(n)

soma = sum(lista)
media = soma / 5
print(f"A Soma total é {soma} e a média é {media}")