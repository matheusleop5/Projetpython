print("Cadastro de doadores de sangue")
nome = input("Por favor, digite o seu nome: ")
peso = float(input("Por favor, digite o seu peso Kg: "))
altura = float(input("Por favor, digite a sua altura em cm: "))
idade = int(input("Por favor, digite sua idade: "))

peso_min = peso > 50
idade_min = idade >= 16

texto_saida = f"\tNOME: {nome}\n\tPESO: {peso}Kg\n\tALTURA: {altura}cm\n\tIDADE: {idade}\n\tTEM PESO MINIMO PARA DOAR: {peso_min}\n\tTEM IDADE MINIMA PARA DOAR: {idade_min}"
print(texto_saida)