from flask import Flask, render_template, request
import csv, sqlite3


app = Flask(__name__)#creamos app
BASE_DATOS = ("./data/ventas.db")
        
@app.route("/")
def index():
    fVentas = open("./sales10.csv", "r")
    csvreader = csv.reader(fVentas, delimiter= ",")

    d = {}
    for linea in csvreader:        
        if linea[0] in d:
            d[linea[0]]["ingresos"] += float(linea[11])
            d[linea[0]]["beneficios"] += float(linea[13])
        else:
            if linea[0] != "region":
                d[linea[0]] = {"ingresos": float(linea[11]), "beneficios": float(linea[13])}

    return render_template("region.html", ventas=d)#método de flask para importar html y pasamos diccionario d a region.html

@app.route("/paises")
def paises():
    region_name = request.values["region"]

    fVentas = open("./sales10.csv", "r")
    csvreader = csv.reader(fVentas, delimiter= ",")

    d = {}
    for linea in csvreader:
        if linea[0] == region_name:#es pais igual al pais que deseamos?
            if linea[1] in d:#si está region en diccionario
                d[linea[1]]["ingresos"] += float(linea[11])#obtener y añadir valor de ingresos
                d[linea[1]]["beneficios"] += float(linea[13])#obtener y añadir valor de beneficios
            else:#si no está en diccionario me lo creas y guardas region, ingresos y beneficios
                d[linea[1]] = {"ingresos": float(linea[11]), "beneficios": float(linea[13])}
        
    return render_template("paises.html", ventas=d, region_nm=request.values["region"])#método de flask para importar html y pasamos diccionario d a paises.html


@app.route("/productos")
def productos():#consultar listado de productos
    
    conn = sqlite3.connect(BASE_DATOS)
    cur = conn.cursor()

    query = 'SELECT id, tipo_producto, precio_unitario, coste_unitario FROM productos;'
    productos = cur.execute(query).fetchall()

    conn.close()
    return render_template("productos.html", productos=productos)


@app.route("/addproducto")
def addproducto():
    return render_template('newproduct.html')