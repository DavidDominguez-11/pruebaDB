from Usuario import Usuario
import ConsultasI


class Traductor(Usuario):
    def __init__(self):
        super().__init()

    def mostrar_menu(self):
        while True:
            print(" Menú de Traductor ")
            print("1. Realizar tarea de traducción")
            print("2. Cerrar sesión")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.realizar_tarea_traduccion()
            elif opcion == "2":
                self.cerrar_sesion()
                break
            else:
                print("Opción no válida")

    def realizar_tarea_traduccion(self):
        print("Realizando tarea de traducción...")

        result = ConsultasI.Consultas().obtener_idiomas_usuario(3)
        print(result)
