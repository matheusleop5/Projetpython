def calcular_velocidade_media(distancia, tempo):
    #Código da nossa função
    velocidade_media = distancia / tempo
    #exibir o resultado
    print(f"A velocidade média é {velocidade_media}")


#Solicitar distância e tempo
dist_digitada = float(input("Digite a distância percorrida: "))
tempo_digitado = float(input("Digite o tempo gasto: "))
calcular_velocidade_media(dist_digitada, tempo_digitado)