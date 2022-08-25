from flask import Flask, request, render_template

app = Flask(__name__)

with app.app_context():
    citas = []
    print(citas)


@app.route("/", methods=['GET', 'POST'])
def post():
    if request.method == 'POST':
        nombre = request.form['nombre'].capitalize()
        apellido = request.form['apellido'].capitalize()
        cedula = request.form['cedula']
        fecha = request.form['fecha']
        hora = request.form['hora']
        newCita = {
            "nombre": nombre,
            "apellido": apellido,
            "cedula": str(cedula),
            "fecha": str(fecha),
            "hora": str(hora)
        }
        citas.append(newCita)
        print(citas)
        return render_template("index.html")
    return render_template("index.html")


@app.route("/citas", methods=['GET'])
def show():
    return render_template("citas.html", citas=citas)


if __name__ == '__main__':
    app.run(debug=True)
