# app.py
from flask import Flask, render_template
from rutas_productos import rutas_productos  # Importar Blueprint

# Crear la instancia de Flask
aplicacion = Flask(__name__)

# Registrar el Blueprint de productos
aplicacion.register_blueprint(rutas_productos)

# Rutas principales
@aplicacion.route("/")
def inicio():
    """
    Función asociada a la ruta principal (/).
    Retorna la plantilla index.html.
    """
    return render_template("index.html")

@aplicacion.route("/acerca")
def acerca():
    """
    Función asociada a la ruta /acerca.
    Retorna la plantilla acerca.html con información sobre el proyecto.
    """
    return render_template("acerca.html")

# Punto de entrada de la aplicación
if __name__ == "__main__":
    # Ejecutar la app en modo depuración y puerto 5000
    # host="0.0.0.0" permite acceso desde la red local
    aplicacion.run(host="0.0.0.0", port=5000, debug=True)
