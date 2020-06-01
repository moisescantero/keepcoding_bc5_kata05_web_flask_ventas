import csv
import sqlite3

filename = "./sales10.csv"
database = "./data/ventas.db"

conn = sqlite3.connect(database)#creamos conexión
cur = conn.cursor()#creamos cursor

fSales = open(filename, "r")
csvreader = csv.reader(fSales, delimiter = ",")

headerRow = next(csvreader)#así anulamos la primera línea del csv
print(headerRow)

query = 'INSERT OR IGNORE INTO productos (tipo_producto, precio_unitario, coste_unitario) VALUES (?,?,?);'

for dataRow in csvreader:
    tupla_datos = ( dataRow[2], float(dataRow[9]), float(dataRow[10]) )#tipo_producto, precio_unitario y coste_unitario
    cur.execute(query, tupla_datos)

conn.commit()
conn.close()


