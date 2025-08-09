'''
Supondo que a população de um país A seja da ordem de 80000 habitantes 
com uma taxa anual de crescimento de 3% e que a população de B seja 200000 habitantes 
com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários 
para que a população do país A ultrapasse ouiguale a população do país B, mantidas as taxas de crescimento.
'''

popa = 8000
popb = 20000
taxaa = 0.03 # 3%
taxab = 0.015 # 1.5%
ano = 0

while popa <= popb:
    popa += popa * taxaa
    popb += popb * taxab
    ano += 1
    print(f"Ano {ano} : Pop a = {int(popa)}, Pop b = {int(popb)}")
print(f"A população A ultrapassou ou igualou B em {ano}")    
