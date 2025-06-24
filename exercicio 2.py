carros = {
    'nomes': ['celta', 'up', 'kombi', 'uno'],
    'portas': [4, 2, 6, 2],
    'preço': [1000, 200, 300, 100],
    'ano de fabricação': [2014, 2018, 1970, 2005]
}

def mostrar_info(indice):
    print("\nInformações do carro:")
    print(f"Nome: {carros['nomes'][indice]}")
    print(f"Portas: {carros['portas'][indice]}")
    print(f"Preço: R${carros['preço'][indice]}")
    print(f"Ano de fabricação: {carros['ano de fabricação'][indice]}\n")

while True:
    print("\nO que você deseja fazer?")
    print("1 - Ver o carro mais potente")
    print("2 - Ver o carro menos potente")
    print("3 - Remover um carro")
    print("4 - Cadastrar um novo carro")
    print("5 - Sair")

    opcao = input("Digite o número da opção: ")

    if opcao == "1":
        indice = carros['preço'].index(max(carros['preço']))
        mostrar_info(indice)

    elif opcao == "2":
        indice = carros['preço'].index(min(carros['preço']))
        mostrar_info(indice)

    elif opcao == "3":
        nome = input("Digite o nome do carro que deseja remover: ").lower()
        if nome in carros['nomes']:
            idx = carros['nomes'].index(nome)
            for chave in carros:
                carros[chave].pop(idx)
            print(f"{nome} removido com sucesso!")
        else:
            print("Carro não encontrado.")

    elif opcao == "4":
        nome = input("Nome do carro: ").lower()
        portas = int(input("Número de portas: "))
        preco = int(input("Preço (número): "))
        ano = int(input("Ano de fabricação: "))

        carros['nomes'].append(nome)
        carros['portas'].append(portas)
        carros['preço'].append(preco)
        carros['ano de fabricação'].append(ano)

        print(f"{nome} cadastrado com sucesso!")

    elif opcao == "5":
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida. Tente novamente.")
