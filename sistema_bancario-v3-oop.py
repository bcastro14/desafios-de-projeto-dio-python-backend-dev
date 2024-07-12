
'''
- deposito: valores positivos - deve ser armazenado em uma variável que é mostrada em extrato.
- saque: limite de 3 saques diários, com valor máximo de R$500 cada. Caso não haja saldo, informar via mensagem.
Armazenar saques em uma variável que será listada no extrato.
- extrato: Lista todos os depósitos e saques, e no final mostra o saldo da conta.

v2: Serão adicionadas duas novas funções:
- criar usuário (cliente do banco): usuário é composto por nome, data de nasc, cpf e endereço
Endereço é uma string no formato logradouro - bairro - cidade - UF.
CPF é armazenado somente em numeros, e não pode haver mais de um usuário com o memso cpf.
- criar conta corrente (vincular com usuário): Conta é composta por agência, num da conta, usuário.
O num da conta é sequencial. O num da agência é fixo "0001"
Um usuário pode ter mais de uma conta, mas cada conta pertence a só um usuário.
- [opcional] listar contas, etc
'''


def checa_conta_existe(contas, msg_caso_nao_encontrado="Nenhuma conta encontrada com esse número"):
    num_conta = pega_inteiro("Qual o número da conta?")

    conta_existe = False
    for conta in contas:
        if conta['numero_conta'] == num_conta:
            conta_encontrada = conta
            conta_existe = True
    if not conta_existe:
        print(msg_caso_nao_encontrado)
        return None
    else:
        return conta_encontrada


def pega_float_positivo(mensagem_de_input):
    while True:
        try:
            valor = float(input(mensagem_de_input))
        except:
            print("Valor inválido.")
            continue
        if valor <= 0:
            print("O valor deve ser positivo.")
            continue
        else:
            return valor


def deposito(contas):
    conta = checa_conta_existe(contas)
    if conta == None:
        return None
    
    print(f"Conta: {conta['numero_conta']}. Agência: {conta['numero_agencia']}")
    valor_deposito = pega_float_positivo("Insira o valor que deseja depositar: R$")
    conta['saldo'] += valor_deposito
    conta['extrato_transacoes'].append(f"Depósito: R${valor_deposito:.2f}")
    print("Deposito realizado com sucesso")


def saque(contas, valor_limite_saque):
    conta = checa_conta_existe(contas)
    if conta == None:
        return None

    while True:
        print(f"Conta: {conta['numero_conta']}. Agência: {conta['numero_agencia']}")
        valor_saque = pega_float_positivo("Insira o valor que deseja sacar: R$")
        if valor_saque > valor_limite_saque:
            print(f"Valor inválido. Lembre-se do limite de R${valor_limite_saque:.2f}.")
            continue
        if conta['quantidade_saques'] >= 3:
            print(f"Você já atingiu seu limite de {LIMITE_SAQUES} saques por hoje.")
        else:
            if valor_saque > conta['saldo']:
                print(f"Saldo insuficiente. Seu saldo atual é de R${conta['saldo']:.2f}.")
            else:
                conta['saldo'] -= valor_saque
                conta['quantidade_saques'] += 1
                conta['extrato_transacoes'].append(f"Saque: R${valor_saque:.2f}")
                print("Saque realizado com sucesso.")
        break


def extrato(contas):
    conta = checa_conta_existe(contas)
    if conta == None:
        return None

    print(f"Conta: {conta['numero_conta']}. Agência: {conta['numero_agencia']}")
    print("### Extrato ###")
    for item in conta['extrato_transacoes']:
        print(item)
    print(f"Saldo em conta: R${conta['saldo']}")


def confimar_escolha(valor_inserido):
    while True:
        escolha = input(f"\nVocê digitou '{valor_inserido}'. Está correto?\nDigite 'S' para confirmar e salvar ou 'N' para digitar novamente: ")
        print("")
        if escolha.upper() == 'S':
            return True
        elif escolha.upper() == 'N':
            return False
        else:
            tente_novamente()


def tente_novamente():
    print("Input inválido. Tente novamente")


def pega_inteiro(mensagem_de_input):
    while True:
        try:
            cpf = int(input(mensagem_de_input + "\n"))
        except:
            tente_novamente()
            continue
        if confimar_escolha(cpf):
            break
    return cpf


def cria_usuario(usuarios): 
    cpf = pega_inteiro("Digite o cpf do usuário (somente números):")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Um usuário com esse CPF já existe.\nRetornando ao menu principal.")
            return None
        
    while True:
        nome = input("Digite o nome completo do usuário:\n")
        if confimar_escolha(nome):
            break
    
    while True:
        data_nascimento = input("Digite a data de nascimento do usuário no formato dd/mm/yyyy:\n")
        if len(data_nascimento) != 10:
            tente_novamente()
            continue
        if confimar_escolha(data_nascimento):
            break

    while True:
        endereco = input("Digite o endereço do usuário no formato logradouro-bairro-cidade-UF:\n")
        if confimar_escolha(endereco):
            break
    novo_usuario = {'nome':nome,
                    'data_nascimento':data_nascimento,
                    'cpf':cpf,
                    'Endereço':endereco}
    usuarios.append(novo_usuario)
    print(f"O usuário {nome}, de CPF {cpf}, com data de nascimento {data_nascimento}, e endereço '{endereco}' foi criado com sucesso!")


def cria_conta(usuarios, contas, num_de_contas):
    cpf_do_usuario = pega_inteiro("Qual o CPF do usuário a quem irá pertencer a conta?")

    usuario_valido = False
    for user in usuarios:
        if cpf_do_usuario == user['cpf']:
            usuario = user
            usuario_valido = True
    
    if not usuario_valido:
        print("Não existe um usuário com esse CPF. Crie um novo usuário antes de criar uma nova conta.")
        return None
    
    numero_conta = num_de_contas + 1
    numero_agencia = "0001"
    saldo = 0
    numero_saques = 0
    extrato_transacoes = []
    print("\nCriando uma nova conta...")
    nova_conta = {'usuario': usuario,
                  'numero_conta': numero_conta,
                  'numero_agencia': numero_agencia,
                  'saldo': saldo,
                  'quantidade_saques': numero_saques,
                  'extrato_transacoes': extrato_transacoes}
    contas.append(nova_conta)
    print(f"Uma conta foi criada com sucesso para o usuário {nova_conta['usuario']['nome']}, de CPF {nova_conta['usuario']['cpf']}.")
    print(f"Número da conta: {nova_conta['numero_conta']}. Agência: {nova_conta['numero_agencia']}")


def main(menu, valor_limite_saque):
    usuarios = []
    contas = []
    num_de_contas = 0

    while True:
        opcao = input(menu).lower()

        if opcao == "d":
            print("Depósito")
            deposito(contas)
        elif opcao == "s":
            print("Sacar")
            saque(contas, valor_limite_saque)
        elif opcao == "e":
            print("Extrato")
            extrato(contas)
        elif opcao == "n":
            print("Criar novo usuário")
            cria_usuario(usuarios)
        elif opcao == "c":
            print("Criar conta corrente para usuário")
            cria_conta(usuarios, contas, num_de_contas)
        elif opcao == "q":
            print("Saindo da aplicação...")
            break
        else:
            print("Opção inválida. Tente novamente.")


# conta
# {'usuario': usuario,
# 'numero_conta': numero_conta,
# 'numero_agencia': numero_agencia,
# 'saldo': saldo,
# 'quantidade_saques': numero_saques,
# 'extrato_transacoes': extrato_transacoes}

# usuario
# {'nome':nome,
# 'data_nascimento':data_nascimento,
# 'cpf':cpf,
# 'Endereço':endereco}

LIMITE_SAQUES = 3
menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[n] Criar novo usuário
[c] Criar conta corrente para usuário
[q] Sair

=> '''

main(menu, valor_limite_saque=500.0)


# TO DO: Depois adicionar funções pra listar usuários, listar contas, remover usuários (que não possuam contas), e remover contas.