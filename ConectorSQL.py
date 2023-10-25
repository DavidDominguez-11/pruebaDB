import mysql.connector

config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'proyecto 2',  # Nombre base de datos
}


def verificar_usuario(username, password):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        query = "SELECT id FROM user WHERE User = %s AND Password = %s"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        if result:
            print("Usuario encontrado")
        else:
            print("Usuario no encontrado")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


def crear_cuenta(username, password):
    try:
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        cursor.execute("SELECT MAX(id) FROM user")
        result = cursor.fetchone()
        last_id = result[0] if result[0] is not None else 0

        query = "INSERT INTO user (ID, User, Password) VALUES (%s, %s, %s)"
        cursor.execute(query, (last_id + 1, username, password))
        connection.commit()
        print("Cuenta creada con éxito")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()


crear_cuenta('hola2', 'como')  # ejemplo
verificar_usuario('hola2', 'como')  # ejemplo
