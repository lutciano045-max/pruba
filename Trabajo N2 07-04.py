numero = int(input('ingrese un numero'))
if numero % 2 == 0:
    print('El numero es par')
else:
   print('El numero es impar')


A1 = int(input('ingrese primer valor'))
A2 = int(input('ingrese segundo valor'))
if A1 > A2:
    print(f'es el numero mayor {A1}')
elif A2 > A1:
    print(f'el numero mas grande es {A2}')
else:
    print('ambos numeros tienen el mismo valor')

Numero = int(input('seleccione un numero entre el cero y el 10'))

if Numero >=0 and Numero <10 :
    print('Este numero se encuentra entre estos numeros seleccionados')
else:
    print('Numero no seleccionado')
