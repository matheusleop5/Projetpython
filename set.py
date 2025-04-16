#criando um set vazio
conjunto = set()
print(type(conjunto))
#criando um set a partir de uma lista
lista = ["Andre", "David", "Cebolinha", "Andre"]
print(lista)
conjunto2 = set(lista)
print(conjunto2)
#criando um set com valores
conjunto3 = {"Cebolinha", "Magali", "Monica", "Cascao", "Cebolinha"}
print(conjunto3)
#selecionando um elemento(add)
conjunto3.add("Franjinha")
print(conjunto3)
#removendo elemento que estão em outro set (diference_update)
conjunto1 = {"Mega Drive", "Super nintendo", "Playstation"}
conjunto2 = {"Playstation", "Nintendo 64", "Sega saturn", "Dreancast"}

print(f"O primeiro set contém {conjunto1}")
print(f"O segundo set contém {conjunto2}")
conjunto1.difference_update(conjunto2)
print(f"O primeiro set contém {conjunto1}")
#remover um elemento especifico do set (remove)
conjunto1 = {"Mega Drive", "Super nintendo", "Playstation"}
print(conjunto1)
conjunto1.remove("Mega Drive")
print(conjunto1)
#remover um elemento especifico do set (discard)
conjunto1.discard("Playstation")
print(conjunto1)
conjunto1.discard("Playstation")
print(conjunto1)
