#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal en minúscula, y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.

frase = input('Ingrese una frase: ')
vocal = input('Ingrese una vocal en minuscula: ')
if vocal in ['a','e','i','o','u']:
    frase_modificada = frase.replace(vocal, vocal.upper())
    print(frase_modificada)
else:
    print('no ingresante una minuscula')

