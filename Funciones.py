from conexion import get_db_connection

import win32print
import pandas as pd
import win32ui
from decimal import Decimal
from PIL import Image, ImageDraw, ImageFont
from barcode import Code128
from barcode.writer import ImageWriter
from io import BytesIO
from datetime import datetime
from PIL import ImageWin
from datetime import datetime
import os
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders




###Funciones base de datos
def registrar_tarifa(tipo_vehiculo,tipo_cliente,precio_hora,precio_extravio,precio_dia,precio_mes,id_usuario):
    try:
        conexion = get_db_connection()
        if not conexion or not conexion.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return {"Mensaje":"No se pudo conectar a la base de datos"}

        cursor = conexion.cursor()
        print("¡Se conectó con éxito!")

        # Aquí se ejecutara el procedimiento almacenado
        resultado= cursor.callproc('sp_guardar_tarifa', [tipo_vehiculo,tipo_cliente,precio_hora,precio_extravio,precio_dia,precio_mes,id_usuario,"",""])
        conexion.commit()

        print(resultado)
        tipo_vehiculo, tipo_cliente, precio_hora,precio_extravio,precio_dia,precio_mes,estatus, mensaje = resultado[0], resultado[1], resultado[2],resultado[3], resultado[4],resultado[6],resultado[7], resultado[8]

        


        return{"Estado": estatus, "Mensaje": mensaje, "Tipo_vehiculo": tipo_vehiculo,"Tipo_cliente":tipo_cliente,"Precio_hora": precio_hora,"Precio_Extravio":precio_extravio,"Precio_dia": precio_dia,"Presio_mes": precio_mes}

    except Exception as e:
        print(f"Error: {e}")
        return {"Error":{e}}

    finally:
        try:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
        except:
            pass  # Si falla aquí, cerramos de todos modos

def agregar_cliente(nombre,telefono,correo,tipoCliente,tipoPension,Placa,id_usuario,tipovehiculo):
    try:
        conexion = get_db_connection()
        if not conexion or not conexion.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return {"Mensaje":"No se pudo conectar a la base de datos"}

        cursor = conexion.cursor()
        print("¡Se conectó con éxito!")

        # Aquí se ejecutara el procedimiento almacenado
        resultado= cursor.callproc('sp_crear_cliente_con_ticket', [nombre,telefono,correo,tipoCliente,tipoPension,Placa,id_usuario,tipovehiculo,"",""])
        conexion.commit()

        print(resultado)
        nombre, telefono,correo,tipo_cliente,tipo_pension,placa,tipo_vehiculo,estado,mensaje= resultado[0],resultado[1],resultado[2],resultado[3],resultado[4],resultado[5],resultado[7],resultado[8],resultado[9]
        


        return{"Estado": estado, "Mensaje": mensaje, "Nombre": nombre,"Telefono":telefono,"Correo": correo,"Tipo cliente": tipo_cliente,"Tipo pension": tipo_pension, "Placas": placa,"Tipo Vehiculo":tipo_vehiculo}

    except Exception as e:
        print(f"Error: {e}")
        return {"Error":{e}}

    finally:
        try:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
        except:
            pass  # Si falla aquí, cerramos de todos modos

def agregar_entrada(placa,tipoVehiculo,id_usuario):
    try:
        conexion = get_db_connection()
        if not conexion or not conexion.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return {"Mensaje":"No se pudo conectar a la base de datos"}

        cursor = conexion.cursor()
        print("¡Se conectó con éxito!")

        # Aquí se ejecutara el procedimiento almacenado
        resultado= cursor.callproc('registrar_ticket', [placa,tipoVehiculo,id_usuario,"","",""])
        conexion.commit()

        print(resultado)
        placa,tipo_vehiculo,estado,mensaje, codigo = resultado[0],resultado[1],resultado[3],resultado[4],resultado[5]

        


        return{"Estado": estado, "Mensaje": mensaje, "Placa":placa,"Tipo":tipo_vehiculo, "codigo": codigo} 

    except Exception as e:
        print(f"Error: {e}")
        return {"Error":{e}}

    finally:
        try:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
        except:
            pass  # Si falla aquí, cerramos de todos modos

def check_precio(codigo,id_usuario):
    try:
        conexion = get_db_connection()
        if not conexion or not conexion.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return {"Mensaje":"No se pudo conectar a la base de datos"}

        cursor = conexion.cursor()
        print("¡Se conectó con éxito!")

        # Aquí se ejecutara el procedimiento almacenado
        resultado= cursor.callproc('checar_precio_ticket', [codigo,id_usuario,"","",0.0])

        print(resultado)
        codigo,estado,mensaje,precio= resultado[0], resultado[2],resultado[3],resultado[4]

        


        return{"Estado": estado, "Mensaje": mensaje, "codigo":codigo,"Precio":precio}

    except Exception as e:
        print(f"Error: {e}")
        return {"Error":{e}}

    finally:
        try:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
        except:
            pass  # Si falla aquí, cerramos de todos modos

def pagar_precio(codigo,id_usuario):
    try:
        conexion = get_db_connection()
        if not conexion or not conexion.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return {"Mensaje":"No se pudo conectar a la base de datos"}

        cursor = conexion.cursor()
        print("¡Se conectó con éxito!")

        # Aquí se ejecutara el procedimiento almacenado
        resultado= cursor.callproc('pagar_ticket', [codigo,id_usuario,"","",0.0])
        conexion.commit()

        print(resultado)
        codigo, estatus, mensaje,precio = resultado[0], resultado[2], resultado[3],resultado[4]

        


        return{"Estado": estatus, "Mensaje": mensaje, "codigo":codigo,"Precio":precio}

    except Exception as e:
        print(f"Error: {e}")
        return {"Error":{e}}

    finally:
        try:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
        except:
            pass  # Si falla aquí, cerramos de todos modos

def pagar_precio_Extravio(ticket,id_usuario):
    try:
        conexion = get_db_connection()
        if not conexion or not conexion.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return {"Mensaje":"No se pudo conectar a la base de datos"}

        cursor = conexion.cursor()
        print("¡Se conectó con éxito!")

        # Aquí se ejecutara el procedimiento almacenado
        resultado= cursor.callproc('pagar_ticket_extravio', [ticket,id_usuario,"","",0.0])
        conexion.commit()

        print(resultado)
        placa, estatus, mensaje,precio = resultado[0], resultado[1], resultado[2],resultado[3]

        


        return{"Estado": estatus, "Mensaje": mensaje, "placa":placa,"Precio":precio}

    except Exception as e:
        print(f"Error: {e}")
        return {"Error":{e}}

    finally:
        try:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
        except:
            pass  # Si falla aquí, cerramos de todos modos

def eliminar_Ticket(codigo,motivo,id_usuario):
    try:
        conexion = get_db_connection()
        if not conexion or not conexion.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return {"Mensaje":"No se pudo conectar a la base de datos"}

        cursor = conexion.cursor()
        print("¡Se conectó con éxito!")

        # Aquí se ejecutara el procedimiento almacenado
        resultado= cursor.callproc('eliminar_ticket', [codigo,motivo,id_usuario,"",""])
        conexion.commit()

        print(resultado)
        codigo, motivo,estatus,mensaje=resultado[0],resultado[1],resultado[3],resultado[4]

        


        return{"Estado": estatus, "Mensaje": mensaje, "codigo":codigo,"Motivo":motivo}

    except Exception as e:
        print(f"Error: {e}")
        return {"Error":{e}}

    finally:
        try:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
        except:
            pass  # Si falla aquí, cerramos de todos modos

def dar_reporte(fecha_inicial,fecha_final,id_usuario):
    try:
        conexion = get_db_connection()
        if not conexion or not conexion.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return {"Mensaje":"No se pudo conectar a la base de datos"}

        cursor = conexion.cursor()
        print("¡Se conectó con éxito!")

        # Aquí se ejecutara el procedimiento almacenado
        cursor.callproc('obtener_tickets_por_fechas', [fecha_inicial,fecha_final,id_usuario])

        for resultado in cursor.stored_results():
            rows= resultado.fetchall()
            return(rows)

    except Exception as e:
        print(f"Error: {e}")
        return {"Error":{e}}

    finally:
        try:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
        except:
            pass  # Si falla aquí, cerramos de todos modos

def add_usuario(usuario,contrasena,nombre,usuario_id,tipo):
    try:
        conexion = get_db_connection()
        if not conexion or not conexion.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return {"Mensaje":"No se pudo conectar a la base de datos"}

        cursor = conexion.cursor()
        print("¡Se conectó con éxito!")

        # Aquí se ejecutara el procedimiento almacenado
        cursor.callproc('CrearUsuario', [usuario,contrasena,nombre,usuario_id,tipo])
        resultados = []

        for result in cursor.stored_results():
            resultados.extend(result.fetchall())

        conexion.commit()
        return {"Mensaje": resultados[0][0] if resultados else "Sin mensaje"}

    except Exception as e:
        print(f"Error: {e}")
        return {"Error":{e}}

    finally:
        try:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
        except:
            pass  # Si falla aquí, cerramos de todos modos

def validacion_loggin(usuario, contrasena):
    try:
        conexion = get_db_connection()
        if not conexion or not conexion.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return {"Mensaje":"No se pudo conectar a la base de datos"}

        cursor = conexion.cursor()
        print("¡Se conectó con éxito!")

        # Aquí se ejecutara el procedimiento almacenado
        resulatdo= cursor.callproc('validar_login', [usuario,contrasena,0,"",False])
        usuario, id_usuario,rol,valido=resulatdo[0], resulatdo[2],resulatdo[3],resulatdo[4] 


        print(usuario, id_usuario,rol,valido)

        return{"usuario":usuario,"id_usuario": id_usuario,"rol":rol,"valido":valido}

    except Exception as e:
        print(f"Error: {e}")
        return {"Error":{e}}

    finally:
        try:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
        except:
            pass  # Si falla aquí, cerramos de todos modos

def check_precio_extravio(placa):
    try:
        conexion = get_db_connection()
        if not conexion or not conexion.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return {"Mensaje":"No se pudo conectar a la base de datos"}

        cursor = conexion.cursor()
        print("¡Se conectó con éxito!")

        # Aquí se ejecutara el procedimiento almacenado
        resulatdo= cursor.callproc('calcular_ticket_extravio_por_placa', [placa,"","","",0])
        codigo,estatus,mensaje,precio =resulatdo[1], resulatdo[2],resulatdo[3],resulatdo[4] 


        return{"Codigo":codigo,"Estado": estatus,"Mensaje":mensaje,"Precio":precio}

    except Exception as e:
        print(f"Error: {e}")
        return {"Error":{e}}

    finally:
        try:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
        except:
            pass  # Si falla aquí, cerramos de todos modos
    
def Precio_pension(tipo_cliente,tipo,vehiculo):
    try:
        conexion = get_db_connection()
        if not conexion or not conexion.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return {"Mensaje":"No se pudo conectar a la base de datos"}

        cursor = conexion.cursor()
        print("¡Se conectó con éxito!")

        # Aquí se ejecutara el procedimiento almacenado
        resulatdo= cursor.callproc('obtener_precio_pension', [tipo_cliente,tipo,vehiculo,""])
        precio= resulatdo[3]


        return{"Precio":precio}

    except Exception as e:
        print(f"Error: {e}")
        return {"Error":{e}}

    finally:
        try:
            if conexion.is_connected():
                cursor.close()
                conexion.close()
        except:
            pass  # Si falla aquí, cerramos de todos modos
    


###Imprecion de Ticket 3 Funciones

def generar_imagen_ticket(codigo):
    # Generar código de barras en memoria
    barcode = Code128(codigo, writer=ImageWriter())
    buffer = BytesIO()
    barcode.write(buffer, {'module_height': 10.0, 'module_width': 0.2})  # Ajusta tamaño aquí
    buffer.seek(0)
    img_barcode = Image.open(buffer)

    ancho = max(200, img_barcode.width)

    try:
        font = ImageFont.truetype("arial.ttf", 16)
        font_small = ImageFont.truetype("arial.ttf", 12)
    except:
        font = ImageFont.load_default()
        font_small = font

    texto_aviso = (
        "Aviso importante:\n"
        "Al ingresar al estacionamiento, usted acepta que el establecimiento no se hace responsable\n"
        "por daños, pérdidas, robos o cualquier otro perjuicio que pueda sufrir el vehículo o sus pertenencias\n"
        "mientras se encuentre dentro de las instalaciones.\n"
        "La custodia y cuidado del vehículo es responsabilidad exclusiva del propietario.\n"
        "Se recomienda asegurar adecuadamente el vehículo y no dejar objetos de valor a la vista.\n"
        "En caso de extravío del ticket, se aplicará una tarifa adicional conforme a las políticas del establecimiento.\n"
        "Al utilizar este servicio, usted reconoce y acepta estas condiciones, liberando al establecimiento de cualquier\n"
        "responsabilidad derivada del uso del estacionamiento."
    )

    # Espaciados
    espacio_linea = 18  # altura por línea para texto pequeño
    espacio_encabezado = 30  # espacio entre líneas del encabezado
    margen_entre_secciones = 20  # espacio vertical entre secciones

    dummy_img = Image.new('RGB', (1, 1))
    dummy_draw = ImageDraw.Draw(dummy_img)
    line_heights = []
    for line in texto_aviso.split('\n'):
        bbox = dummy_draw.textbbox((0, 0), line, font=font_small)
        line_heights.append(bbox[3] - bbox[1])
    line_height = max(line_heights) + 3
    num_lineas = len(line_heights)
    texto_height = espacio_linea * num_lineas

    # Calcular altura total de la imagen
    alto = (
        espacio_encabezado * 2 +  # para las 2 líneas del encabezado
        espacio_linea +            # para la fecha
        margen_entre_secciones +
        texto_height +
        margen_entre_secciones +
        img_barcode.height +
        20                        # margen inferior
    )

    img = Image.new('RGB', (ancho, alto), 'white')
    draw = ImageDraw.Draw(img)

    # Escribir encabezado con espacios
    y = 10
    draw.text((10, y), "Estacionamiento Hidalgo", font=font, fill='black')
    y += espacio_encabezado
    draw.text((10, y), "Hidalgo 54, Barrio de Santiaguito, 36588 Irapuato, Gto.", font=font_small, fill='black')
    y += espacio_linea
    # Fecha
    fecha_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    draw.text((10, y), f"Hora entrada: {fecha_hora}", font=font_small, fill='black')
    y += margen_entre_secciones

    # Texto legal línea a línea
    for line in texto_aviso.split('\n'):
        draw.text((10, y), line, font=font_small, fill='black')
        y += espacio_linea

    y += margen_entre_secciones

    # Código de barras centrado
    x_bar = (ancho - img_barcode.width) // 2
    img.paste(img_barcode, (x_bar, y))

    return img

def imprimir_imagen(img, nombre_impresora=None):
    if nombre_impresora is None:
        nombre_impresora = win32print.GetDefaultPrinter()

    hdc = win32ui.CreateDC()
    hdc.CreatePrinterDC(nombre_impresora)

    printable_area = hdc.GetDeviceCaps(8), hdc.GetDeviceCaps(10)
    printer_size = hdc.GetDeviceCaps(110), hdc.GetDeviceCaps(111)

    dib = ImageWin.Dib(img)

    ratios = [1.0 * printable_area[0] / img.width,
              1.0 * printable_area[1] / img.height]

    scale = min(ratios) * 0.9  # Escala más grande para no cortar

    scaled_width, scaled_height = int(img.width * scale), int(img.height * scale)
    x1 = int((printer_size[0] - scaled_width) / 2)
    y1 = int((printer_size[1] - scaled_height) / 2)
    x2 = x1 + scaled_width
    y2 = y1 + scaled_height

    hdc.StartDoc("Ticket Estacionamiento")
    hdc.StartPage()
    dib.draw(hdc.GetHandleOutput(), (x1, y1, x2, y2))
    hdc.EndPage()
    hdc.EndDoc()
    hdc.DeleteDC()

def imprimir_ticket(codigo, nombre_impresora=None):
    img = generar_imagen_ticket(codigo)
    imprimir_imagen(img, nombre_impresora)


def reporteExcel(datos, nombre_archivo,destinatario):
    columnas = ["id_ticket", "codigo_unico", "id_vehiculo", "tipo_cliente",
                "hora_entrada", "hora_salida", "precio", "estatus"]
    
    # Crear DataFrame
    df = pd.DataFrame(datos, columns=columnas)
    
    # Obtener ruta del escritorio del usuario
    escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
    ruta_completa = os.path.join(escritorio, nombre_archivo)
    
    # Guardar en Excel
    df.to_excel(ruta_completa, index=False)
    
    print(f"✅ Archivo guardado en: {ruta_completa}")

    remitente = "omarsaidmagallon1495@gmail.com"
    contraseña = "oxezdcdzzzpzmbbq"  # contraseña de aplicación, no la normal
    asunto = "Reporte de Tickets"
    cuerpo = "Hola, adjunto te envío el reporte en Excel."

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje["From"] = remitente
    mensaje["To"] = destinatario
    mensaje["Subject"] = asunto
    mensaje.attach(MIMEText(cuerpo, "plain"))

    # Adjuntar archivo
    with open(ruta_completa, "rb") as adjunto:
        parte = MIMEBase("application", "octet-stream")
        parte.set_payload(adjunto.read())
        encoders.encode_base64(parte)
        parte.add_header("Content-Disposition", f"attachment; filename={nombre_archivo}")
        mensaje.attach(parte)

    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(remitente, contraseña)
        servidor.sendmail(remitente, destinatario, mensaje.as_string())
        servidor.quit()
        print("📧 Correo enviado exitosamente.")
    except Exception as e:
        print(f"❌ Error al enviar correo: {e}")



def autosActivos():
    try:
        conexion = get_db_connection()
        if not conexion or not conexion.is_connected():
            print("No se pudo establecer conexión con la base de datos.")
            return {"Mensaje": "No se pudo conectar a la base de datos"}

        cursor = conexion.cursor()
        print("¡Se conectó con éxito!")

        # Ejecutar el procedimiento almacenado
        cursor.callproc('ObtenerTicketsAbiertos')

        rows = []
        for resultado in cursor.stored_results():
            rows = resultado.fetchall()  # Guardamos todos los resultados

        return rows

    except Exception as e:
        print(f"Error: {e}")
        return {"Error": str(e)}

    finally:
        if conexion and conexion.is_connected():
            cursor.close()
            conexion.close()