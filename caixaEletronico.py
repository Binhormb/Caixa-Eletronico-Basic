
saldo = 1020

def caixaEletronico():
    
    global saldo

    while True:
        print("=============================================")
        print(f"Saldo: R$ {saldo}")
        print("1 - Sacar")
        print("2 - Depositar")
        print("=============================================")
        resposta = input("Escolha um número, por favor! ")

        if resposta == "1" or resposta.lower() == "sacar":
            while True:
                try:
                    sacar = float(input("Quanto deseja sacar? R$ "))
                    if sacar <= saldo:
                        saldo -= sacar
                        print(f"Saque realizado com sucesso. Novo saldo: R$ {saldo}")
                        break
                    else:
                        print("Seu saldo é insuficiente.")
                except ValueError:
                    print("Por favor, digite um valor numérico.")
            break

        elif resposta == "2" or resposta.lower() == "depositar":
            while True:
                try:
                    deposito = float(input("Quanto você deseja depositar? R$ "))
                    saldo += deposito
                    print(f"Depósito realizado com sucesso. Novo saldo: R$ {saldo}")
                    break
                except ValueError:
                    print("Por favor, digite um valor numérico.")
            break 
        
        else:
            print("Por favor, digite uma opção válida (1, 2, sacar, depositar).")
            continue  

caixaEletronico()
