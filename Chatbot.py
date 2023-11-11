from Usuario import Usuario


class Chatbot(Usuario):
    def __init__(self):
        super().__init()

    def mostrar_menu(self):
        while True:
            print(" Menú de Chatbot ")
            print("1. Realizar tarea de chatbot")
            print("2. Cerrar sesión")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.realizar_tarea_chatbot()
            elif opcion == "2":
                self.cerrar_sesion()
                break
            else:
                print("Opción no válida")

    def realizar_tarea_chatbot(self):
        print("Realizando tarea de chatbot...")
