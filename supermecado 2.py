import os

listaFinal = []
listaProd = {}

def menu():
    print("----------------MENU---------------- \n"
          "[1] - Registrar produto. \n"
          "[2] - Listar produtos. \n"
          "[3] - Pesquisar produto. \n"
          "[4] - Alterar preço ou quantidade do produto. \n"
          "[5] - Remover produto. \n"
          "[6] - Sair. \n")

def registrar():
    os.system('cls')
    opcaor = '1'
    while True:
        if opcaor == '1':
            print("----------Registrar produto-----------")
            nome = input("Digite o nome do produto: ")
            listaProd['nome'] = nome
            valor = float(input("Digite o valor do produto: "))
            listaProd['valor'] = valor
            quant = int(input("Digite a quantidade inicial do produto em stock: "))
            listaProd['quantidade'] = quant
            codigo = input("Digite o codigo de registro do produto: ")
            listaProd['codigo'] = codigo
            listaFinal.append(listaProd.copy())
            print("Produto Registrado com sucesso!\n")
            opcaor = input("Deseja registrar outro produto? \n"
                              "[1] - SIM \n"
                              "[2] - NÃO \n"
                              "Digite: ")
        elif opcaor == '2':
            os.system('cls')
            break
        else:
            while True:
                print("Opção inválida! tente novamente.")
                opcaor = input("Deseja registrar outro produto? \n"
                              "[1] - SIM \n"
                              "[2] - NÃO \n"
                              "Digite: ")
                if opcaor == '1':
                    break
                elif opcaor == '2':
                    break

def listar():
    listaOrd = sorted(listaFinal, key=lambda nome: nome['nome'])
    res = '1'
    while True:
        os.system('cls')
        print("------------Listar produtos------------")
        if res == '1':
            for n in listaOrd:
                print(f"Nome: {n['nome']} \n"
                      f"Valor: {n['valor']:.2f} R$ \n"
                      f"Quantidade em stock: {n['quantidade']} \n"
                      f"Código do produto: {n['codigo']} \n"
                      "---------------------------------- \n")
            res = input("[1] - Listar novamente.\n"
                                "[2] - Voltar ao menu.\n"
                                "Digite: ")
        elif res == '2':
            os.system('cls')
            break
        else:
            while True:
                print("Opção inválida! tente novamente.")
                res = input("[1] - Listar novamente.\n"
                    "[2] - Voltar ao menu.\n"
                    "Digite: ")
                if res == '1':
                    break
                elif res == '2':
                    break

def pesquisar():
    res = '1'
    while True:
        if res == '1':
            os.system('cls')
            pesquisa = input("Digite o nome ou código do produto: ").upper()
            for n in listaFinal:
                if pesquisa in n['nome'].upper():
                    print("\nProduto encontrado! \n")
                    print("-------------------------------------")
                    print(f"Nome: {n['nome']} \n"
                          f"Valor: {n['valor']:.2f} R$ \n"
                          f"Quantidade em stock: {n['quantidade']}\n"
                          f"Código do produto: {n['codigo']}\n")
                    print("-------------------------------------\n")
                    
                elif pesquisa in n['codigo']:
                    print("\nProduto encontrado! ")
                    print("-------------------------------------")
                    print(f"Nome: {n['nome']} \n"
                          f"Valor: {n['valor']:.2f} R$ \n"
                          f"Quantidade em stock: {n['quantidade']}\n"
                          f"Código do produto: {n['codigo']}\n")
                    print("-------------------------------------\n")
            
            res = input("[1] - Pesquisar novamente.\n"
                            "[2] - Voltar ao menu.\n"
                            "Digite: ")
        elif res == '2':
            os.system('cls')
            break

        else:
            while True:
                print("Opção inválida! tente novamente.")
                res = input("[1] - Pesquisar Novamente.\n"
                    "[2] - Voltar ao menu.\n"
                    "Digite: ")
                if res == '1':
                    break
                elif res == '2':
                    break

def alterar():
    os.system('cls')
    op = '1'
    while True:
        if op == '1':
            resp = int(input("Você deseja alterar o preço ou a quantidade? \n"
                     "[1] - Preço \n"
                     "[2] - Quantidade \n"
                     "Digite: "))
            if resp == 1:
                pesquisa = input("Digite o nome ou código do produto: ").upper()
                for n in listaFinal:
                    if pesquisa in n['nome'].upper():
                        print("\nProduto encontrado! ")
                        print("---------------------------------------")
                        print(f"Nome: {n['nome']} \n"
                            f"Valor: {n['valor']:.2f} R$ \n"
                            f"Quantidade em stock: {n['quantidade']} \n"
                            f"Código do produto: {n['codigo']} \n")
                        print("---------------------------------------\n")
                        res = float(input("Digite o novo preço do produto: "))
                        n['valor'] = res
                        print("Preço alterado com sucesso! \n")
                    elif pesquisa in n['codigo']:
                        print("\nProduto encontrado! ")
                        print("---------------------------------------")
                        print(f"Nome: {n['nome']} \n"
                            f"Valor: {n['valor']:.2f} R$ \n"
                            f"Quantidade em stock: {n['quantidade']} \n"
                            f"Código do produto: {n['codigo']} \n")
                        print("---------------------------------------\n")
                        res = float(input("Digite o novo preço do produto: "))
                        n['valor'] = res
                        print("Preço alterado com sucesso! \n")
            elif resp == 2:
                pesquisa = input("Digite o nome ou código do produto: ").upper()
                for n in listaFinal:
                    if pesquisa in n['nome'].upper():
                        print("\nProduto encontrado! ")
                        print("---------------------------------------")
                        print(f"Nome: {n['nome']} \n"
                            f"Valor: {n['valor']:.2f} R$ \n"
                            f"Quantidade em stock: {n['quantidade']} \n"
                            f"Código do produto: {n['codigo']} \n")
                        print("---------------------------------------\n")
                        res = int(input("Você deseja aumentar ou diminuir a quantidade em stock? \n"
                            "[1] - Aumentar\n"
                            "[2] - Diminuir\n"))
                        if res == 1:
                            num = int(input("Digite a quantidade que vai ser adcionada: "))
                            n['quantidade'] += num
                            print("Quantidade aumentada com sucesso! \n")
    
                        elif res == 2:
                            num = int(input("Digite a quantidade que vai ser diminuida: "))
                            n['quantidade'] -= num
                            print("Quantidade diminuida com sucesso! \n")
                    elif pesquisa in n['codigo']:
                        print("\nProduto encontrado! ")
                        print("---------------------------------------")
                        print(f"Nome: {n['nome']} \n"
                            f"Valor: {n['valor']:.2f} R$ \n"
                            f"Quantidade em stock: {n['quantidade']} \n"
                            f"Código do produto: {n['codigo']} \n")
                        print("---------------------------------------\n")
                        res = int(input("Você deseja aumentar ou diminuir a quantidade em stock? \n"
                            "[1] - Aumentar\n"
                            "[2] - Diminuir\n"))
                        if res == 1:
                            num = int(input("Digite a quantidade que vai ser adcionada: "))
                            n['quantidade'] += num
                            print("Quantidade aumentada com sucesso! \n")

                        elif res == 2:
                            num = int(input("Digite a quantidade que vai ser diminuida: "))
                            n['quantidade'] -= num
                            print("Quantidade diminuida com sucesso! \n")

            else:
                print("Opção inválida! \n")

            op = input("[1] - Alterar produto.\n"
                    "[2] - Voltar ao menu.\n"
                    "Digite: ")
        elif op == '2':
            os.system('cls')
            break
        else:
            while True:
                print("Opção inválida! tente novamente.")
                op = input("[1] - Alterar produto.\n"
                    "[2] - Voltar ao menu.\n"
                    "Digite: ")
                if op == '1':
                    break
                elif op == '2':
                    break

def remover():
    os.system('cls')
    op = '1'
    while True:
        if op == '1':
            pesquisa = input("Digite o nome ou código do produto: ").upper()
            for n in listaFinal:
                if pesquisa in n['nome'].upper():
                    print("\nProduto encontrado! ")
                    print("---------------------------------------")
                    print(f"Nome: {n['nome']} \n"
                        f"Valor: {n['valor']:.2f} R$ \n"
                        f"Quantidade em stock: {n['quantidade']} \n"
                        f"Código do produto: {n['codigo']} \n")
                    print("---------------------------------------\n")
                    print()
                    res = input("Tem certeza que deseja excluir o item acima? \n"
                            "[1] - Sim \n"
                            "[2] - Não \n"
                            "Digite: " )
                    if res == '1':
                        listaFinal.remove(n)
                        print("Produto removido com sucesso! ")
                    elif res == '2':
                        print("Produto não foi removido! ")
                    else:
                        print("Opção Inválida! O produto não foi removido")
                elif pesquisa in n['codigo']:
                    print("\nProduto encontrado! ")
                    print("---------------------------------------")
                    print(f"Nome: {n['nome']} \n"
                        f"Valor: {n['valor']:.2f} R$ \n"
                        f"Quantidade em stock: {n['quantidade']} \n"
                        f"Código do produto: {n['codigo']} \n")
                    print("---------------------------------------\n")
                    print()
                    res = input("Tem certeza que deseja excluir o item acima? \n"
                            "[1] - Sim \n"
                            "[2] - Não \n"
                            "Digite: ")
                    if res == '1':
                        listaFinal.remove(n)
                        print("Produto excluído com sucesso! ")
                    elif res == '2':
                        print("Produto não foi removido! ")
                    else:
                        print("Opção Inválida! O produto não foi removido")

            op = input("[1] - Remover produto.\n"
                        "[2] - Voltar ao menu.\n"
                        "Digite: ")
        elif op == '2':
            os.system('cls')
            break
        
        else:
            while True:
                print("Opção inválida! tente novamente.")
                op = input("[1] - Remover produto.\n"
                    "[2] - Voltar ao menu.\n"
                    "Digite: ")
                if op == '1':
                    break
                elif op == '2':
                    break

while True:
    menu()
    opcao = input("Digite: ")
    if opcao == '1':
        registrar()
    elif opcao == '2':
        listar()
    elif opcao == '3':
        pesquisar()
    elif opcao == '4':
        alterar()
    elif opcao == '5':
        remover()
    elif opcao == '6':
        break
    else:
        print("Opção digitada inválida! Por favor, tente novamente!")

print("FIM")