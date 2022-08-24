#Dado el primer nombre, segundo nombre, primer apellido y el segundo apellido de un
#estudiante de manera individual, escriba un código en Python que permita crear un correo
#electrónico utilizando la siguiente sintaxis: primer nombre + punto (.) + primer apellido +
#“@est.uca.edu.ni”



from re import L


print("Ingrese su primer nombre: ")
nombre1 = (input())
print("Ingrese su segundo nombre: ")
nombre2 = (input())
print("Ingrese su primer apellido: ")
ape1 = (input())
print("Ingrese su segundo apellido: ")
ape2 = (input())
inicio=nombre1+(".")
usuario=inicio+ape1
usuario=usuario
print("Su usuario es: ", usuario, ("@est.uca.edu,ni"))







 