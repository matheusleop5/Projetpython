print("Restaurante bauru")

preco_quilo = float(input("Informe o valor cobrado pelo quilo: "))
peso_prato = float(input("Informe o peso do prato (em kg): "))
peso_comida = float(input("Informe o peso do prato do cliente (em Kg): "))

peso_real = peso_comida - peso_prato
preco_final = peso_real * preco_quilo

print(f"O valor do prato é R${preco_final:.2f}")

if peso_real > 1:
    print("Como o valor da refeição do cliente ultrapassou 1Kg, ele deve pagar apenas o valor fixo de R$80,00")