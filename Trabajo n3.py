'''
x = 5
x+= 2 # Es lo mismo que x = x+2
print (x)

numero = 5
if numero < 0: # el if funciona si la condicion es verdadera
    print ("Condicional verdadera")
else:
    print ("Come trabas, pero hermosos")

humedad = 85
if humedad > 80:
    print ("esta lloviendo")
elif  30 < humedad < 80:
    print ("esta nublado")
else:
    print ("esta soleado")
'''
'''
Actividad 1
nombre = input("Ingrese su nombre: ")
años = int(input("Ingrese los años de servicio: "))
if (5 >= años):
    print (f"{nombre}  tiene un bono de $5.000")
elif (5 < años < 20):
    print (f"{nombre}  tiene un bono de $10.000")
elif (20 < años):
    print (f"{nombre}  tiene un bono de $15.000")
'''
'''
Actividad 2
producto = "chocolate"
precio = 325
cantidad = int(input('Seleccione la cantidad de chocolates: '))
precio_final = precio * cantidad
descuento = int (precio_final * 0.10)
descuento_2 = int(precio_final * 0.17)
descuento_3 = int(precio_final * 0.20)
if 9 >= cantidad:
    print ('la cantidad a pagar es de: ' , int ( precio_final -descuento))
elif 19 >= cantidad:
    print('la cantidad a pagar es de:' , int (precio_final - descuento_2))
elif 20 <= cantidad:  
    print('la cantidad a pagar es de:' , int(precio_final - descuento_3))
'''
'''
Actividad 3
letra = input('ingrese una letra') # letra = int(input('ingrese una letra'))----> de esta manera esta mal ejecutado el codigo
if letra in ['a', 'e', 'i', 'o', 'u']:
    print('la letra es una vocal')
else:
    print('es una consonate')
'''
'''
Actividad 4
dia_semana = int(input('selecciones un numero del 1 al 7'))
if dia_semana == 1:
    print('Lunes')
elif dia_semana == 2:
    print('Martes')
elif dia_semana == 3:
    print('Miercoles')
elif dia_semana == 4:
    print('Jueves')
elif dia_semana == 5:
    print('Viernes')
elif dia_semana == 6:
    print('Sabado')
elif dia_semana == 7:
    print('Domingo')
else:
    print('tienes que selccionar un numero del 1 al 7')
'''
'''
precio = int(input('ingrese el precio del producto'))
cantidad = int(input('indeque la cantidad de productos que desea llevar'))
precio_final = cantidad * precio
if 20 < cantidad :
    print('la cantidad a pagar es de:' , int(precio_final * 0.97))
elif cantidad > 10:
    print('la cantidad a pagar es de:' , int(precio_final * 0.95))
elif cantidad > 5:
    print('la cantidad a pagar es de:' , int(precio_final * 0.90))
else:
    print('no hay descuentos para esta cantidad deseada')
'''
print("Bienvenido al juego de la adivinansa, te tocara elegir un numeor que escogi entre el uno y el diez")
numero = int(input('Eliga un numero entre el 1 y el 10'))
numero_2 = 7
if numero == numero_2:
    print('Felicidades adivinaste el numero')
elif numero < numero_2:
    print('el numero es mas grande')
elif numero > numero_2:
    print('el numero es mas pequeño')



