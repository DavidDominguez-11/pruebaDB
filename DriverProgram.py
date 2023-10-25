from main import *

if __name__ == "__main__":
    menu = Menu()
    
    # usuario de prueba admin
    usuario_prueba = Usuario("Admin", "12345")
    menu.usuarios.append(usuario_prueba)
    
    while True:
        menu.mostrar_menu_principal()
        if menu.usuario_actual:
            menu.mostrar_menu_usuario()
