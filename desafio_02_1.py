import textwrap

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [cc]\tNovo Cliente
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

# função depósito
def f_op_deposito(saldo, vlr_deposito, extrato, /):
    if vlr_deposito < 0.0:
        print("Este não é um valor válido. Repita a operação.")
    else:
        saldo += vlr_deposito
        extrato += f"(+) Depósito no valor de R$ {vlr_deposito:.2f}\n" 
        print("Depósito realizado com sucesso.")
        print(f"Seu saldo atual é de: R${saldo:.2f}")
    return saldo, extrato

# função saque
def f_op_saque(*, saldo, vlr_saque, extrato, limite_vlr_saque, qtde_saque, limite_qtde_saque):

    saldo_insuficiente = vlr_saque > saldo

    excedeu_limite_vlr_saque = vlr_saque > limite_vlr_saque 

    excedeu_limite_saques_diario = limite_qtde_saque < qtde_saque

    if saldo_insuficiente:
            print("Saldo Insuficiente, tente novamente.")
    elif excedeu_limite_vlr_saque:
            print("Excedeu o limite no valor do saque.")
    elif excedeu_limite_saques_diario:
            print("Excedeu o limite de saques diários.")
    elif vlr_saque > 0.0:
            saldo -= vlr_saque
            qtde_saque += 1
            extrato += f"(-) Saque no valor de R$ {vlr_saque:.2f}\n" 
            print("Saque realizado com sucesso.")
            print(f"Seu saldo atual é de: R${saldo:.2f}")
    else:
        print("Valor Inválido.")
    
    return saldo, extrato

#função extrato
def f_op_extrato(saldo, /, *, extrato):
    print("\n------ Extrato Bancário ----------")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSeu saldo atual é de: R${saldo:.2f}")
    print("\n------ Extrato Bancário ----------")

#função criar cliente
def f_criar_cliente(clientes):
     cliente_cpf = int(input("Insira o CPF do cliente: "))
     cliente = f_filtrar_cliente(cliente_cpf, clientes)

     if cliente:
        print("Este cliente já está cadastrado no sistema.")
        return
     
     cliente_nome = (input("Insira o nome do cliente: "))
     cliente_dt_nasc = (input("Insira a data de nascimento do cliente: "))
     cliente_endereco = (input("Insira o endereço do cliente: "))

     clientes.append({"cliente_nome" : cliente_nome, "cliente_dt_nasc" : cliente_dt_nasc, "cliente_cpf" : cliente_cpf, "cliente_endereco" : cliente_endereco })

     print("Cliente criado com sucesso.")

#função pesquisar cliente
def f_filtrar_cliente(cliente_cpf, clientes):
     clientes_filtrados = [cliente for cliente in clientes if cliente["cliente_cpf"] == cliente_cpf]
     return clientes_filtrados[0] if clientes_filtrados else None

#função criar contas
def f_criar_conta(agencia, nro_conta, clientes):
     cliente_cpf = int(input("Insira o número do cpf"))
     cliente = f_filtrar_cliente(cliente_cpf, clientes)

     if cliente:
          print("Conta criada com sucesso.")
          return{"agencia" : agencia, "nro_conta" : nro_conta, "cliente" : cliente}
     
     print("Cliente não encontrado.")

#função listar contas
def f_listar_contas(contas):
     for conta in contas:
          linha = f"""\
            Agência: \t {conta["agencia"]}
            Conta Corrente: \t \t {contas["nro_conta"]}
            Titular: \t {conta["cliente"]["cliente_nome"]}
            """
          print("=" * 100)
          print(textwrap.dedent(linha))

    

def main():

    agencia = 1001
    saldo = 0
    saldo = float(saldo) 
    qtde_saque = 0 
    LIMITE_QTDE_SAQUE = 3
    limite_vlr_saque = 500.0
    extrato = ""
    clientes = []
    contas = []


    while True:

        opcao = menu()

        #operação depósito
        if opcao == "d":
            vlr_deposito = float(input("Insira o valor desejado para depósito: "))
            saldo, extrato = f_op_deposito(saldo, vlr_deposito, extrato)
        
        # operação saque
        elif opcao == "s":
            vlr_saque = float(input("Informe o valor desejado para saque: "))
            saldo, extrato = f_op_saque(
                saldo = saldo, 
                vlr_saque = vlr_saque, 
                extrato = extrato,
                limite_vlr_saque = limite_vlr_saque,
                qtde_saque= qtde_saque,
                limite_qtde_saque = LIMITE_QTDE_SAQUE,
                )

        #operação extrato
        elif opcao == "e":
             f_op_extrato(saldo, extrato=extrato)
        
        #operação criar clientes
        elif opcao == "cc":
             f_criar_cliente(clientes)
        
        #operação criar conta
        elif opcao == "nc":
            nro_conta = len(contas) + 1
            conta = f_criar_conta(agencia, nro_conta, clientes)

            if conta:
                 contas.append(conta)

        # operação listar contas
        elif opcao == "lc":
             f_listar_contas(contas)    

        # operação sair do programa
        elif opcao == "q":
            break
        
        # operação opção inválida.
        else:
            print("Opção Inválida, tente novamente.")

main()





