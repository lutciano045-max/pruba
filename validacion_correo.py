#haremos que el usuario tenga que validar su correo electronico, al ponerlo mal que le salte un mensaje de que su correo no es valido
usuario =input("Ingrese su correo electronico: ")

if '@' in usuario and 'gmail' in usuario and '.com' in usuario:
    print('correo electronico valido')
elif '@' == '@@' and '@' == '@':
    print('correo electronico no valido')     
else:
    print('correo electronico no valido')
    

    
