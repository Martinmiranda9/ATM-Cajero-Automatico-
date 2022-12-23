import time
global opc

print("------ CAJERO AUTOMATICO -------")

clientes = {"ADMIN":["00",20000],
            "Martin":["01", 10000],
            "Walter":["02", 10000]}

def menu():
    time.sleep(2)
    print("¿Que operacion desea realizar?\n1-Mi cuenta (Cambiar clave).\n2-Ingresar dinero.\n3-Retirar dinero."
    "\n4-Consultar saldo.\n5-Pedir prestamo.\n6-Salir. ")
    print("-------------------------------------------")


def login():
    global user
    user = input("Ingrese su usuario: ")
    global password
    password = input("Ingrese su contraseña: ")
    if user in clientes.keys() and password in clientes[user][0] and clientes.keys() != "ADMIN" and clientes[user][0]\
            != "00":
        print("-------INGRESANDO-------")
        time.sleep(2)
        print("    BIENVENIDO", user,   )

    elif user == "ADMIN" and password == "00":
        print("-------INGRESANDO-------")
        time.sleep(2)
        print("    BIENVENIDO", user, )
        print("-------------------------------------------")
    else:
        time.sleep(1)
        print("---------------------------------------------------------")
        print("El usuario o la contraseña son erroneas, por favor revise")
        login()

login()


def menuAdmin():
    print("-------------------------------------------")
    print("¿Que operacion desea realizar?\n1-Mi cuenta (Cambiar clave).\n2-Ingresar dinero.\n3-Retirar dinero."
          "\n4-Consultar saldo.\n5-Agregar cliente.\n6-Salir.")
    print("---------------------------------------------")
    try:
        global opc
        opc = int(input("Ingrese el numero de operacion: "))
        print("-------------------------------------------------------")
    except ValueError:
        print("-------------------------------------------")
        print("¡ERROR! DEBE INGRESAR UN NUMERO")
        print("-------------------------------------------")
        time.sleep(2)
        return opc


def cambiarClave():
    print("----------------------------------------------")
    clientes[user][0] = input("Ingrese su nueva contraseña: ")
    time.sleep(1)
    print("----------------------------------------------")
    print("CONTRASEÑA MODIFICADA CON EXITO")
    time.sleep(1)
    print("----------------------------------------------")
    print("Corrobore sus datos:\n1-USUARIO: ", user, "\n2-CONTRASEÑA: ", clientes[user][0])
    print("----------------------------------------------")
    time.sleep(2)


def deposito():
            print("----------------------------------------------")
            depositoMonto = int(input("Ingrese su monto a depositar: "))
            clientes[user][1] += depositoMonto
            time.sleep(1)
            print("-------- OPERACION EXITOSA -------- ")
            print("Su saldo acutal es de:", "$", clientes[user][1])
            print("----------------------------------------------")
            time.sleep(2)

def retiro():
            print("----------------------------------------------")
            retiroMonto = int(input("Ingrese su monto a retirar: "))
            while retiroMonto > clientes[user][1]:
                print("El saldo a retirar es superior al monto que tiene en su cuenta.")
                retiroMonto = int(input("Ingrese su monto a retirar: "))
            else:
                clientes[user][1] -= retiroMonto
                print("---- OPERACION EXITOSA ----")
                print("Su saldo es de", "$", clientes[user][1])
                print("----------------------------------------------")
                time.sleep(2)


def consultaSaldo():
    print("----------------------------------------------")
    print(user, ",su saldo es de:", "$", clientes[user][1])
    print("---------------------------------------------------------")
    time.sleep(2)

def agregarcliente():
            print("----------------------------------------------")
            agregar_usuario = input("Ingrese el nombre de usuario para agendar: ")
            clientes1 = []
            clientes1.append(input("Ingrese la contraseña del usuario: "))
            clientes1.append(input("Ingrese el monto del usuario: "))

            clientes[agregar_usuario] = [clientes1]
            print("El usuario se agrego correctamente. Por favor, revise los datos")
            print("--------------------------------")
            print("Usuario:", agregar_usuario)
            print("Contraseña:", clientes1[0])
            print("Monto:", clientes1[1])
            print("--------------------------------")
            print(clientes)
            time.sleep(2)

def pedir_prestamo():
    print("----------------------------------------------")
    print("Usteded puede pedir un prestamo hasta $",clientes[user][1] * 2)
    print("----------------------------------------------")
    monto_prestamo = int(input("Ingrese el monto del prestamo:"))
    print("----------------------------------------------")
    while monto_prestamo > clientes[user][1] * 2:
        print("El monto ingresado excede su importe maximo de prestamo.")
        monto_prestamo = int(input("Ingrese el monto del prestamo:"))
    else:
        print("-- PRESTAMO CONFIRMADO --")
        print("Su prestamo fue es de $",monto_prestamo)
        clientes[user][1] += monto_prestamo
        print("Su saldo actual es de:$",clientes[user][1])
        print("----------------------------------------------")
        time.sleep(2)



opc = int
while opc !=6:
    while user == "ADMIN" and password == "00":
        menuAdmin()

        if opc == 1:
               cambiarClave()

        elif opc == 2:
            deposito()

        elif opc == 3:
            retiro()

        elif opc == 4:
            consultaSaldo()

        elif opc == 5:
            agregarcliente()

        else:
            print("     CERRANDO SESION....     ")
            time.sleep(2)
            print("      MUCHAS GRACIAS         ")
            print("----------------------------------------------")
     


    while user in clientes.keys() and password in clientes[user][0] and clientes.keys() != "ADMIN" and\
            clientes[user][0]!= "00":
            menu()
            opc = int(input("Ingrese un numero de operacion: "))
            if opc == 1:
                cambiarClave()
            elif opc == 2:
                deposito()
            elif opc == 3:
                retiro()
            elif opc == 4:
                consultaSaldo()
            elif opc == 5:
                pedir_prestamo()
            else:
                print("     CERRANDO SESION....     ")
                time.sleep(2)
                print("      MUCHAS GRACIAS         ")
                print("----------------------------------------------")
                login()



















