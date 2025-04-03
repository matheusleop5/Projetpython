resposta = ""
tentativa = 0
while resposta != "ei":
    resposta = input("Digite a senha: ")
    tentativa = tentativa +1

print(f"\tSenha correta! Foi preciso usar {tentativa} tentativas para o acerto!")