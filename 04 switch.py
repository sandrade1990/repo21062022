#swith case, no existe en python debido a la simplicidad del sistema de programacion.

salarioPresidente=int(input("Introduce Salario del Presidente:"))
print("salario presidente:"+ str(salarioPresidente)) #Python no puede concatenar diferentes variables

salarioDirector=int(input("Introduce Salario del Director:"))
print("salario Director:"+ str(salarioDirector)) #Python no puede concatenar diferentes variables

salarioGerente=int(input("Introduce Salario del Gerente:"))
print("salario Gerente:"+ str(salarioGerente)) #Python no puede concatenar diferentes variables

salarioSupervisor=int(input("Introduce Salario del Supervisor:"))
print("salario Supervisor:"+ str(salarioSupervisor)) #Python no puede concatenar diferentes variables

salarioAnalista=int(input("Introduce Salario del Analista:"))
print("salario Analista:"+ str(salarioAnalista)) #Python no puede concatenar diferentes variables

if salarioAnalista<salarioSupervisor<salarioGerente<salarioDirector<salarioPresidente:
    print("Todo funciona correctamente")
else:
    print("Algo Falla")

if salarioAnalista<1000 and salarioSupervisor< 5000 and salarioGerente< 15000 and salarioDirector< 60000 and salarioPresidente<100000:
    print("Todo funciona correctamente")
else:
    print("Algo Falla")

opcion=input("Escribe la asignatura:")

asignatura =opcion.lower() # transforma todo lo que ingreso a minusculas

print (asignatura)