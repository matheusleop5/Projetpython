#importação
from collections import defaultdict
#criação de um default dict com uma lista como valor padrão
dicionario_lista = defaultdict(list)
dicionario_lista["PRODUTO"] = "Macbook Pro"
dicionario_lista["MARCA"] = "Apple"

print(dicionario_lista["PREÇO"])
print(dicionario_lista)

#Criação de função que retorna a frase "INEXISTENTE"
def funcao_exemplo():
    return "INEXISTENTE"
dicionario_funcao = defaultdict(funcao_exemplo)
dicionario_funcao["PRODUTO"] = "Macbook Pro"
dicionario_funcao["MARCA"] = "Apple"

print(dicionario_funcao)
print(dicionario_funcao["PRECO"])
print(dicionario_funcao)

#Criação de dicionário com uma função lambda
dicionario_lambda = defaultdict(lambda: "Não disponível")
dicionario_lambda["PRODUTO"] = "Macbook Pro"
dicionario_lambda["MARCA"] = "Apple"

print(dicionario_lambda)
print(dicionario_lambda["PRECO"])
print(dicionario_lambda)