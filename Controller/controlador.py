from mysqlx import Error
from SqlConnect.connector_db import SQLConnection
from TablesRegistry.registro_consultas import RegistroConsulta
from datetime import datetime

class Controller:
    def obtener_ropa(self):
        try:
            conexion = SQLConnection.connection();
            ropa = []
            with conexion.cursor() as cursor:
                cursor.execute("select articulos.id, articulos_ropa_detalles.* from articulos join articulos_ropa_detalles on articulos.id = articulos_ropa_detalles.idArticulo")
                ropa = cursor.fetchall()
            conexion.close()
        except Error as e:
            error_msg = f"OBTENER REGISTROS : {e}"
            print(error_msg)
        else:
            #Registro
            registro_datos = f"Consulta Ropa|{datetime.today()}\n"
            for i in ropa:
                registro_datos += f"{i[0]};{i[1]};{i[2]};{i[3]};{i[4]};{i[5]};{i[6]};{i[7]}\n"
            RegistroConsulta.registro("",registro_datos)
        return ropa

    def obtener_accesorio(self):
        try:
            conexion = SQLConnection.connection()
            accesorio = []
            with conexion.cursor() as cursor:
                cursor.execute("select articulos.id, articulos_accesorios_detalles.* from articulos join articulos_accesorios_detalles on articulos.id = articulos_accesorios_detalles.idArticulo")
                accesorio = cursor.fetchall()
            conexion.close()
        except Error as e:
            error_msg = f"OBTENER REGISTROS : {e}"
            print(error_msg)
        else:
            #Registro
            registro_datos = f"Consulta Accesorio|{datetime.today()}\n"
            for i in accesorio:
                registro_datos += f"{i[0]};{i[1]};{i[2]};{i[3]};{i[4]}\n"
            RegistroConsulta.registro("",registro_datos)
            return accesorio

    def obtener_calzado(self):
        try:
            conexion = SQLConnection.connection()
            calzado = []
            with conexion.cursor() as cursor:
                cursor.execute("select articulos.id, articulos_calzados_detalles.* from articulos join articulos_calzados_detalles on articulos.id = articulos_calzados_detalles.idArticulo")
                calzado = cursor.fetchall()
            conexion.close()
        except Error as e:
            error_msg = f"OBTENER REGISTROS : {e}"
            print(error_msg)
        else:
            #Registro
            registro_datos = f"Consulta Calzado|{datetime.today()}\n"
            for i in calzado:
                registro_datos += f"{i[0]};{i[1]};{i[2]};{i[3]};{i[4]};{i[5]};{i[6]}\n"
            RegistroConsulta.registro("",registro_datos)
            return calzado