opcao = 0

while opcao != 3:
    print("1 - Receber um elogio ")
    print("2 - Calcular o fatorial ")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        print("Você é uma pessoal muito inteligente!")
    elif opcao == 2:
        numero = int(input("Por favor, digite o numero do qual deseja o fatorial: "))
        for valor in range(1, numero, 1):
            fat = fat * valor

        print(f"O fatorial deu: {fat}")
else:
    print("Escolha uma opção do menu:")