import json

SENHA_MESTRE = "1234"

senha = input("Digite a senha mestre: ")
if senha != SENHA_MESTRE:
    print("Senha incorreta! Saindo...")
    exit()

def ler_dados():
    try:
        with open("dados.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def salvar_dados(dados):
    with open("dados.json", "w") as f:
        json.dump(dados, f, indent=4)

while True:
    print("\n=== COFRE DE DADOS PESSOAIS ===")
    print("1 - Adicionar dados")
    print("2 - Ver dados salvos")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        login = input("Login: ")
        senha_user = input("Senha: ")
        dados = ler_dados()
        dados.append({"nome": nome, "login": login, "senha": senha_user})
        salvar_dados(dados)
        print("Dados salvos com sucesso!")

    elif opcao == "2":
        dados = ler_dados()
        if not dados:
            print("Nenhum dado salvo.")
        else:
            print("\n=== DADOS SALVOS ===")
            for i, item in enumerate(dados, 1):
                print(f"{i}. Nome: {item['nome']}, Login: {item['login']}, Senha: {item['senha']}")

    elif opcao == "3":
        print("Saindo do cofre...")
        break

    else:
        print("Opção inválida!")
