from flask import Flask, render_template, request, redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3
        if asistencia >= 75 and promedio >= 40:
            estado = "APROBADO"
        else:
            estado = "REPROBADO"

        return render_template('ejercicio1.html', promedio=promedio, estado=estado)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        if len(nombre1) >= len(nombre2) and len(nombre1) >= len(nombre3):
            mayor_nombre = nombre1
        elif len(nombre2) >= len(nombre1) and len(nombre2) >= len(nombre3):
            mayor_nombre = nombre2
        else:
            mayor_nombre = nombre3

        cantidad_caracteres = len(mayor_nombre)

        return render_template(
            'ejercicio2.html',
            mayor_nombre=mayor_nombre,
            cantidad_caracteres=cantidad_caracteres
        )

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)