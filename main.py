print("\n\tBem vindo ao menu da companhia aerea!")

voos = {}
clientes = {}
voosDisponiveis = []
menu = 0

while menu != 7:
    print("="*50)
    print("\n\tSelecione uma opção:")
    print("\n\t1. Cadastrar voo")
    print("\n\t2. Consultar voo")
    print("\n\t3. Informar voos com as menores escalas")
    print("\n\t4. Listar passageiros de um voo")
    print("\n\t5. Vendas de passagens")
    print("\n\t6. Cancelamento de passagens")
    print("\n\t7. Sair")
    print("="*50)
    menu = int(input("\n\t> "))

    if menu == 1:
        print("\n\tCadastrar voo")
        print("="*50)

        codigo_voo = str(input("\n\tDigite o código do voo: "))

        while codigo_voo in voos:
            print("="*50)
            print("\n\tEsse código já foi cadastrado! Digite outro código.")
            print("="*50)
            codigo_voo = str(input("\n\tCódigo do voo: "))

        while not (codigo_voo.isdigit()):
            print("="*50)
            print("\n\tEsse Código é inválido! Digite outro código.")
            print("="*50)
            codigo_voo = str(input("\n\tCódigo do voo: "))

        voos[codigo_voo] = {
            "origem": input("\n\tDigite a origem do voo: "),
            "destino": input("\n\tDigite o destino do voo: "),
            "data": input("\n\tDigite a data do voo (dd/mm/aaaa): "),
            "escala": int(input("\n\tDigite o número de escalas: ")),
            "preco": float(input("\n\tDigite o preço da passagem: ")),
            "quantidade_lugares_disponiveis": int(input("\n\tDigite a quantidade de lugares disponíveis: ")),
            "passageiros": []
        }

        if voos[codigo_voo]["quantidade_lugares_disponiveis"] != 0:
            voosDisponiveis.append(codigo_voo)

        print("="*50)
        print("\n\tVoo cadastrado com sucesso!")

    elif menu == 2:
        if len(voos) == 0:
            print("\n\tNão há voos cadastrados!")

        else:
            print("\n\tConsultar voo")
            print("="*50)
            print("\n\tDigite sua opção:")
            print("\n\t1.Consultar pelo codigo do voo")
            print("\n\t2.Consultar pela origem do voo")
            print("\n\t3.Consultar pelo destino do voo")
            opcao = int(input("\n\t: "))

            if opcao == 1:
                codigo_voo = str(input("\n\tDigite o código do voo: "))

                if codigo_voo in voos:
                    consultarVoo = voos[codigo_voo]
                    print("="*50)
                    print(f"\n\tCódigo do voo: {codigo_voo}")
                    print(f"\n\tOrigem do voo: {consultarVoo['origem']}")
                    print(f"\n\tDestino do voo: {consultarVoo['destino']}")
                    print(f"\n\tData do voo: {consultarVoo['data']}")
                    print(f"\n\tNúmero de escalas: {consultarVoo['escala']}")
                    print(f"\n\tPreço da passagem: R${consultarVoo['preco']}")
                    print(f"\n\tQuantidade de lugares disponiveis: {consultarVoo['quantidade_lugares_disponiveis']}")
                    print("="*50)

                else:
                    print("="*50)
                    print("\n\tEsse voo não existe!")
                    print("="*50)

            elif opcao == 2:
                origem = input("\n\tDigite a origem do voo: ")
                encontrou = False
                for codigo_voo, consultarVoo in voos.items():
                    if origem.lower() in consultarVoo["origem"].lower():
                        print("="*50)
                        print(f"\n\tCódigo do voo: {codigo_voo}")
                        print(f"\n\tDestino do voo: {consultarVoo['destino']}")
                        print(f"\n\tPreço da passagem: {consultarVoo['preco']}")
                        encontrou = True

                if not encontrou:
                    print("="*50)
                    print("\n\tNenhum voo encontrado com essa origem!")
                    print("="*50)

            elif opcao == 3:
                destino = input("\n\tDigite o destino do voo: ")
                encontrou = False

                for codigo_voo, consultarVoo in voos.items():
                    if consultarVoo["destino"].lower() == destino.lower():
                        print("="*50)
                        print(f"\n\tCódigo do voo: {codigo_voo}")
                        print(f"\n\tOrigem do voo: {consultarVoo['origem']}")
                        print(f"\n\tPreço da passagem: {consultarVoo['preco']}")
                        encontrou = True

                if not encontrou:
                        print("="*50)
                        print("\n\tNenhum voo encontrado com esse destino!")
                        print("="*50)

            else:
                print("="*50)
                print("\n\tOpção inválida!")
                print("="*50)

    elif menu == 3:
        print("=" * 50)
        print("Informar voos com as menores escalas")

        if len(voos) == 0:
            print("\n\tNenhum voo cadastrado!")

        else: 
            origem = input("\n\tInforme a cidade origem da viagem: ")
            destino = input("\n\tInforme a cidade destino: ")
            menor_escala = None

            for consultarVoo in voos.values():
                if consultarVoo["origem"].lower() == origem.lower() and consultarVoo["destino"].lower() == destino.lower():
                    if menor_escala == None or consultarVoo["escala"] < menor_escala:
                        menor_escala = consultarVoo["escala"]

            if menor_escala is None:
                print("=" * 50)
                print("\n\tNenhum voo encontrado com essa origem e destino!")
                print("=" * 50)

            else:
                for codigo_voo, consultarVoo in voos.items():
                    if consultarVoo["origem"].lower() == origem.lower() and consultarVoo["destino"].lower() == destino.lower() and consultarVoo["escala"] == menor_escala:

                        print("=" * 50)
                        print(f"\n\tCódigo do voo: {codigo_voo}")
                        print(f"\n\tOrigem do voo: {consultarVoo['origem']}")
                        print(f"\n\tDestino do voo: {consultarVoo['destino']}")
                        print(f"\n\tNúmero de escalas: {consultarVoo['escala']}")
                        print("=" * 50)
  
    elif menu == 4:
        print("\n\tListar passageiros de um voo")
        print("="*50)

        if len(voos) == 0:
            print("\n\tNão há voos cadastrados!")

        else:
            codigo_voo = str(input("\n\tDigite o código do voo: "))

            if codigo_voo in voos:
                if len(voos[codigo_voo]["passageiros"]) == 0:
                    print("="*50)
                    print("\n\tNão há passageiros cadastrados nesse voo!")
                    print("="*50)

                else:
                    print(f"\n\tPassageiros do voo {codigo_voo}:")
                    print("="*50)

                    for cpf_passageiro in voos[codigo_voo]["passageiros"]:
                        passageiro = clientes[cpf_passageiro]
                        print(f"\n\tNome: {passageiro['nome']}")
                        print(f"\n\tCPF: {cpf_passageiro}")
                        print(f"\n\tTelefone: {passageiro['telefone']}")
                        print("="*50)

                    print("\n\tVagas restantes:", voos[codigo_voo]["quantidade_lugares_disponiveis"])
                    print("="*50)

            else:
                print("="*50)
                print("\n\tEsse voo não existe!")
                print("="*50)
                
    
    elif menu == 5:
        print("\n\tVendas de passagens")
        print("="*50)

        if len(voos) == 0:
            print("\n\tNão há voos cadastrados!")
        else:
            codigo_voo = input("\n\tDigite o código do voo: ")

            if codigo_voo not in voos:
                print("="*50)
                print("\n\tEsse voo não existe!")
                print("="*50)
            elif codigo_voo not in voosDisponiveis:
                print("="*50)
                print("\n\tNão há mais passagens disponíveis para esse voo!")
                print("="*50)
            else:
                cpf_passageiro = input("\n\tDigite o CPF do passageiro: ")

                if cpf_passageiro in voos[codigo_voo]["passageiros"]:
                    print("="*50)
                    print("\n\tEsse CPF já está cadastrado nesse voo!")
                    print("="*50)

                else:
                    if cpf_passageiro not in clientes:
                        print("\n\tEsse passageiro ainda não foi cadastrado")
                        nome_passageiro = input("\n\tDigite o nome do passageiro: ")
                        telefone_passageiro = input("\n\tDigite o telefone do passageiro: ")
                        clientes[cpf_passageiro] = {"nome": nome_passageiro,"telefone": telefone_passageiro}

                    voos[codigo_voo]["passageiros"].append(cpf_passageiro)
                    voos[codigo_voo]["quantidade_lugares_disponiveis"] -= 1

                    if voos[codigo_voo]["quantidade_lugares_disponiveis"] == 0:
                        voosDisponiveis.remove(codigo_voo)

                    print("="*50)
                    print("\n\tPassagem vendida com sucesso!")
                    print("="*50)

    elif menu == 6:
        print("\n\tCancelamento de passagens")
        print("="*50)

        if len(voos) == 0:
            print("\n\tNão há voos cadastrados!")
        else:
            codigo_voo = input("\n\tDigite o código do voo: ")

            if codigo_voo not in voos:
                print("="*50)
                print("\n\tEsse voo não existe!")
                print("="*50)
            else:
                cpf_passageiro = input("\n\tDigite o CPF do passageiro: ")

                if cpf_passageiro not in voos[codigo_voo]["passageiros"]:
                    print("="*50)
                    print("\n\tNão há passageiro cadastrado com esse CPF nesse voo!")
                    print("="*50)
                else:
                    voos[codigo_voo]["passageiros"].remove(cpf_passageiro)
                    voos[codigo_voo]["quantidade_lugares_disponIveis"] += 1

                    if codigo_voo not in voosDisponiveis:
                        voosDisponiveis.append(codigo_voo)

                print("="*50)
                print("\n\tPassagem cancelada com sucesso!")
                print("="*50)

    elif menu == 7:
        print("\n\tObrigado por usar o sistema da companhia aérea!\n")
   
    else:
        print("="*50)
        print("\n\tOpção inválida! Por favor, selecione uma opção válida.")
        print("="*50)
