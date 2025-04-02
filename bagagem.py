print("Companhia aérea")
tipo_cliente = int(input("Selecione o tipo de cliente sendo:\n\t1 - Premium\n\t2 - Gold\n\t3 - Regular\n\t->"))
peso_bagagem = float(input("Informe o peso da bagagem do cliente (em Kg): "))

if tipo_cliente == 1:
    if peso_bagagem > 32:
        peso_excedente = peso_bagagem - 32
        print(f"O cliente deve pagar taxa adicional pelo peso de {peso_excedente:.2f}!")
    else:
        print("O peso da bagagem se enquadra no plano do cliente, por tanto o despacho da bagagem é gratuita!")
else:
    if tipo_cliente == 2:
        if peso_bagagem > 28:
            peso_excedente = peso_bagagem - 28
            print(f"O cliente deve pagar taxa adicional pelo peso de {peso_excedente:.2f}!")
        else:
            print("O peso da bagagem se enquadra no plano do cliente, por tanto o despacho da bagagem é gratuita!")
    else:
        print("O cliente deve pagar taxa pelo peso da bagagem!")