Menu = """

[A] Depositar
[B] Sacar
[C] Extrato
[D] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(Menu)
    
    if opcao == "A":
        valor = float(input("Informe o valor de depósito:\n"))
        
        if valor > 0:
            saldo += valor  
            extrato += f"Depósito : R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou! O valor digitadado e invalido!.")
       
    elif opcao == "B":
        valor = float(input("Informe o valor de saque:\n"))
    
        excedeu_saldo = valor > saldo
    
        excedeu_limite = valor > limite
    
        excedeu_saques = numero_saques >= LIMITE_SAQUES
    
        if excedeu_saldo:
            print("Operação falhou! Voçe não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou! O valor de saque excede o limite.")
    
        elif excedeu_saques:
            print("Operação falhou! Numero de saques ja excedido.")

        
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor :.2f}\n"
            numero_saques += 1 
        
        else:
            print("Operação falhou! O valor informado é invalido")
        
    elif opcao == "C":
        print("\n===================== EXTRATO =====================")
        print("Não foram realizados movimentações." if not extrato else extrato) 
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================================")
        
    elif opcao == "D":
        break

else:
    print("Operacao invalida, digite outro numero!.")
        