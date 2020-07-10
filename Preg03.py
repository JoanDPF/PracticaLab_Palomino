#Richard Licirio victorio Tito - Estudiante 03


frase = input("Ingresa los datos :")
cant=0
datos=frase.split()
for nombre in datos:
    cant=len(nombre)+cant

print("Cantidad de letras")
print(cant)
