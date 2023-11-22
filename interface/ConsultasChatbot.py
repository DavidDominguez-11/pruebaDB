from interface import ConsultaI
import mysql.connector
from controllers import Database


class ConsultasChatbot(ConsultaI):
    def __init__(self):
        self.db = Database('localhost', 'root', '', 'proyecto_2')

    def obtener_traducciones(self, usuario_actual):
        connection = None
        cursor = None
        try:
            connection = self.db.conectar()
            cursor = connection.cursor(dictionary=True)

            query_id = "SELECT ID FROM user WHERE User = %s"
            cursor.execute(query_id, (usuario_actual,))
            user_result = cursor.fetchone()

            if not user_result:
                print("Usuario no encontrado.")
                return []

            user_id = user_result[0] if isinstance(
                user_result, tuple) else user_result['ID']

            query = "SELECT entrada, salida FROM chatbot WHERE ID = %s"
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

    def guardar_traducciones(self, usuario_actual, texto_idioma1, texto_idioma2):
        try:
            connection = self.db.conectar()
            cursor = connection.cursor()

            query_id = "SELECT ID FROM user WHERE User = %s"
            cursor.execute(query_id, (usuario_actual,))
            user_result = cursor.fetchone()

            user_id = user_result[0] if isinstance(
                user_result, tuple) else user_result['ID']

            query = "INSERT INTO chatbot (ID, entrada, salida) VALUES (%s, %s, %s)"
            cursor.execute(query, (user_id, texto_idioma1, texto_idioma2))
            connection.commit()

            print("Traducción guardada exitosamente.")

        except mysql.connector.Error as err:
            print(f"Error al guardar la traducción: {err}")
        finally:
            if cursor:
                cursor.close()
            if connection and connection.is_connected():
                connection.close()
