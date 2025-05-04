def divisor_de_conta():
    print("=== Divisor de Conta ===")

    try:
        total = float(input("Digite o valor total da conta: R$ "))
        pessoas = int(input("Quantas pessoas irão dividir a conta? "))
        
        if pessoas <= 0:
            print("Número de pessoas inválido.")
            return
        
        incluir_taxa = input("Deseja incluir os 10% de taxa de serviço? (s/n): ").strip().lower()

        if incluir_taxa == "s":
            total_com_taxa = total * 1.10  # adiciona 10%
            print(f"Total com 10%: R$ {total_com_taxa:.2f}")
        else:
            total_com_taxa = total

        valor_por_pessoa = total / pessoas
        print(f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")

    except ValueError:
        print("Erro: por favor, digite apenas números válidos.")

divisor_de_conta()
