import sqlite3
import csv

fVentas = open('./sales10.csv', 'r')#abrir fichero CSV y guardar en variable fVentas
csvreader = csv.reader(fVentas, delimiter=',')#guardar valores separados por "," de fichero csv a variable csvreader

conn = sqlite3.connect('data/ventas.db')#crear base de datos en ruta y guardar en variable
c = conn.cursor()#crear cursor para base de datos y guardar en variable

def create_table():#función crear tabla
    # Create table, con orden SQL ejecutar crear tabla si no existe llamada "productos" con esos campos y características de cada uno
    c.execute('''CREATE TABLE IF NOT EXISTS "productos" (
    "tipo_producto" TEXT NOT NULL UNIQUE,
    "precio_unitario"   REAL NOT NULL,
    "coste_unitario"    INTEGER NOT NULL)''')
 
d = {}#diccionario vacío
for linea in csvreader: #recorrer para cada valor en variable csvreader
    if linea[2] not in d and linea[2] != 'tipo_producto':#si valor tipo_producto no está en d y no vale "tipo_producto"
        d[linea[2]] = {"precio_unitario":float(linea[9]), "coste_unitario":float(linea[10])}#se guarda diccionario dentro de d //
        #//con clave:babyfood  valores precio_unitario:valor y coste_unitario:valor
        #//RESULTADO:{1º 'Baby Food': {'precio_unitario': 255.28, 'coste_unitario': 159.42}, 
        # 2º 'Cereal': {'precio_unitario': 205.7, 'coste_unitario': 117.11}} 3º ... Y así hasta final de bucle

def data_entry():#función introducir valores en tabla
    for t_producto, precio_coste in d.items():#recorrer para tipo_producto, precio y coste en items del diccionario d
        c.execute("INSERT INTO productos (tipo_producto, precio_unitario, coste_unitario) VALUES ('{}', '{}', '{}')".format(t_producto, d[t_producto]["precio_unitario"], d[t_producto]["coste_unitario"]))
        #ejecutar insert(SQL) en tabla productos con valores 1º tipo_producto:clave(babyfood), babyfood:precio_unitario(255.28) y  
        # babyfood:coste_unitario(159.42), 2º tipo_producto:clave(cereal), cereal:precio_unitario(205.7) y  
        # cereal:coste_unitario(117.11), 3º... y así hasta final de bucle
    conn.commit()#comentar (por ahora magia) para validar los datos en tabla productos
    c.close()#cerramos cursor
    conn.close()#cerramos conexión a base de datos

def read_table():#función leer tabla
    #CONSULTO LO QUE HAY EN LA BASE DE DATOS, en la segunda vuelta. 
    c.execute("SELECT * FROM productos")#ejecutar select para ver todos los valores de la tabla productos
    print (c.fetchall())#imprimir todo el contenido

create_table()#llamada a función create_table()
#data_entry()#llamada a función data_entry()
#read_table()#llamada a función read_table()