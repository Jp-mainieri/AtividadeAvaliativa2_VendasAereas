print("\n\tBem vindo ao menu da companhia aerea!")

voos = {}
passageiros = {}
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
            "quantidade_lugares_disponiveis": int(input("\n\tDigite a quantidade de passageiros: ")),
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
                codigo = int(input("\n\tDigite o código do voo: "))
                if codigo in voos:
                    v = voos[codigo]
                    print("="*50)
                    print(f"\n\tCódigo do voo: {codigo}")
                    print(f"\n\tOrigem do voo: {v['origem']}")
                    print(f"\n\tDestino do voo: {v['destino']}")
                    print(f"\n\tPreço da passagem: R${v['preco']}")
                    print(f"\n\tQuantidade de lugares disponiveis: {v['quantidade_lugares_disponiveis']}")
                    print(f"\n\tData do voo: {v['data']}")
                    print(f"\n\tNúmero de escalas: {v['escala']}")
                    print("="*50)
                else:
                    print("="*50)
                    print("\n\tEsse voo não existe!")
                    print("="*50)
            elif opcao == 2:
                origem = input("\n\tDigite a origem do voo: ")
                encontrou = 0
                for codigo, dados in voos.items():
                    if dados["origem"].lower() == origem.lower():
                        print("="*50)
                        print(f"\n\tCódigo do voo: {codigo}")
                        print(f"\n\tDestino do voo: {dados['destino']}")
                        print(f"\n\tPreço da passagem: {dados['preco']}")
                        encontrou = 1
                if encontrou == 0:
                        print("="*50)
                        print("\n\tNenhum voo encontrado com essa origem!")
                        print("="*50)
            elif opcao == 3:
                destino = input("\n\tDigite o destino do voo: ")
                encontrou = 0
                for codigo, dados in voos.items():
                    if dados["destino"].lower() == destino.lower():
                        print("="*50)
                        print(f"\n\tCódigo do voo: {codigo}")
                        print(f"\n\tOrigem do voo: {dados['origem']}")
                        print(f"\n\tPreço da passagem: {dados['preco']}")
                        encontrou = 1
                if encontrou == 0:
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
            for dados in voos.values():
                if dados["origem"].lower() == origem.lower() and dados["destino"].lower() == destino.lower():
                    if menor_escala == None or dados["escala"] < menor_escala:
                        menor_escala = dados["escala"]
            if menor_escala is None:
                print("=" * 50)
                print("\n\tNenhum voo encontrado com essa origem e destino!")
                print("=" * 50)
            else:
                for codigo, dados in voos.items():
                    if dados["origem"].lower() == origem.lower() and dados["destino"].lower() == destino.lower() and dados["escala"] == menor_escala:

                        print("=" * 50)
                        print(f"\n\tCódigo do voo: {codigo}")
                        print(f"\n\tOrigem do voo: {dados['origem']}")
                        print(f"\n\tDestino do voo: {dados['destino']}")
                        print(f"\n\tNúmero de escalas: {dados['escala']}")
                        print("=" * 50)
    elif menu == 4:
        print("\n\tListar passageiros de um voo")
        print("="*50)
        if len(voos) == 0:
            print("\n\tNão há voos cadastrados!")
        else:
            codigo_voo = int(input("\n\tDigite o código do voo: "))
            if codigo_voo not in voos:
                print("="*50)
                print("\n\tEsse voo não existe!")
                print("="*50)
            else:
                if len(voos[codigo_voo]["passageiros"]) == 0:
                    print("="*50)
                    print("\n\tNão há passageiros cadastrados nesse voo!")
                    print("="*50)
                else:
                    print(f"\n\tPassageiros do voo {codigo_voo}:")
                    print("="*50)
                    for passageiro in voos[codigo_voo]["passageiros"]:
                        print(f"\n\tNome: {passageiro['nome']}")
                        print(f"\n\tCPF: {passageiro['cpf']}")
                        print(f"\n\tTelefone: {passageiro['telefone']}")
                        print("="*50)
                    print("\n\tVagas restantes:", voos[codigo_voo]["quantidade_lugares_disponiveis"])
                    print("="*50)
    elif menu == 5:
        print("\n\tVendas de passagens")
        print("="*50)
        if len(voos) == 0:
            print("\n\tNão há voos cadastrados!")
        else:
            codigo_voo = int(input("\n\tDigite o código do voo: "))
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
                ja_cadastrado = False
                if cpf_passageiro not in passageiros:
                    print("\tPassageiro não cadastrado")
                    nome_passageiro = input("\n\tDigite o nome do passageiro: ")
                    telefone_passageiro = input("\n\tDigite o telefone do passageiro: ")
                for passageiro in voos[codigo_voo]["passageiros"]:
                    if passageiro["cpf"] == cpf_passageiro:
                        ja_cadastrado = True
                        break
                if ja_cadastrado:
                    print("="*50)
                    print("\n\tEsse CPF já está cadastrado nesse voo!")
                    print("="*50)
                else:
                    passageiros[cpf_passageiro] = {
                        "nome": nome_passageiro,
                        "telefone": telefone_passageiro,
                        "voos": [codigo_voo]  # Lista de voos associados ao passageiro
                    }
                    voos[codigo_voo]["passageiros"].append()
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
            codigo_voo = int(input("\n\tDigite o código do voo: "))
            if codigo_voo not in voos:
                print("="*50)
                print("\n\tEsse voo não existe!")
                print("="*50)
            else:
                passageiro_cpf = input("\n\tDigite o CPF do passageiro: ")
                encontrado = False
                for passageiro in voos[codigo_voo]["passageiros"]:
                    if passageiro["cpf"] == passageiro_cpf:
                        voos[codigo_voo]["passageiros"].remove(passageiro)
                        voos[codigo_voo]["quantidade_passageiros"] += 1
                        print("="*50)
                        print("\n\tPassagem cancelada com sucesso!")
                        print("="*50)
                        encontrado = True
                        break
                if encontrado == False:
                    print("="*50)
                    print("\n\tNão há passageiro cadastrado com esse CPF nesse voo!")
                    print("="*50)
    elif menu == 7:
        print("\n\tObrigado por usar o sistema da companhia aérea!\n")
    else:
        print("="*50)
        print("\n\tOpção inválida! Por favor, selecione uma opção válida.")
        print("="*50)
