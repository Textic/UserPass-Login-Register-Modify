import os

def clear():
    os.system('cls')

def login(name, password):
    file = open("profesor.txt", "r")
    for i in file:                      # i = linea de archivo
        a, b = i.split(":")             # separa por : y la guarda en a y b
        b = b.strip()                   # limpia el string de b (\n)
        if a == name and b == password:
            file.close()
            return True
    file.close()
    return False

def register(name, password):
    if login(name, password) == True:
        print("El usuario ya existe")
        return False
    else:
        file = open("profesor.txt", "a")
        file.write(name + ":" + password + "\n")
        file.close()
        return True

def replace(name, password):
    if login(name, password) == True:
        file = open("profesor.txt", "r")
        for i in file:
            userpass = i.strip('\n')
            a, b = i.split(":")
            b = b.strip()
            if a == name and b == password:
                clear()
                print(f'Nombre Anterior: {a}')
                a1 = input('Ingrese su nuevo nombre de usuario: ')
                clear()
                print(f'Contraseña Anterior: {b}')
                b2 = input('Ingrese su nueva contraseña: ')
                userpass1 = a1 + ":" + b2
                with open("profesor.txt", "r") as fileopened:
                    filedata = fileopened.read()
                filedata = filedata.replace(userpass, userpass1)
                with open("profesor.txt", "w") as fileopened:
                    fileopened.write(filedata)
                file.close()
                return True
    return False

menu = 9
while menu != 0:
    name = ""
    password = ""
    clear()

    print("1. Login")
    print("2. Registrarse")
    print("3. Modificar usuario")
    print("0. Salir")

    menu = int(input("\nIngrese una opcion: "))
    if menu == 1:
        clear()
        name = input("Ingrese su nombre: ")
        clear()
        password = input("Ingrese su contraseña: ")
        if login(name, password) == True:
            print("\nBienvenido")
            input("Presione enter para continuar...")
        else:
            print("\nUsuario o contraseña incorrectos")
            input("Presione enter para continuar...")
    elif menu == 2:
        clear()
        name = input("Ingrese su nombre: ")
        clear()
        password = input("Ingrese su contraseña: ")
        if register(name, password) == True:
            print("\nRegistro exitoso")
            input("Presione enter para continuar...")
        else:
            input("\nPresione enter para continuar...")
    elif menu == 3:
        clear()
        name = input("Ingrese su nombre: ")
        clear()
        password = input("Ingrese su contraseña: ")
        if login(name, password) == True:
            replace(name, password)
            print("\nModificacion exitosa")
            input("Presione enter para continuar...")
        else:
            print("\nModificacion incorrecta")
            input("Presione enter para continuar...")
