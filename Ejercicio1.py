"""Mostrar el total a pagar por la compra de n cantidad de productos a un precio
desconocido."""

print("Ingrese Cantidad de productos a pagar  ")
producto = int(input())
i = 0
total = 0
while i<producto:
    print("Precio del producto: " ,i+1)
    pre= int(input())
    print("cantidad")
    cantidad = int(input())
    subpro=pre*cantidad
    total=total+subpro
    i+=1
total = total 
print("Se vendieron: ", producto, "Productos ")
print("Total: ",total)



