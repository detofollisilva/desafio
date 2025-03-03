menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao =="d":
        valor = float(input("Digite o valor do depósito R$"))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido")


    elif opcao == "s":
        valor = float(input("Digite o valor do saque R$"))
        
        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente")

        elif excedeu_limite:
            print("Operação falhou! Limite excedido")

        elif excedeu_saques:
            print("Operação falhou! Limite de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
    elif opcao == "e":
        print(f"\n ========== EXTRATO ==========")
        print(f"Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo atual: R$ {saldo:.2f}\n")  
        print(" =============================\n")

    elif opcao == "q":
        break

    else:
            print("Operação Inválida, por favor selecione novamente a operação desejada")
 
      



        
