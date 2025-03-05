#CLASIFICACION DE FRASES AL USUARIO SEGUN SU LONGITUD

#Solicita al usuario una frase y clasificala por longitud, si es corta, mediana o larga

frase= input('ingrese la frase: ')
longitud= len(frase)

  
if longitud < 20:
        print("La frase es corta.")
elif 20 <= longitud <= 50:
        print("La frase es mediana.")
else:
        print("La frase es larga.")