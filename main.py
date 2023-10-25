class Usuario:
    def __init__(self, nombre, contrasena):
        self.nombre = nombre
        self.contrasena = contrasena

class Menu:
    def __init__(self):
        self.usuarios = []
        self.usuario_actual = None

    def mostrar_menu_principal(self):
        
        while True:

            if self.usuario_actual:
                self.mostrar_menu_usuario()  # Redirigir al menú de usuario si ya ha iniciado sesión
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

        for usuario in self.usuarios:
            if usuario.nombre == nombre and usuario.contrasena == contrasena:
                self.usuario_actual = usuario
                print(f"Bienvenido, {usuario.nombre}!")
                return

        print("Nombre de usuario o contraseña incorrectos.")

    def crear_cuenta(self):
        nombre = input("Ingrese un nombre de usuario: ")
        contrasena = input("Ingrese una contraseña: ")

        nuevo_usuario = Usuario(nombre, contrasena)
        self.usuarios.append(nuevo_usuario)
        print("Cuenta creada exitosamente")

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


