pedidos = []

while True:
    print("\n=== Cadastro de Pedido ===")
    nome_cliente = input("Nome do cliente: ")
    prato = input("Prato pedido: ")
    valor = float(input("Valor do pedido: R$ "))

    pedido = {
        "cliente": nome_cliente,
        "prato": prato,
        "valor": valor
    }

    pedidos.append(pedido)

    continuar = input("Deseja cadastrar outro pedido? (s/n): ").lower()
    if continuar != 's':
        break

# Mostrar pedidos cadastrados
print("\n=== Lista de Pedidos Cadastrados ===")
for i, pedido in enumerate(pedidos, start=1):
    print(f"\nPedido {i}:")
    print(f"Cliente: {pedido['cliente']}")
    print(f"Prato: {pedido['prato']}")
    print(f"Valor: R$ {pedido['valor']:.2f}")