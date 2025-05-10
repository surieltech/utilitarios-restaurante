mesas = []

def cadastrar_mesa():
    numero = int(input("Número da mesa: "))
    lugares = int(input("Quantidade de lugares: "))
    mesa = {
        "numero": numero,
        "lugares": lugares,
        "status": "livre"  # Status padrão
    }
    mesas.append(mesa)
    print("Mesa cadastrada com sucesso!\n")

def consultar_mesas():
    if not mesas:
        print("Nenhuma mesa cadastrada.\n")
        return
    print("\nMesas cadastradas:")
    for mesa in mesas:
        print(f"Mesa {mesa['numero']} - Lugares: {mesa['lugares']} - Status: {mesa['status']}")
    print()

def atualizar_status():
    numero = int(input("Digite o número da mesa para atualizar o status: "))
    for mesa in mesas:
        if mesa["numero"] == numero:
            novo_status = input("Novo status (livre/ocupada): ").lower()
            if novo_status in ["livre", "ocupada"]:
                mesa["status"] = novo_status
                print("Status atualizado!\n")
            else:
                print("Status inválido. Use 'livre' ou 'ocupada'.\n")
            return
    print("Mesa não encontrada.\n")

# Menu principal
while True:
    print("=== Sistema de Mesas ===")
    print("1. Cadastrar nova mesa")
    print("2. Consultar mesas")
    print("3. Atualizar status de uma mesa")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        cadastrar_mesa()
    elif opcao == "2":
        consultar_mesas()
    elif opcao == "3":
        atualizar_status()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida.\n")