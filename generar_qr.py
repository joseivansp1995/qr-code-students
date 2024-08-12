import qrcode
import pandas as pd
import barcode
from barcode.writer import ImageWriter

# Cargar datos desde un archivo CSV
datos = pd.read_csv('datos_estudiantes.csv')

def generar_qr_y_codigo_barras(id_estudiante, nombre_completo, url_base):
    # Asegurarse de que el ID se maneje como una cadena
    id_estudiante = str(id_estudiante)
    
    # Reemplazar espacios por guiones bajos en el nombre
    nombre_formateado = nombre_completo.replace(" ", "_")

    # Generar el código QR
    url = f"{url_base}?id={id_estudiante}"
    qr = qrcode.make(url)
    qr.save(f"qr_{id_estudiante}_{nombre_formateado}.png")

    # Generar el código de barras en formato Code 39 sin caracteres adicionales
    code39 = barcode.Code39(id_estudiante, writer=ImageWriter(), add_checksum=False)
    code39.save(f"barcode_{id_estudiante}_{nombre_formateado}")

# URL base de la aplicación (ajústala según tus necesidades)
url_base = "https://web-production-9c4d.up.railway.app/"

for _, fila in datos.iterrows():
    generar_qr_y_codigo_barras(fila['ID'], fila['NOMBRE COMPLETO'], url_base)
