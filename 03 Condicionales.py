print ("verificacion de Acceso")

edad_usuario= int(input("Introduce tu edad:"))

if edad_usuario<18:
    print("No puede pasar") #verifica la primera condicion
if edad_usuario<19:
    print("Verificar Permiso") #verifica la segunda condicion
elif edad_usuario>100:
    print("Edad Incorrecta") #verifica la edad elif funciona con toda la estructura del condicional 
else:
    print("puede pasar")# si nincuna cumple sucede esta operacion
print("el programa ha finalizado")