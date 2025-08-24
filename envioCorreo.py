
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_pdf(file_name, nombreCliente, codigoCliente, isbnPrestado, numEjemplarPrestado, fechaPrestamo, fechaLimite):
    c = canvas.Canvas(file_name, pagesize=letter)
    
    logo_path = "logo.png"  # Ruta a la imagen del logo
    c.drawImage(logo_path, x=370, y=670, width=100, height=100)

    logo_path_right = "logo2.png"  # Ruta a la imagen del logo
    c.drawImage(logo_path_right, x=100, y=670, width=100, height=100)

    # Agregar un marco alrededor del texto
    width, height = letter
    c.setStrokeColorRGB(0, 0, 0)  # Color del marco (negro)
    c.rect(100, 440, width - 240, 330, stroke=1, fill=0)
    
    # Formato del texto
    c.setFont("Times-Roman", 12)  # Fuente y tamaño del texto
    
    # Agregar texto al PDF con formato
    c.drawString(200, 720, "BIBLIOTECA VIRTUAL : AVISO")
    c.drawString(130, 660, "Nombre: " + str(nombreCliente))
    c.drawString(130, 630, "Codigo: " + str(codigoCliente))
    c.drawString(130, 600, "ISBN: " + str(isbnPrestado))
    c.drawString(130, 570, "Numero ejemplar: " + str(numEjemplarPrestado))
    c.drawString(130, 540, "Fecha del prestamo: " + str(fechaPrestamo))
    c.drawString(130, 510, "Fecha limite de entrega: " + str(fechaLimite))
    
    c.save()

def enviar_mensaje_fecha_limite(nombre_cliente,codigo_cliente,correo_cliente,isbn,ejemplar,fecha_prestamo,fecha_limite):
    # Variables
    recipient = correo_cliente
    subject = 'Fecha limite de entrega del libro prestado'
    body = 'Adjunto encontrará un PDF con información.'
    nombreCliente = nombre_cliente
    codigoCliente = codigo_cliente
    isbnPrestado = isbn
    numEjemplarPrestado = ejemplar
    fechaPrestamo = fecha_prestamo
    fechaLimite = fecha_limite
    pdf_file = 'fecha_limite.pdf'

    # Crear el archivo PDF
    create_pdf(pdf_file, nombreCliente, codigoCliente, isbnPrestado, numEjemplarPrestado, fechaPrestamo, fechaLimite)

    # Crear el mensaje de correo electrónico
    message = MIMEMultipart()
    message['From'] = 'Biblioteca Virtual'
    message['To'] = recipient
    message['Subject'] = subject

    # Cuerpo del mensaje
    message.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo PDF
    with open(pdf_file, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {pdf_file}')
        message.attach(part)

    # Conectar al servidor SMTP y enviar el correo electrónico
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('bibliotecavirtualgratuitaudg@gmail.com', 'rret tyno ibrl ztro')
        server.send_message(message)

#-------------------------------------------------------------------------------------------------------------

def create_pdf_notificacion(file_name, nombreCliente, codigoCliente, isbnPrestado, numEjemplarPrestado, fechaPrestamo, fechaLimite):
    c = canvas.Canvas(file_name, pagesize=letter)
    
    logo_path = "logo.png"  # Ruta a la imagen del logo
    c.drawImage(logo_path, x=370, y=670, width=100, height=100)

    logo_path_right = "logo2.png"  # Ruta a la imagen del logo
    c.drawImage(logo_path_right, x=100, y=670, width=100, height=100)

    # Agregar un marco alrededor del texto
    width, height = letter
    c.setStrokeColorRGB(0, 0, 0)  # Color del marco (negro)
    c.rect(100, 440, width - 240, 330, stroke=1, fill=0)
    
    # Formato del texto
    c.setFont("Times-Roman", 12)  # Fuente y tamaño del texto
    
    # Agregar texto al PDF con formato
    c.drawString(200, 720, "BIBLIOTECA VIRTUAL : AVISO")
    c.drawString(130, 660, "Nombre: " + str(nombreCliente))
    c.drawString(130, 630, "Codigo: " + str(codigoCliente))
    c.drawString(130, 600, "ISBN: " + str(isbnPrestado))
    c.drawString(130, 570, "Numero ejemplar: " + str(numEjemplarPrestado))
    c.drawString(130, 540, "Fecha del prestamo: " + str(fechaPrestamo))
    c.drawString(130, 510, "Fecha limite de entrega: " + str(fechaLimite))
    
    c.save()

def enviar_mensaje_notifiacion(nombre_cliente,codigo_cliente,correo_cliente,isbn,ejemplar,fecha_prestamo,fecha_limite):
    # Variables
    recipient = correo_cliente
    subject = '¡¡ La fecha limite de entrega esta proxima !!'
    body = 'Se le notifica que su periodo de prestamo esta apunto de expirar, de no realizarse la entrega del libro en tiempo y forma, se le aplicara una multa de 5 pesos por cada dia de atraso.'
    nombreCliente = nombre_cliente
    codigoCliente = codigo_cliente
    isbnPrestado = isbn
    numEjemplarPrestado = ejemplar
    fechaPrestamo = fecha_prestamo
    fechaLimite = fecha_limite
    pdf_file = 'notificacion.pdf'

    # Crear el archivo PDF
    create_pdf_notificacion(pdf_file, nombreCliente, codigoCliente, isbnPrestado, numEjemplarPrestado, fechaPrestamo, fechaLimite)

    # Crear el mensaje de correo electrónico
    message = MIMEMultipart()
    message['From'] = 'Biblioteca Virtual'
    message['To'] = recipient
    message['Subject'] = subject

    # Cuerpo del mensaje
    message.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo PDF
    with open(pdf_file, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {pdf_file}')
        message.attach(part)

    # Conectar al servidor SMTP y enviar el correo electrónico
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('bibliotecavirtualgratuitaudg@gmail.com', 'rret tyno ibrl ztro')
        server.send_message(message)
        return True

#-------------------------------------------------------------------------------------------------------------


def create_orden_de_pago(file_name, nombreCliente, codigoCliente, isbnPrestado, numEjemplarPrestado, fechaPrestamo, fechaLimite, fechaEntrega, adeudo):
    c = canvas.Canvas(file_name, pagesize=letter)
    
    logo_path = "logo.png"  # Ruta a la imagen del logo
    c.drawImage(logo_path, x=370, y=670, width=100, height=100)

    # Agregar un marco alrededor del texto
    width, height = letter
    c.setStrokeColorRGB(0, 0, 0)  # Color del marco (negro)
    c.rect(100, 340, width - 240, 430, stroke=1, fill=0)
    
    # Formato del texto
    c.setFont("Times-Roman", 12)  # Fuente y tamaño del texto
    
    # Agregar texto al PDF con formato
    c.drawString(200, 720, "BIBLIOTECA VIRTUAL : FOLIO")
    c.drawString(130, 660, "Clave : 51908041805")
    c.drawString(130, 630, "Referencia: 80023442819")
    c.drawString(130, 600, "Nombre: " + str(nombreCliente))
    c.drawString(130, 570, "Codigo: " + str(codigoCliente))
    c.drawString(130, 540, "ISBN: " + str(isbnPrestado))
    c.drawString(130, 510, "Numero ejemplar: " + str(numEjemplarPrestado))
    c.drawString(130, 480, "Fecha del prestamo: " + str(fechaPrestamo))
    c.drawString(130, 450, "Fecha limite de entrega: " + str(fechaLimite))
    c.drawString(130, 420, "Fecha de entrega: " + str(fechaEntrega))
    c.drawString(130, 390, "Monto a depositar: $" + str(adeudo))
    
    c.save()

def enviar_mensaje_multa(nombre_cliente,codigo_cliente,correo_cliente,isbn,ejemplar,fecha_prestamo,fecha_limite, fecha_entrega, multa):
    # Variables
    recipient = correo_cliente
    subject = 'Multa aplicada por entrega atrasada'
    body = 'Se le notifica que excedio el limite del tiempo asignado para su prestamos, por lo que se le aplico una multa la cual debera de pagar por medio de un deposito, podra apoyarse de la siguiente orden de pago.'
    nombreCliente = nombre_cliente
    codigoCliente = codigo_cliente
    isbnPrestado = isbn
    numEjemplarPrestado = ejemplar
    fechaPrestamo = fecha_prestamo
    fechaLimite = fecha_limite
    fechaEntrega = fecha_entrega
    adeudo = multa
    pdf_file = 'orden_de_pago.pdf'

    # Crear el archivo PDF
    create_orden_de_pago(pdf_file, nombreCliente, codigoCliente, isbnPrestado, numEjemplarPrestado, fechaPrestamo, fechaLimite, fechaEntrega, adeudo)

    # Crear el mensaje de correo electrónico
    message = MIMEMultipart()
    message['From'] = 'Biblioteca Virtual'
    message['To'] = recipient
    message['Subject'] = subject

    # Cuerpo del mensaje
    message.attach(MIMEText(body, 'plain'))

    # Adjuntar el archivo PDF
    with open(pdf_file, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {pdf_file}')
        message.attach(part)

    # Conectar al servidor SMTP y enviar el correo electrónico
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('bibliotecavirtualgratuitaudg@gmail.com', 'rret tyno ibrl ztro')
        server.send_message(message)
        return True
