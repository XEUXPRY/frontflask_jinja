<<<<<<< HEAD
from flask import Flask, render_template
aplicacion = Flask(__name__)
@aplicacion.route(&#39;/&#39;)
def inicio():
return render_template(&#39;index.html&#39;)
if __name__ == &#39;__main__&#39;:
aplicacion.run(debug=True)
=======
# app.py
# ---------------------------------------------------------
# Archivo principal del proyecto Flask
# Aquí se configuran las rutas y la lógica inicial
# ---------------------------------------------------------
from flask import Flask, render_template

# Se crea la aplicación Flask
aplicacion = Flask(__name__)

# ---------------------------------------------------------
# Ruta para la página de inicio
# ---------------------------------------------------------
@aplicacion.route("/")
def inicio():
    """
    Renderiza la plantilla index.html
    """
    return render_template("index.html")

# ---------------------------------------------------------
# Ruta para la página "Acerca del proyecto"
# ---------------------------------------------------------
@aplicacion.route("/acerca")
def acerca():
    """
    Renderiza la plantilla acerca.html
    """
    return render_template("acerca.html")

# ---------------------------------------------------------
# Punto de entrada de la aplicación
# ---------------------------------------------------------
if __name__ == "__main__":
    # Se ejecuta la aplicación en el puerto 5000
    aplicacion.run(debug=True, port=5000)

>>>>>>> 34ab88a (Configuración inicial del proyecto Flask con Jinja2, entorno virtual y requirements.txt)
