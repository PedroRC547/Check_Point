vazamentos = []
while True:
    opcao=str(input("\n[1]Encontrar um vazamento específico?\n[2]Adcionar vazamento?\n[3]Sair\n\nR: "))

    if opcao == "1":
        busca=input("\nPalavra chave: ")
        procura=vazamentos.index(busca)
        print("\nE-Mail encontrado:\n\nE-Mail:",vazamentos[procura])

    elif opcao == "2":
        resposta = "S"
        while resposta == "S":
            email=input("\nE-Mail: ")
            confirmacao=input("\nDeseja confirmar os dados? ").upper()
            if confirmacao == "S":
                vazamentos.append(email)
                resposta=input("\nAdcionar mais um vazamento: ").upper()
                if resposta == "S":
                    continue
                elif resposta == "N":
                    break
                else:
                    print("Esse comando é inválido")
                    resposta=input("\nDeseja adcionar mais um vazamento: ")
            elif confirmacao == "N":
                print("\nOs dados não foram adicionados ao Banco de Dados.")
                resposta=input("\nAdicionar mais um vazamento: ").upper()
            else:
                print("Os dados não foram adicionados ao Banco de Dados.")
                resposta=input("\nAdicionar mais um vazamento: ").upper()
    elif opcao == "3":
        print("Fim.")
        break
    else:
        print("Erro.")
        continue

