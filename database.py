import mysql.connector


class Database:
    def __init__(self, host, user, password, database):
        self.config = {
            'host': host,
            'user': user,
            'password': password,
            'database': database,
        }

    def conectar(self):
        return mysql.connector.connect(**self.config)

    def verificar_usuario(self, username, password):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            query = "SELECT id FROM user WHERE User = %s AND Password = %s"
            cursor.execute(query, (username, password))
            result = cursor.fetchone()

            return bool(result)

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    def usuario_existe(self, username):
        try:
            connection = self.conectar()
            cursor = connection.cursor()

            query = "SELECT id FROM user WHERE User = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()

            return bool(result)

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return True
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()

    def crear_cuenta(self, username, password):
        if self.usuario_existe(username):
            print("El nombre de usuario ya está en uso. Por favor, elija otro.")
            return False

        try:
            connection = self.conectar()
            cursor = connection.cursor()

            cursor.execute("SELECT MAX(id) FROM user")
            result = cursor.fetchone()
            last_id = result[0] if result[0] is not None else 0

            query = "INSERT INTO user (ID, User, Password) VALUES (%s, %s, %s)"
            cursor.execute(query, (last_id + 1, username, password))
            connection.commit()

            return True

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()
