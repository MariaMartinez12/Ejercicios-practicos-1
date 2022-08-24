#Leer dos números y decir cual es mayor y cual es menor.

a = int(input("ingrese un numero "))
b = int(input("ingrese un numero "))
c = int(input("ingrese un numero "))
if a < b:
  print ("el el mayor es ",a)
else  #aca marca error
  print ("el mayor es ",b)
else print ("el mayor es ",c)
elif a > b:
  print ("el valor menor es ",a)
else print("el valor menor es ",b)
else print("el valor menor es ",c)
input()