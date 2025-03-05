#DETECTOR DE DOMINIO DE CORREOS ELECTRONICOS

#pide al usuario un correo electronico y determina si pertenece a gmail, outlook o Yahoo

correo=input('ingrese un correo electrónico: ')

if correo.endswith("@gmail.com"):
    
    print("El correo pertenece a Gmail")
    
elif correo.endswith("@outlook.com"):
    
    print("El correo pertenece a Outlook")
    
elif correo.endswith("@yahoo.com"):
    
    print("El correo pertenece a Yahoo")
else:
    print("otro")

