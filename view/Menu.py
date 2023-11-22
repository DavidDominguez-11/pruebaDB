from controllers import Database
from controllers import Traductor
from controllers import Chat
from controllers import ConsultasChatbot
from controllers import ConsultasTraductor
from users import Chatbot
from users import TraductorU
from users import SuperUser


class Menu:
    def __init__(self):
        self.type_users = ("chat", "traslate", "super")
        self.usuario_actual = None
        self.db = Database('localhost', 'root', '', 'proyecto_2')

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
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        flag = self.db.verificar_usuario(username, password)
        if flag:
            print(f"Bienvenido, {username}!")
            data_user = self.get_user(username)
            self.usuario_actual = self.set_user(data_user)
        else:
            print("Nombre de usuario o contraseña incorrectos.")

    def crear_cuenta(self):
        try:
            nombre = input("Ingrese un nombre de usuario: ")
            contrasena = input("Ingrese una contraseña: ")
            type_user = input(
                f"Que tipo de usuario sera ({', '.join(self.type_users)}): ")
            type_user = type_user.lower().strip()
            if type_user not in self.type_users:
                raise ValueError("Tipo de usuario no válido")
            flag = self.db.crear_cuenta(nombre, contrasena, type_user)
            if not flag:
                raise ValueError("No se pudo crear la cuenta")
            print("Cuenta creada exitosamente")
        except ValueError as e:
            print(e)

    def mostrar_menu_usuario(self):
        while True:

            userT = self.usuario_actual.get_type_user().lower()

            if userT == self.type_users[0]:

                print(" Menu de Usuario ")
                print("1. ChatBot")
                print("2. Cerrar sesion")
                opcion = input("Seleccione una opcion: ")

                if opcion == "1":
                    self.chatbot()
                elif opcion == "2":
                    self.usuario_actual = None
                    print("Sesión cerrada.")
                    break
                else:
                    print("Opción no valida")

            elif userT == self.type_users[1]:

                print(" Menu de Usuario ")
                print("1. Traductor")
                print("2. Cerrar sesion")
                opcion = input("Seleccione una opcion: ")

                if opcion == "1":
                    self.traductor()
                elif opcion == "2":
                    self.usuario_actual = None
                    print("Sesión cerrada.")
                    break
                else:
                    print("Opción no valida")

            elif userT == self.type_users[2]:
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
        if isinstance(self.usuario_actual, TraductorU) or isinstance(self.usuario_actual, SuperUser):
            username = self.usuario_actual.get_username()
            type_class = ConsultasTraductor.ConsultasTraductor()
            data = self.get_data(username, type_class)
            idioma1, idioma2 = self.split_data(data)
            self.usuario_actual.set_idioma_original(idioma1)
            self.usuario_actual.set_idioma_final(idioma2)
            traductor = Traductor()
            texto_a_traducir = input("Ingrese el texto que desea traducir: ")
            texto_traducido = traductor.traducirTexto(texto_a_traducir)
            print(texto_traducido)
            self.seve_data(username, type_class,
                           texto_a_traducir, texto_traducido)
            historial = self.get_data(username, type_class)
            for registro in historial:
                print(registro)
        else:
            print("Acceso no autorizado.")

    def chatbot(self):
        if isinstance(self.usuario_actual, Chatbot) or isinstance(self.usuario_actual, SuperUser):
            username = self.usuario_actual.get_username()
            type_class = ConsultasChatbot.ConsultasChatbot()
            data = self.get_data(username, type_class)
            texto1, texto2 = self.split_data(data)
            self.usuario_actual.set_input_text(texto1)
            self.usuario_actual.set_output_text(texto2)
            chat = Chat()
            texto = input(f"{username}: ").strip()
            texto_respuesta = chat.hacerPregunta(texto)
            self.seve_data(username, type_class, texto, texto_respuesta)
            print(texto_respuesta)
            historial = self.get_data(username, type_class)
            for registro in historial:
                print(registro)

        else:
            print("Acceso no autorizado.")

    def split_data(self, lista):
        lista1 = []
        lista2 = []
        for diccionario in lista:
            key1, key2 = diccionario.keys()
            lista1.append(diccionario[key1])
            lista2.append(diccionario[key2])
        return (lista1, lista2)

    def seve_data(self, username, type_class, text1, text2):
        type_class.guardar_data(username, text1, text2)

    def get_data(self, username, type_class):
        return type_class.obtener_data(username)

    def set_user(self, data):
        user = None
        id_ = data[0]
        username = data[1]
        password = data[2]
        type_user = data[3]
        if type_user == self.type_users[0]:
            user = Chatbot(id_, username, password, type_user)
        elif type_user == self.type_users[1]:
            user = TraductorU(id_, username, password, type_user)
        elif type_user == self.type_users[2]:
            user = SuperUser(id_, username, password, type_user)
        return user

    def get_user(self, username):
        return self.db.get_user(username)
