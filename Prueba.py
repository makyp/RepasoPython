'''
Primer ejercicio
numeroa=float(input("Ingrese el valor de a:"))
numerob=float(input("Ingrese el valor de b:"))
numeroc=float(input("Ingrese el valor de c:"))

operacion = (numeroa**3 * (numerob**2 - 2*numeroa*numeroc))/(2*numerob)
print(f"El resultado de la operación es: {operacion}")

'''
'''
Ejercicio 2: calcular la nota final
parcial1=float(input("Ingrese la calificación del parcial 1: "))
parcial2=float(input("Ingrese la calificación del parcial 2: "))
parcial3=float(input("Ingrese la calificación del parcial 3: "))
parcial4=float(input("Ingrese la calificación del parcial 4: "))
proyectofinal=float(input("Ingrese la calificación del proyecto final: "))
trabajos=float(input("Ingrese la calificación final de trabajos: "))

calificaciónfinal= ((parcial1+parcial2+parcial3+parcial4)/4)*0.55+proyectofinal*0.3+trabajos*0.15
print(f"La calificación final es: {calificaciónfinal}")

Ejercicio 3: Numero de discos para la copia de seguridad
CapacidadCopia = float(input("Cual es tamaño de la copia de seguridad en Gigabytes: "))
capacidad=700
capacidadDisco = CapacidadCopia*1024
Discos= (capacidadDisco/capacidad)
print(f"Necesita un total de {Discos} para una copia de {CapacidadCopia} Gigabytes")

Ejercicio 4:

altura= float(input("Ingrese su estatura en metros"))
alturacm= altura*100
if alturacm<=150:
    print("Persona de Altura baja")
elif 151>=alturacm<=170:
    print("Persona de altura media")
elif alturacm==171 or alturacm<=190:
    print("Persona alta")
elif alturacm==191 or alturacm<=230:
    print("Persona Muy Alta")
else:
    print("Persona Demasiado Alta")
    
Ejercicio 5: Hacer un programa que pida 3 numeros y determine cual es el mayor
'''
a=float(input("Ingrese el primer valor "))
b=float(input("Ingrese el segundo valor "))
c=float(input("Ingrese el tercer valor "))

if a>=b and a>=c:
    print(f"El numero mayor es {a}")
elif b>=a and b>=c:
    print(f"El numero mayor es {b}")
else:
    print(f"El numero mayor es {c}")



