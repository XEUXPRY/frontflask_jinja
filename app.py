from flask import Flask, render_template
aplicacion = Flask(__name__)
@aplicacion.route(&#39;/&#39;)
def inicio():
return render_template(&#39;index.html&#39;)
if __name__ == &#39;__main__&#39;:
aplicacion.run(debug=True)
