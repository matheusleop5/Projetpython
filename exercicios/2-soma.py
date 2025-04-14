#Exercício 2: Soma de números digitados pelo usuário
# Objetivo: Pedir ao usuário que digite números até que ele insira 0. No final, mostrar a soma de todos os números digitados.

soma = 0
numero = int(input("acerte o numero escondido (0 a 10): "))

while numero != 0:
    soma += numero
    numero = int(input("Errou, digite outro: "))

print(f"Acertou! E a so1ma dos numeros digitados foi: {soma}")