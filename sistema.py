menu = """
##### Menu ######
[a] Depositar
[b] Sacar
[c] Extrato
[s] Sair

Informe abaixo => """

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
LIMITE_SAQUE = 3

while True: 

    opcao = input(menu)

    if opcao == "a":
        print("\nVocê selecionou a opção: Depósito.")
        
        valor = float(input("\nInforme o valor a depositar: R$ "))
       
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"O depósito de R$ {valor:.2f} foi realizado com sucesso!")
        else:
            print("\nO valor de depósito deve ser um valor positivo.")


    elif opcao == "b":
        print("\nVocê selecionou a opção: Sacar.")
        
        if numero_saque < LIMITE_SAQUE:
            valor = float(input("\nInforme o valor a sacar: R$ "))
            if 0 < valor <= saldo:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saque += 1
                print(f"O saque de R$ {valor:.2f} foi realizado com sucesso!")
            elif valor > saldo:
                print("\nSaldo insuficiente!")
            else:
                print("\nO valor de saque deve ser um valor positivo.")
        else:
            print("\nNúmero máximo de saques atingido!")

    elif opcao == "c":
        print("\nVocê selecionou a opção: Extrato.")
        if extrato:
            print("##### Extrato #####")
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")
        else:
            print("\nNenhuma movimentação realizada.")

    elif opcao == "s":
        print("Saindo...")
        break 
   
    else: 
        print("Opção invalida, selecione outra opção!!")