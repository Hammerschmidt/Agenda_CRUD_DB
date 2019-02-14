from Database import *


def Inserir():
    nome = input("Digite o nome: ")
    email = input("Digite o e-mail: ")
    p = insertPessoa(nome, email)

    inserirEnd = True
    while inserirEnd:
        print("Adicionar um endereço? s/n")
        op = input()
        if op == 's':
            rua = input("Digite o nome da rua: ")
            numero = input("Digite o número da rua: ")
            cep = input("Digite o CEP: ")
            insertEndereco(rua, numero, cep, p)
        elif op == 'n':
            inserirEnd = False

    inserirTel = True
    while inserirTel:
        print("Deseja adicionar um telefone? s/n")
        op = input()
        if op == 's':
            numero = input("Digite o numero do telefone: ")
            tipo = input("Digite o tipo do telefone: ")
            insertTelefone(numero, tipo, p)
        elif op == 'n':
            inserirTel = False


def Atualizar():
    nome = input("Qual nome você deseja atualizar? ")
    p = getPessoa(nome)

    if p != None:
        print("Editar nome? s/n")
        op = input()
        if op == 's':
            p.nome = input("Digite o nome: ")

        print("Editar e-mail? s/n")
        op = input()
        if op == 's':
            p.email = input("Digite o e-mail: ")
        updatePessoa(p)
        enderecos = getEnderecos(p)
        for e in enderecos:
            print("Editar endereco " + e.rua + "? s/n")
            op = input()
            if op == 's':
                e.rua = input("Digite o nome da rua: ")
                e.numero = input("Digite o numero da rua: ")
                e.cep = input("Digite o CEP: ")
                updateEndereco(e)

        telefones = getTelefones(p)
        for t in telefones:
            print("Editar telefone " + str(t.numero) + "? s/n")
            op = input()
            if op == 's':
                t.numero = input("Digite o numero do telefone: ")
                t.tipo_numero = input("Digite o tipo do telefone: ")
                updateTelefone(t)

    else:
        print("Pessoa não existente.")

def Listar():
    pessoas = getPessoas()
    for pessoa in pessoas:
        print("Nome: " + pessoa.nome)
        print("E-mail: " + pessoa.email)
        enderecos = getEnderecos(pessoa)
        for endereco in enderecos:
            print("Rua: " + endereco.rua)
            print("Número: " + endereco.numero)
            print("CEP: " + endereco.cep)
            telefones = getTelefones(pessoa)

        for telefone in telefones:
            print("Número: " + str(telefone.numero))
            print("Tipo: " + telefone.tipo_telefone)

def Deletar():
    nome = input("Qual nome você deseja apagar? ")
    deletarPessoa(nome)
    print("Pessoa apagada com sucesso.")




while True:
    print("1 - Adicionar novo contato")
    print("2 - Atualizar contato")
    print("3 - Apagar contato")
    print("4 - Listar contato")
    print("0 - Sair")

    op = int(input("\nOpções: "))
    if op == 1:
        Inserir()
    elif op == 2:
        Atualizar()
    elif op == 3:
        Deletar()
    elif op == 4:
        Listar()
    elif op == 0:
        quit()
