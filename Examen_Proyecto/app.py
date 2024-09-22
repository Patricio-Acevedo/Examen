
from flask import Flask, render_template, request

app = Flask(__name__)

# Página principal con los botones Ejercicio 1 y Ejercicio 2
@app.route('/')
def index():
    return render_template('index.html')

# ------------------ Ejercicio 1: Cálculo de compras ------------------

@app.route('/ejercicio1')
def ejercicio1():
    return render_template('ejercicio1.html')

@app.route('/procesar_formulario', methods=['POST'])
def procesar_formulario():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    cantidad_tarros = int(request.form['cantidad_tarros'])
    precio_por_tarro = 9000

    # Calcular el total sin descuento
    total_sin_descuento = cantidad_tarros * precio_por_tarro

    # Determinar el descuento
    if 18 <= edad <= 30:
        descuento = 0.15  # 15%
    elif edad > 30:
        descuento = 0.25  # 25%
    else:
        descuento = 0  # Sin descuento

    # Calcular el total con descuento
    total_con_descuento = total_sin_descuento * (1 - descuento)
    monto_descuento = total_sin_descuento * descuento

    return render_template('ejercicio1.html',
                           nombre=nombre,
                           total_sin_descuento=total_sin_descuento,
                           descuento=monto_descuento,
                           total_con_descuento=total_con_descuento)

# ------------------ Ejercicio 2: Inicio de sesión ------------------

@app.route('/ejercicio2')
def ejercicio2():
    return render_template('ejercicio2.html')

@app.route('/verificar_usuario', methods=['POST'])
def verificar_usuario():
    nombre = request.form['nombre']
    contrasena = request.form['contrasena']

    # Verificación de credenciales
    if nombre == "juan" and contrasena == "admin":
        mensaje = "Bienvenido administrador juan"
    elif nombre == "pepe" and contrasena == "user":
        mensaje = "Bienvenido usuario pepe"
    else:
        mensaje = "Usuario o contraseña incorrectos"

    return render_template('ejercicio2.html', mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
