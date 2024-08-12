from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

# Cargar datos desde un archivo CSV
datos = pd.read_csv('datos_estudiantes.csv')

# Convertir la columna 'ID' a string para evitar problemas de tipo
datos['ID'] = datos['ID'].astype(str)

@app.route('/qr-datos-estudiantes', methods=['GET'])
def mostrar_datos():
    id_estudiante = request.args.get('id')
    if not id_estudiante:
        return render_template('index.html', error="ID del estudiante es requerido")

    try:
        # Buscar el estudiante por ID
        fila = datos[datos['ID'] == id_estudiante]
        if fila.empty:
            return render_template('index.html', error="Estudiante no encontrado")

        # Convertir la fila a un diccionario con los nombres de columna correctos
        datos_estudiante = fila.iloc[0].to_dict()

        # Depuración: Imprimir el diccionario de datos para verificar su contenido
        print(datos_estudiante)

        return render_template('index.html',
                               nombre=datos_estudiante.get('NOMBRE COMPLETO', ''),
                               domicilio=datos_estudiante.get('DOMICILIO', ''),
                               tipo_sangre=datos_estudiante.get('TIPO DE SANGRE', ''),
                               nss=datos_estudiante.get('NUMERO DE SEGURIDAD SOCIAL', ''),
                               contacto_emergencia=datos_estudiante.get('CONTACTO DE EMERGENCIA', ''))
    except Exception as e:
        print(f"Error: {e}")
        return render_template('index.html', error="Ocurrió un error al procesar la solicitud.")

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=5000, debug=True)

