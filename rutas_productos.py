# rutas_productos.py
from flask import Blueprint, render_template

# Crear el Blueprint
rutas_productos = Blueprint("rutas_productos", __name__)

# Ruta para /productos
@rutas_productos.route("/productos")
def productos():
    """
    Retorna la plantilla productos.html
    """
    return render_template("productos.html")
