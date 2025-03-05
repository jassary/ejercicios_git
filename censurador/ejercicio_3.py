#CENSURADOR DE PALABRAS

#Pide al usuario una frase y remplaza una palabra por astericos

frase= input('ingrese la frase: ')
palabra_censurada = "mierda"   
frase_censurada = frase.replace(palabra_censurada, '*' * len(palabra_censurada))
print("Frase censurada:", frase_censurada)
