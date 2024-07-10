# from django.db import models
import cx_Oracle


# Create your models here.
class Departamento:
    def __init__(self):
        self.conn = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")

    def listardptos(self):
        consulta = 'SELECT * FROM DEPT'
        try:
            cursor = self.conn.cursor()
            cursor.execute(consulta, )
            return cursor
        except self.conn.Error as error:
            return error

    def datosdept(self, numdpt):
        try:
            consulta = 'SELECT * FROM DEPT WHERE DEPT_NO = :p1'
            cursor = self.conn.cursor()
            print("Busco el número", numdpt)
            cursor.execute(consulta, (numdpt,))
            return cursor
        except self.conn.Error as error:
            return error

    def altadept(self, numdpt, nom, loc):
        cursor = self.conn.cursor()
        try:
            consultaalta = "INSERT INTO DEPT (DEPT_NO, DNOMBRE, LOC) VALUES (:p1, :p2, :p3)"
            cursor.execute(consultaalta, (numdpt, nom, loc))
            if cursor.rowcount > 0:
                self.conn.commit()
                cursor.close()
        except self.conn.Error as error:
            return error
        return cursor.rowcount

    def editadept(self, numdpt, nom, loc):
        cursor = self.conn.cursor()
        try:
            consulta = "UPDATE DEPT SET DNOMBRE = :p1, LOC = :p2 WHERE DEPT_NO = :p3"
            cursor.execute(consulta, (nom, loc, numdpt))
            if cursor.rowcount > 0:
                self.conn.commit()
                cursor.close()
        except self.conn.Error as error:
            return error
        return cursor.rowcount

    def bajadept(self, numdpt):
        cursor = self.conn.cursor()
        try:
            consultabaja = "DELETE FROM DEPT WHERE DEPT.DEPT_NO = :p1"
            print("Intentamos borrar el:", numdpt)
            cursor.execute(consultabaja, (numdpt,))
            print("Vamos a borrar el:", numdpt)
            if cursor.rowcount > 0:
                self.conn.commit()
                cursor.close()
        except self.conn.Error as error:
            print("La baja ha peteao", error)
            return error
        return cursor.rowcount
