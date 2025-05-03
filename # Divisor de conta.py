def divisor_de_conta():
    print("=== Divisor de Conta ===")

    try:
        total = float(input("Digite o valor total da conta: R$ "))
        pessoas = int(input("Quantas pessoas irão dividir a conta? "))
        
        if pessoas <= 0:
            print("Número de pessoas inválido.")
            return
        
        valor_por_pessoa = total / pessoas
        print(f"Cada pessoa deve pagar: R$ {valor_por_pessoa:.2f}")

    except ValueError:
        print("Erro: por favor, digite apenas números válidos.")

divisor_de_conta()
