import mysql.connector
from controllers import Database
from interface import ConsultaI


class Consulta_Traductor(ConsultaI):
    def __init__(self):
        self.db = Database('localhost', 'root', '', 'proyecto_2')

    # Funciones para la base de datos Traductor
    def get_data(self, username):
        connection = None
        cursor = None
        try:
            connection = self.db.conectar()
            cursor = connection.cursor(dictionary=True)

            # Obtener el ID del usuario actual
            query_id = "SELECT ID FROM user WHERE User = %s"
            cursor.execute(query_id, (username,))
            user_result = cursor.fetchone()

            if not user_result:
                print("Usuario no encontrado.")
                return []

            user_id = user_result[0] if isinstance(
                user_result, tuple) else user_result['ID']

            query = "SELECT Idioma1, Idioma2 FROM traducciones WHERE ID = %s"
            cursor.execute(query, (user_id,))
            results = cursor.fetchall()

            return results if results else []

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return []
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()

    def save_data(self, username, data1, data2):
        try:
            connection = self.db.conectar()
            cursor = connection.cursor()

            # Obtener el ID del usuario actual
            query_id = "SELECT ID FROM user WHERE User = %s"
            cursor.execute(query_id, (username,))
            user_result = cursor.fetchone()

            user_id = user_result[0] if isinstance(
                user_result, tuple) else user_result['ID']

            query = "INSERT INTO Traducciones (ID, Idioma1, Idioma2) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, data1, data2))
            connection.commit()

            print("Traducción guardada exitosamente.")

        except mysql.connector.Error as err:
            print(f"Error al guardar la traducción: {err}")
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
