#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio = float(input('ingrese el precio: '))
euros = int(precio)
centimos = (precio - euros)*100 // 10
print(f'tienes {euros} euros y {centimos} centimos')
