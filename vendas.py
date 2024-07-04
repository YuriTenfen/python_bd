from conexao import conecta_db

def consultar(conexao):
    print("consultar")

def inserir(conexao):
    print("inserir")

def menu_vendas(opcao):
    print("|--------------------------------|")
    print("|       Menu -> Vendas           |")
    print("|--------------------------------|")
    print("|     1 - Consultar Vendas       |")
    print("|     2 - Inserir Vendas         |")
    print("|     3 - Sair do Usuário        |")
    print("|--------------------------------|")

    conexao = conecta_db()

    while True:
        opcao = input("Escolha uma opção:")
     
        if opcao == "1":
            consultar(conexao)  
        if opcao == "2":
            inserir(conexao)
        elif opcao == "5":
            break
        else:
            print("Opção invalida, tente novamente")