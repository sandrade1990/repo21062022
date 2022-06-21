miDiccionario={"alemania":"Berlin","Francia":"paris","Inglaterra":"Londres"}

print(miDiccionario["Francia"])

miDiccionario["Italia"]="Lisboa" #de esta forma puedo agregar un nuevo pais, pero es erroneo.

print(miDiccionario["Italia"])

miDiccionario["Italia"]="Roma" #para corregir simplemente volvemos a escribir el valor correcto.

print(miDiccionario["Italia"]) # Dentro de un diccionario no hay dos claves iguales.

del miDiccionario["Inglaterra"]

print(miDiccionario)

miTupla=["España","Argentina", "Brasil","Alemania"]

miDiccionario={miTupla[0]:"Madrid"}

print(miDiccionario.keys())
print(miDiccionario.values())

if "Argentina" in miDiccionario: # funcion in para el condicional
    print ("Esta Ingresado")
else:
    print("No Ingresado")
