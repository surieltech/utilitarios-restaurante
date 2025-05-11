print("=== Calculadora de Troco ===")
preco = float(input("Digite o valor total: R$ "))
pago = float(input("Digite o valor pago pelo cliente: R$ "))

troco = pago - preco

if troco < 0:
    print(f"O valor pago é insuficiente, ainda faltam R$ {abs(troco):.2f}")
elif troco == 0:
    print("O valor pago é exato. Não há troco.")
else:
    print(f"O troco é de R$ {troco:.2f}")