import database
import ConsultasI

from Traductor import Traductor
from Chat import Chat

class Menu:
    def __init__(self):
        self.usuario_actual = None
        self.db = database.Database('localhost', 'root', '', 'proyecto_2')
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

        flag = self.db.verificar_usuario(nombre, contrasena)
        if flag:
            self.usuario_actual = nombre
            print(f"Bienvenido, {nombre}!")
        else:
            print("Nombre de usuario o contraseña incorrectos.")

    def crear_cuenta(self):
        nombre = input("Ingrese un nombre de usuario: ")
        contrasena = input("Ingrese una contraseña: ")

        flag = self.db.crear_cuenta(nombre, contrasena)
        if flag:
            print("Cuenta creada exitosamente")
        else:
            print("No se pudo crear la cuenta")

    def mostrar_menu_usuario(self):
        while True:
            print(" Menu de Usuario ")
            print("1. Traductor")
            print("2. ChatBot")
            print("3. Cerrar sesion")
            opcion = input("Seleccione una opcion: ")

            if opcion == "1":
                self.traductor()
            elif opcion == "2":
                self.chatbot()
            elif opcion == "3":
                self.usuario_actual = None
                print("Sesión cerrada.")
                break
            else:
                print("Opción no valida")

    def traductor(self):

        #instancia de la clase Traductor
        traductor = Traductor()

        texto_a_traducir = input("Ingrese el texto que desea traducir: ")
        traductor.traducirTexto(texto_a_traducir)

    def chatbot(self):
<<<<<<< HEAD
        print("ChatBot")
        texto1 = input("Ingrese texto a traducir: ")
        texto2 = "holamundo"
        if self.usuario_actual:
            # Guardar la traducción en la base de datos
            ConsultasI.Consultas().guardar_traducciones_usuario(self.usuario_actual, texto1, texto2)
            
            # Obtener el historial de traducciones del usuario actual
            historial = ConsultasI.Consultas().obtener_idiomas_usuario(self.usuario_actual)
            
            for registro in historial:
                print(registro)
        

=======
        # instacia de la clase Chat
        chat = Chat()
<<<<<<< HEAD

        mensaje = input("Ingrese su mensaje:" )
        chat.hacerPregunta(mensaje)
>>>>>>> 56c509ee3da8b80de8ec31efd274f74db1635174
=======
        chat.hacerPregunta()
>>>>>>> 0ba059b81ff08f5b1afbe144a42d117750210908
