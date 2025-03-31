print("Lojas Bras")

total_compra = float(input("Informe o valor total da compra: "))
forma_pagamento = int(input("Selecione a forma de pagamento: 1 - boleto ou 2 - cartão: "))

if forma_pagamento == 1:
    desconto = total_compra * 5 / 100
    total_compra = total_compra - desconto
    print(f"O desconto foi de R${desconto:.2f}, e o valor total com desconto ficou em R${total_compra:.2f}")

else :
    parcelas = int(input("Selecione a quantidade de parcelas até 12x:"))
    total_parcelas = total_compra / parcelas
    print(f"O valor a ser cobrado pelas parcelas é de R${total_parcelas:.2f}")