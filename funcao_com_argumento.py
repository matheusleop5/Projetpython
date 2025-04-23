def calcular_velocidade_media(distancia:float, tempo:float, unidade_medida = "Km/h"):
    #Código da nossa função
    velocidade_media = distancia / tempo
    #exibir o resultado
    print(f"A velocidade média é {velocidade_media}{unidade_medida}")


calcular_velocidade_media(200, 3)