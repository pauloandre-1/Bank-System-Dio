

Saldo = 3000
calc_saques=0
quantidade_depositos = 0
Depositos = []


def retirada():
    global Saldo
    global calc_saques
    limite_saque = 500
    saque = float(input("Digite um Valor de retirada: "))

    if saque > Saldo:
        print(f"Saldo insuficiente\nValor na conta: {Saldo}")
    elif saque <= 0:
        print("Saque Inválido")
    elif saque > limite_saque:
        print(f"O valor solicitado R${saque} é muito alto, apenas R${limite_saque} por saque")
    else:
        calc_saques += 1
        Saldo -= saque
        print(f"Valor R${saque:.2f} Retirado com Sucesso\nSeu saldo é de {Saldo:.2f}")

def deposito(valor):
    global Saldo
    Saldo += valor
    print(f"Depósito: {valor:.2f}\nValor na conta: {Saldo:.2f}")
    return valor



while True:
    options = input("[S]-Saque [D]-Depósito [E]-extrato [Q]-Sair: ").strip().upper()
    match options:
        case "S":
            if calc_saques >= 3:
                print("Muitas retiradas, Sistema encerrado")
                break
            retirada()
        case "D":
            valor_saque = float(input("Digite um valor para depósito: "))
            if valor_saque > 0:
                valor_depositado = deposito(valor_saque)
                Depositos.append(valor_depositado)
                quantidade_depositos += 1
            else:
                print("Depósito invalido")
        case "E":
            print(
                f"Seu Saldo: R${Saldo}\nNúmero de Depósitos: {quantidade_depositos}\nValores depositados:R${Depositos}")
        case "Q":
            print("Sistema encerrado")
            break
        case _:
            print("Opção invalida")











