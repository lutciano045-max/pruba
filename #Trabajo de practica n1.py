#Trabajo de practica
print('nombre_de_usuario')
usuario_registrado = 'luciano'
nombre_de_usuario = input()
if usuario_registrado == nombre_de_usuario:
     print('bienvenido' , nombre_de_usuario)
elif nombre_de_usuario != usuario_registrado:
     print('nombre de usuario erroneo')
     nombre_de_usuario = input()
     if usuario_registrado == nombre_de_usuario:
          print('bienvenido', nombre_de_usuario)
print('Escribe tu contraseña')
contraseña_guardada = 'santino'
escribir_contraseña = input()
if contraseña_guardada == escribir_contraseña:
     print('bienvenido', nombre_de_usuario)
elif contraseña_guardada != nombre_de_usuario:
     print('te quedan dos intentos pa')
     escribir_contraseña = input()
     if contraseña_guardada == escribir_contraseña:
          print('bienvenido', nombre_de_usuario)
     elif contraseña_guardada != escribir_contraseña:
          print('ultimo intento pa')
          escribir_contraseña = input()
          if contraseña_guardada == escribir_contraseña:
               print('bienvenido', nombre_de_usuario)
          else:
               print('acceso denegado')