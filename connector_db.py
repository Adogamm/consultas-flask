import mysql.connector


def obtener_conexion():
    try:
        return mysql.connector.connect(host='localhost',
                                    user='root',
                                    password='Pkwed*0115',
                                    db='db_indumentaria')
    except mysql.connector.Error as e:
        error_msg = f"DB_CONNECTOR : {e}"
        print(error_msg)
