texto = "Este texto quebra de linha aqui.\nPorém aqui temos uma \ttabulação."
print(texto)

texto = "texto em minusculas AINDA É texto"
print(texto.capitalize()) #Para deixar o texto correto

print(texto.upper()) #Para deixar tudo maiúsculo
print(texto.lower()) #Para deixar tudo minusculo
print(texto.startswith("Tex")) #Para verificar se o começo da variável é igual
print(texto.endswith("o")) #Para verificar se a letra escolhida termina com a selecionada
print(texto.count("@")) #Para verificar quantas vezes a letra ou símbulo aparece na variável
print(texto.replace("AINDA", "com certeza")) #Trocando as palavras da variável