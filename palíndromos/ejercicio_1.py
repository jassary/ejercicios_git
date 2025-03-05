#Pide al usuario una palabra y verifica si es un políndromo (se lee igual al derecho y al reves)

palabra= input('ingrese la palabra: ')
palabra_invertida= palabra[:: -1]
palabra_invertida.lower()

if palabra == palabra_invertida:
    print('la palabra es políndromo')
else:
    print('la palabra no es polídromo')