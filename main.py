import ConectorSQL


class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena


class Menu:
    def __init__(self):
        self.usuario_actual = None

    def mostrar_menu_principal(self):

        while True:

            if self.usuario_actual:
                self.mostrar_menu_usuario()
                break

            print(" Menu Principal ")
            print("1. Iniciar Sesion")
            print("2. Crear Cuenta")
            print("3. Salir")
            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.login()
            elif opcion == "2":
                self.crear_cuenta()
            elif opcion == "3":
                return False
            else:
                print("Opcion no valida")

    def login(self):
        nombre = input("Ingrese su nombre de usuario: ")
        contrasena = input("Ingrese su contraseña: ")

        # pip install mysql-connector-python
        flag = ConectorSQL.verificar_usuario(nombre, contrasena)
        if flag:
            print(f"Bienvenido, {nombre}!")
        else:
            print("Nombre de usuario o contraseña incorrectos.")

    def crear_cuenta(self):
        nombre = input("Ingrese un nombre de usuario: ")
        contrasena = input("Ingrese una contraseña: ")

        flag = ConectorSQL.crear_cuenta(nombre, contrasena)
        if flag:
            print("Cuenta creada exitosamente")
        else:
            print("No se pudo crear la contraseña")

    def mostrar_menu_usuario(self):
        while True:
            print(" Menu de Usuario ")
            print("1. Traductor")
            print("2. ChatBot")
            print("3. Ver material")
            print("4. Cerrar sesion")
            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.traductor()
            elif opcion == "2":
                self.chatbot()
            elif opcion == "3":
                self.ver_material()
            elif opcion == "4":
                self.usuario_actual = None
                print("Sesión cerrada.")
                break
            else:
                print("Opción no valida")

    def traductor(self):
        print("Traductor")

    def chatbot(self):
        print("ChatBot")

    def ver_material(self):
        print("Ver material")
