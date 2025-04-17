#Dados
#Criação do dicionario
dicionario = {
    "nome":"Star Wars - Episódio IV - uma nova esperança",
    "diretor":"George Lucas",
    "ano de lançamento":1977,
    "bilheteria": 775000000.00
}

#Exibindo o dicionario completo
print(dicionario)

#Exibindo o valor de uma chave
print(dicionario["nome"])

#Inserção de uma nova chave e valor (gênero)
dicionario["gênero"] = "Space Opera"
print(dicionario)

#Metodo Keys
print(dicionario.keys())
for chave in dicionario.keys():
    print(chave)

#Metodo values
print(dicionario.values())
for valor in dicionario.values():
    print(valor)

#Metodo items
print(dicionario.items())
for chave, valor in dicionario.items():
    print(f"{chave} -- {valor}")

#Metodo get
print(dicionario.get("público"))
print(dicionario.get("nome"))

#Metodo setdefault
dicionario.setdefault("público", 1000)
print(dicionario)
dicionario.setdefault("público", 9000)
print(dicionario)