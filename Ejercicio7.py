#Leer x cantidad de edades y mostrar el promedio de dichas edades.

n = int(input("Digite total de alumnos: "))
x = 1
while x <= n:
    edad = int(input("Digite edad: "))
    suma = suma + edad
    x += 1
print("El promedio de las edades es: ", suma/n )
