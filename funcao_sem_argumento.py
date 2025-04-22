def calcular_velocidade_media():
    #Código da nossa função
    velocidade_media = distancia / tempo
    #exibir o resultado
    print(f"A velocidade média é {velocidade_media}")


#Solicitar distância e tempo
distancia = float(input("Digite a distância percorrida: "))
tempo = float(input("Digite o tempo gasto: "))
calcular_velocidade_media()