
'''
Sistema conta com 3 operações básicas: depósito, saque, extrato.
Por enquanto, o sistema possuirá apenas um usuário, logo não é preciso autenticação (nome, conta, agência, senha, etc).

- deposito: valores positivos - deve ser armazenado em uma variável que é mostrada em extrato.
- saque: limite de 3 saques diários, com valor máximo de R$500 cada. Caso não haja saldo, informar via mensagem.
Armazenar saques em uma variável que será listada no extrato.
- extrato: Lista todos os depósitos e saques, e no final mostra o saldo da conta.
'''

menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> '''

usuario = {"saldo": 0, "numero_saques": 0, "extrato_transacoes": []}
valor_limite_saque = 500.0
LIMITE_SAQUES = 3


def deposito(usuario):
    while True:
        try:
            valor_deposito = float(input("Insira o valor que deseja depositar: R$"))
        except:
            print("Valor inválido.")
            continue
        if valor_deposito <= 0:
            print("Insira um valor valido.")
            continue
        usuario["saldo"] += valor_deposito
        usuario["extrato_transacoes"].append(f"Depósito: R${valor_deposito:.2f}")
        print("Deposito realizado com sucesso")
        break


def saque(usuario, valor_limite_saque):
    while True:
        try:
            valor_saque = float(input("Insira o valor que deseja sacar: R$"))
        except:
            print("Valor invalido")
            continue
        if valor_saque <= 0 or valor_saque > valor_limite_saque:
            print(f"Valor inválido. Lembre-se do limite de R${valor_limite_saque:.2f}.")
            continue
        if usuario["numero_saques"] >= 3:
            print(f"Você já atingiu seu limite de {LIMITE_SAQUES} saques por hoje.")
        else:
            if valor_saque > usuario["saldo"]:
                print(f"Saldo insuficiente. Seu saldo atual é de R${usuario["saldo"]:.2f}.")
            else:
                usuario["saldo"] -= valor_saque
                usuario["numero_saques"] += 1
                usuario["extrato_transacoes"].append(f"Saque: R${valor_saque:.2f}")
                print("Saque realizado com sucesso.")
        break


def extrato(usuario):
    print("### Extrato ###")
    for item in usuario["extrato_transacoes"]:
        print(item)
    print(f"Saldo em conta: R${usuario["saldo"]}")


while True:
    opcao = input(menu).lower()

    if opcao == "d":
        print("Depósito")
        deposito(usuario=usuario)
    elif opcao == "s":
        print("Sacar")
        saque(usuario=usuario, valor_limite_saque=valor_limite_saque)
    elif opcao == "e":
        print("Extrato")
        extrato(usuario=usuario)
    elif opcao == "q":
        print("Saindo da aplicação...")
        break
    else:
        print("Opção inválida. Tente novamente.")


            
    