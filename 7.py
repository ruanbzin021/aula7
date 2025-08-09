"""
lista= []

n1 = int(input("Digite um numero: "))
lista.append(n1)

n2 = int(input("Digite um numero: "))
lista.append(n2)

n3 = int(input("Digite um numero: "))
lista.append(n3)

n4 = int(input("Digite um numero: "))
lista.append(n4)

n5 = int(input("Digite um numero: "))
lista.append(n5)

print(f"Entre os numeros {lista} o maior é {max(lista)}")
print(f"Entre os numeros {lista} o menor é {min(lista)}")
"""

lista= []

for i in range(5):
    n = int(input("Digite um numero: "))
    lista.append(n)
 
print(f"Entre os numeros {lista} o maior é {max(lista)}")
print(f"Entre os numeros {lista} o menor é {min(lista)}")