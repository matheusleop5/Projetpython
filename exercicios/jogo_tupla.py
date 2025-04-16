inimigos = [(50, 30), (100, 100), (10, 90), (30, 25)]

#for inimigo in inimigos:
    #print(inimigo)
    #for coordenada in inimigo:
        #print(coordenada)
for x, y in inimigos:
    print(f"A posição é X={x} e y={y}")

x = int(input("Digite a coordenada X: "))
y = int(input("Digite a coordenada Y: "))

if (x, y) in inimigos:
    inimigos.remove((x, y))
    print("Você matou um inimigo!")
else:
    print("Você errou!")