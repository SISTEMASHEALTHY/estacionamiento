import mysql.connector  # conector para mysql

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='estacionamiento'
        )
        print("Conexión exitosa a la base de datos")
        return connection
    except Exception as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None