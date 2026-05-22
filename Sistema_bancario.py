

extrato = 3000
max_retiradas=0
cont = 0
Depositos = []
while True:
    def retirada():
        global extrato
        global max_retiradas
        limite_saque = 500
        saque = float(input("Digite um Valor de retirada: "))
        if saque > extrato:
            print(f"Saldo insuficiente\nValor na conta: {extrato}")
        elif saque > limite_saque:
            print(f"O valor solicitado R${saque} é muito alto, apenas R${limite_saque} por saque")
        else:
            max_retiradas += 1
            extrato -= saque
            print(f"Valor R${saque:.2f} Retirado com Sucesso\nSeu saldo é de {extrato:.2f}")

    def deposito():
        global extrato
        valor = float(input("Digite um valor para deposito: "))
        extrato += valor
        print(f"Deposito: {valor:.2f}\nValor na conta: {extrato:.2f}")
        return valor

    opitions = input("1-Saque 2-Depósito 3- Para ver o extrato: ").strip()
    if max_retiradas>=3:
       print("Muitas retiradas, Sistema encerrado")
       break
    elif opitions == "1":
        retirada()

    elif opitions == "2":
        valor_depositado = deposito()
        Depositos.append(valor_depositado)
        cont +=1
    elif opitions == "3":
        print(f"Seu extrato: R${extrato}\nNúmero de Depositos: {cont}\nValores depositados:{Depositos}")
    else:
       print("Opção invalida")









