while True:
    print("\n--- Comparador de Taxas Populacionais Master ---")

    while True:
        try:
            pop_a = int(input("Digite a população do país A: "))
            if pop_a > 0:
                break
            else:
                print("A população deve ser maior que zero.")
        except ValueError:
            print("Digite um número válido.")
    while True:
        try:
            pop_b = int(input("Digite a população do país B: "))
            if pop_b > 0:
                break
            else:
                print("A população deve ser maior que zero.")
        except ValueError:
            print("Digite um número válido.")

    while True:
        try:
            taxa_a = float(input("Digite a taxa de crescimento anual do país A (em %): "))
            if taxa_a > 0:
                taxa_a /= 100  # Converter para decimal
                break
            else:
                print("A taxa deve ser maior que zero.")
        except ValueError:
            print("Digite um número válido.")
    while True:
        try:
            taxa_b = float(input("Digite a taxa de crescimento anual do país B (em %): "))
            if taxa_b > 0:
                taxa_b /= 100  # Converter para decimal
                break
            else:
                print("A taxa deve ser maior que zero.")
        except ValueError:
            print("Digite um número válido.")
    if pop_a >= pop_b:
        print("\nO país A já tem população maior ou igual à do país B.")
    else:
        anos = 0
        while pop_a < pop_b:
            pop_a += pop_a * taxa_a
            pop_b += pop_b * taxa_b
            anos += 1

        print(f"\nSerão necessários {anos} anos para a população do país A ultrapassar ou igualar a do país B.")
        print(f"População final de A: {int(pop_a)} habitantes")
        print(f"População final de B: {int(pop_b)} habitantes")
    repetir = input("\nDeseja realizar outra comparação? (s/n): ").strip().lower()
    if repetir != 's':
        print("Programa encerrado.")
        break