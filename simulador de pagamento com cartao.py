def simular_pagamento (valor_total, parcelas, juros_mensal = 0.02):
    if parcelas <= 0:
        print("Número de parcelas inválido.")
        return

valor_total = float(input("O preço total do produto seria:"))
parcelas = int(input("Você quer parcelar em quantas vezes? "))
juros_mensal = 0.02
valor_final = valor_total * (1 + juros_mensal) ** parcelas
valor_parcela = valor_final / parcelas

print(f"Valor original: R$ {valor_total:.2f}")
print(f"Parcelado em {parcelas}x com juros de {juros_mensal * 100:.2f}% ao mês")
print(f"Valor final com juros: R$ {valor_final:.2f}")
print(f"Cada parcela fica no valor de: R$ {valor_parcela:.2f}")
