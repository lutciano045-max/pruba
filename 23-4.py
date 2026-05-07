#la matriz se lee como fila columna, al editarla
# repasar diagramas de flujo
'''Crear una lista de paises y una lista de caracteristicas
el usuario debe adivinar un pais
le mostraremos la caracteristica y debe adivinar un pais
TENDREMOS QUE DARLE 5 INTENTOS A LOS USUARIOS
Y QUE LE DE UN PUNTAJE OBTENIDO POR PAIS ADIVINADO'''


lista_paises = ['ARGENTINA','CHILE','BRASIL','URUGUAY','PERU']
caract_pais = ['MATE','HABLAN PA EL CULO', 'LOS TRABAS ABUNDAN','CREEN QUE TIENEN 4','PALOMAS']

intentos = 5
puntaje = 0

print('Bienvenido al juego de los paises')
si_no = int(input('seleccione 1 para jugar, seleccione 2 para ser forro '))
if si_no == 2:
     print('Sos un forro')
elif si_no == 1:
    print('Bienvenido al juego')
    print(f'Tienes {intentos} intentos')
    print('Acontinuacion te mostrare las siguientes caracteristicas de los paises:')    
    for i in range(len(lista_paises)):
        intentos=5
        print(caract_pais)
        print('------------------------------')
        print(caract_pais[i])
        while intentos > 0:
            adivina1= input('Que pais crees que es: ').upper()
            if adivina1 == lista_paises[i]:
                print('Adivinaste papa')
                puntaje += 1
                print(f'haz obtenido {puntaje} punto')
                print('cantidad de puntos es:',puntaje )
                intentos=0
            else:
                intentos -= 1
                print('no adivinaste')
                print(f'te quedan {intentos} intentos')
        if puntaje == 5:
            print('GANASTE PAPA 10/10')
            break
        if puntaje == 0:
            print('SOS RE PETERO JAJAJAJAJ')
            break
               






        

    



       
    





'''from tkinter import mainloop
import tkinter as tk
ventana = tk.Tk()
ventana.title = ('prueba tinkter')
ventana.geometry = ('800x600')

label = tk.Label(ventana, text='Tkinter funciona!')
label.pack ()
ventana.mainloop()'''