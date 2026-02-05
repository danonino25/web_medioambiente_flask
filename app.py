from flask import Flask, render_template

app = Flask(__name__)

# Ruta principal
@app.route('/')
def index():
    return render_template(
        'index.html',
        breadcrumb=["Inicio"]
    )

# Sistema de Gestión Ambiental
@app.route('/sistema-ambiental')
def sistema():
    return render_template(
        'sistema.html',
        breadcrumb=["Inicio", "Sistema de Gestión Ambiental"]
    )

# Futuro del planeta
@app.route('/futuro')
def futuro():
    return render_template(
        'futuro.html',
        breadcrumb=["Inicio", "Futuro del Planeta"]
    )

# Las 3 R
@app.route('/tres-r')
def tres_r():
    return render_template(
        'tres_r.html',
        breadcrumb=["Inicio", "Las 3 R"]
    )

# Ejecución de la aplicación
if __name__ == '__main__':
    app.run(debug=True)
