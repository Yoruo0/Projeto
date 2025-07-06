contatos = []

def adicionar_contato():
    contato = {}
    contato["nome"] = input("Nome do contato: ")
    contato["telefone"] = input("Telefone do contato: ")
    contato["email"] = input("Email do contato: ")
    contato["favorito"] = False
    contatos.append(contato)
    print("Contato adicionado com sucesso")
    return

def visualizar_contatos():
    print("\nLista de contatos")
    for indice, contato in enumerate (contatos, start=1):
        status = "☆" if contato ["favorito"] else " "
        print(f"{indice}. [{status}] {contato['nome']}")
    return

def editar_contato():
    indice_ajustado = int(indice_contato) - 1
    novo_nome = input("Digite o novo nome do contato: ")
    novo_telefone = input("Dige o novo telefone do contato: ")
    novo_email = input("Digite o novo email do contato: ")
    contatos[indice_ajustado]["nome"] = novo_nome
    contatos[indice_ajustado]["telefone"] = novo_telefone
    contatos[indice_ajustado]["email"] = novo_email
    print("Contato atualizado com sucesso")
    return

def favoritar_contato():
    indice_ajustado = int(indice_contato) - 1
    contatos[indice_ajustado]["favorito"] = True
    print(f"Contato {indice_contato} adicionado aos favoritos.")
    return

def visualizar_favoritos():
    print("Lista de contatos favoritos")
    favoritos = [contato for contato in contatos if contato["favorito"]]
    for favorito in favoritos:
        print(f" - {favorito['nome']}")
    return

def apagar_contato():
    indice_ajustado = int(indice_contato) - 1
    if indice_ajustado <= 0 < len(contatos):
        contatos.pop(indice_ajustado)
        print("Contato removido com sucesso")
    return


while True:
    print("\nMenu da agenda de contatos.")
    print("1. Adicionar contato")
    print("2. Visualizar contatos")
    print("3. Editar contato")
    print("4. Marcar contato como favorito")
    print("5. Visualizar contatos favoritos")
    print("6. Excluir contato")
    print("7. Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        adicionar_contato()

    elif escolha == "2":
        visualizar_contatos()

    elif escolha =="3":
        visualizar_contatos()
        indice_contato = input("Digite o numer do contatato que deseja atualizar: ")
        editar_contato()

    elif escolha == "4":
        visualizar_contatos()
        indice_contato = input("Digite o numero do contato que desej adicionar aos favoritos: ")
        favoritar_contato()

    elif escolha == "5":
        visualizar_favoritos()

    elif escolha == "6":
        visualizar_contatos()
        indice_contato = input("Digite o numero do contato que deseja excluir: ")
        apagar_contato()


    elif escolha =="7":
        break

print("Agenda fechada")