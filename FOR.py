'''for contador in range(100):
    if(contador %3 == 0):
        print(contador)'''

'''ultima = 1
penul = 1
for susecion in range(2,100,1):
    suma = ultima + penul
    print(suma)
    penul = ultima
    ultima = suma '''

intentos = 5
secret = 2
import random
numero1 = int(input('Seleccione un numero entre el 1 al 10'))
while intentos > 0:
    if numero1 == secret:
        print('Adivinaste el numero pa')
        break
    else:
        numero1=int(input('Ingrese de nuevo'))
    intentos -= 1
    print(intentos)
