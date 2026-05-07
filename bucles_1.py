#Escribe un programa que reciba una cadena de texto y cuente cuántas vocales contiene.Debe retornar el número total de vocales. Las vocales pueden ser mayúsculas o minúsculas.
'''
texto= input('ingrese un texto: ')
vocales = 0
for i in texto:
    if i in 'aeiouAEIOU':
        vocales += 1
print(f'las vocales son: {vocales}')'''




#Escribe un programa que encuentre el número más grande en una lista de números.Debe retornar el `'El numero mas grande es {numero}'`
'''
numero = [1,2,3,4,5,6,7,8,9,0]
numero1 = max(numero)
print(f'el numero mas grande es {numero1}')'''


#encontrar los números primos en un rango del 1 al n, **incluyendo n**.Debe retornar una lista con los números primos encontrados.


#Encontrar los números primos en un rango del 1 al n, **incluyendo n**.Debe retornar una lista con los números primos encontrados.

numeros_primos = [1,3,4,5,7,11,13,15,17,19]
n= int(input('ingrese un numero primo: '))
if n in numeros_primos:
    print('es un numero primo')
else:
    print('no es un numero primo')


'''
texto = input('ingrese una palabra que sea un palindromo: ')
print(texto[::-1])
if texto == (texto[::-1]):
    print('bien es un palindromo')
else:
    print('no es un palindromo')'''


#7. Dada una lista de nombres, crear una funcion que devuelva una lista con los nombres que empiezan con la letra recibida como parámetro.

'''lista_nombres = ['santi','pedro','juan','maria','ana']
letra = input('ingrese una letra: ')
for i in lista_nombres:
    if i[0] == letra:
        print(i)'''
    

'''tuplas = {1,2,3,4,5,6,7,}
tuplas (1,2,5)
print(f'las tuplas son: {tuplas}')'''
