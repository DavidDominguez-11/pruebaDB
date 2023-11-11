import mysql.connector
from database import Database
class Consultas:
    def __init__(self):
        self.db = Database('localhost', 'root', '', 'proyecto_2')

    def obtener_idiomas_usuario(self, user_id):
        try:
            connection = self.db.conectar()
            cursor = connection.cursor()

            query = "SELECT idioma1, idioma2 FROM traducciones WHERE ID = %s"
            cursor.execute(query, (user_id,))
            result = cursor.fetchone()

            return result if result else (None, None)


        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return None, None
        finally:
            if 'connection' in locals() and connection.is_connected():
                cursor.close()
                connection.close()