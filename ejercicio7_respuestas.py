#Escribir un programa que pregunte el correo electrónico del usuario,en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba `@`) pero con dominio `ceu.es`.

email = input('ingrese su correo electronico: ')
print(email.replace(email, email[:email.find('@')]+'@gmail.com'))
