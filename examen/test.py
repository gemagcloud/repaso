import cx_Oracle

connection = cx_Oracle.connect("system", "pythonoracle", "localhost/XE")
consulta = 'SELECT * FROM DEPT'
try:
    cursor = connection.cursor()
    print("Realizo consulta:", consulta)
    cursor.execute(consulta)
    print('Resultado consulta:', cursor)
except connection.Error as error:
    print('Error', error)
