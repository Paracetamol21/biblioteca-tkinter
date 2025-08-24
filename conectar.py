import psycopg2     #Extension de python para conectar con postgresql
from tkinter import messagebox
from envioCorreo import enviar_mensaje_notifiacion, enviar_mensaje_multa
import datetime
from datetime import timedelta

def establecer_conexion():
    try:
        conexion = psycopg2.connect(#Usamos el metodo de psycopg2 y le pasamos los parametros necesarios
            user="postgres",                #Primer parametro: Nuestro usuario de postgrsql
            password="ADMIN",   #Segundo parametro: Contraseña de nuestro server
            host="127.0.0.1",               #Tercer parametro: Host de nuestro server
            port="5432",                    #Cuarto parametro: Puerto de nuestro server
            database="biblioteca"           #Quinto parametro: Nombre de la base de datos
        )
        return conexion
    except (Exception, psycopg2.Error):     #Exception por si la conexion falla
        messagebox.showerror("Error de conexión", "No se pudo conectar a la base de datos.") #Notifica error

def validar_credenciales(nombre, contraseña):
    conexion = establecer_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()

            # Consultar la base de datos para verificar las credenciales
            cursor.execute("SELECT privilegio FROM usuario WHERE nombre = %s AND contraseña = %s", (nombre, contraseña))
            resultado = cursor.fetchone()

            if resultado:
                messagebox.showinfo("Succesful", "Acceso exitoso")
                # Obtener el tipo de privilegio
                tipo_privilegio = resultado[0]  # El tipo de privilegio estará en el primer elemento de la tupla
                cursor.close()
                conexion.close()
                return tipo_privilegio  # Devolver el tipo de privilegio si se desea
            else:
                messagebox.showwarning("Credenciales inválidas", "Acceso denegado")

            cursor.close()
            conexion.close()
        except (Exception, psycopg2.Error):
            messagebox.showerror("Error", "Algo salió mal.")
    return False  # Devolver False si las credenciales no son válidas


def registrar_alumnos(codigo, nombre, carrera, correo):
    conexion = establecer_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO alumno(codigo, nombre, carrera, correo) VALUES (%s, %s, %s, %s)", (codigo, nombre, carrera, correo))
            conexion.commit()  # Confirmar la operación de inserción
            messagebox.showinfo("Succesful", "Registro exitoso")
            return True
        except (Exception, psycopg2.Error) as error:
            messagebox.showwarning("Unsuccessful", "Registro fracaso")
            print("Error al registrar alumno:", error)
            return False
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()


def consultar_alumnos(tabla):
    conexion = establecer_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT codigo,nombre,carrera,correo,adeudo FROM alumno")
            datos = cursor.fetchall()

            cursor.close()
            conexion.close()
    # Mostrar los datos en la tabla
            for i, fila in enumerate(datos, start=1):
                tabla.insert("", "end", text=str(i), values=fila)

            #for fila in datos:
                #tabla.insert("", "end", values=fila)

        except (Exception, psycopg2.Error) as error:
            messagebox.showwarning("Unsuccessful", "Consulta fracaso")
            print("Error al consultar alumnos: ", error)
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

def consultar_alumno_individual(tabla, entradaCodigoBusqueda):
    codigoBuscar = entradaCodigoBusqueda.get()
    conexion = establecer_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            if not codigoBuscar:
                messagebox.showwarning("Error", "Por favor ingrese el código del alumno.")
                return
            else: 
                cursor.execute("SELECT codigo, nombre, carrera, correo, adeudo FROM alumno WHERE codigo = %s", (codigoBuscar,))
                alumno = cursor.fetchone()

            cursor.close()
            conexion.close()

            tabla.delete(*tabla.get_children())  # Limpiar la tabla

            if alumno:
                tabla.insert("", "end", text=str(1), values=alumno)
            else:
                messagebox.showwarning("Error", "No se encontró ningún alumno con el código proporcionado.")
                consultar_alumnos(tabla)

        except Exception as error:
            messagebox.showwarning("Error", "Error al consultar el alumno.")
            print("Error al consultar el alumno:", error)
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

def registrar_profesor(codigo, nombre, carrera, correo):
    conexion = establecer_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO profesor(codigo, nombre, carrera, correo) VALUES (%s, %s, %s, %s)", (codigo, nombre, carrera, correo))
            conexion.commit()  # Confirmar la operación de inserción
            messagebox.showinfo("Succesful", "Registro exitoso")
            return True
        except (Exception, psycopg2.Error) as error:
            messagebox.showwarning("Unsuccessful", "Registro fracaso")
            print("Error al registrar profesor:", error)
            return False
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

def consultar_profesores(tabla):
    conexion = establecer_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT codigo,nombre,carrera,correo,adeudo FROM profesor")
            datos = cursor.fetchall()

            cursor.close()
            conexion.close()
    # Mostrar los datos en la tabla
            for i, fila in enumerate(datos, start=1):
                tabla.insert("", "end", text=str(i), values=fila)

            #for fila in datos:
                #tabla.insert("", "end", values=fila)

        except (Exception, psycopg2.Error) as error:
            messagebox.showwarning("Unsuccessful", "Consulta fracaso")
            print("Error al registrar profesor:", error)
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

def consultar_profesor_individual(tabla, entradaCodigoProfesor):
    codigoProfesorBuscar = entradaCodigoProfesor.get()
    conexion = establecer_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            if not codigoProfesorBuscar:
                messagebox.showwarning("Error", "Por favor ingrese el código del alumno.")
                return
            else: 
                cursor.execute("SELECT codigo, nombre, carrera, correo, adeudo FROM profesor WHERE codigo = %s", (codigoProfesorBuscar,))
                profesor = cursor.fetchone()

            cursor.close()
            conexion.close()

            tabla.delete(*tabla.get_children())  # Limpiar la tabla

            if profesor:
                tabla.insert("", "end", text=str(1), values=profesor)
            else:
                messagebox.showwarning("Error", "No se encontró ningún profesor con el código proporcionado.")
                consultar_profesores(tabla)

        except Exception as error:
            messagebox.showwarning("Error", "Error al consultar el profesor.")
            print("Error al consultar el profesor:", error)
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

def registrar_libro(isbn, titulo, autor, editorial, año_public, ejemplar, estado):
    ejemplar = int(ejemplar) + 1
    conexion = establecer_conexion()
    repetido = False
    fallidos = 0
    if conexion:
        try:
            cursor = conexion.cursor()
            # Verificar si la tupla ya existe en la base de datos
            # Si la tupla no existe, procede con la inserción
            for i in range(1, ejemplar):
                exitosos = int(i)
                numEjemplar = str(i) + " / " + str(isbn)
                cursor.execute("SELECT * FROM libro WHERE isbn = %s AND titulo = %s AND autor = %s AND editorial = %s AND año_public = %s AND num_ejemplar = %s AND estado = %s", (isbn, titulo, autor, editorial, año_public, numEjemplar, estado))
                if cursor.fetchone():
                    repetido = True
                    fallidos += 1 
                    pass
                else:
                    cursor.execute("INSERT INTO libro(isbn, titulo, autor, editorial, año_public, num_ejemplar, estado) VALUES (%s, %s, %s, %s, %s, %s, %s)", (isbn, titulo, autor, editorial, año_public, numEjemplar, estado))
                    conexion.commit()  # Confirmar la operación de inserción
                    repetido = False

            if repetido == False:
                exitosos = exitosos - fallidos
                numEjemplar = str(exitosos)
                messagebox.showinfo("Succesful", "Registros exitosos: " + numEjemplar)
                return True
            else:
                messagebox.showwarning("Error", "La tupla ya existe en la base de datos.")
                return False

        except (Exception, psycopg2.Error) as error:
            messagebox.showwarning("Error", "Registro fracaso")
            print("Error al registrar libro:", error)
            return False
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

def consultar_libros(tabla):
    conexion = establecer_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT isbn, titulo, autor, editorial, año_public, num_ejemplar, estado FROM libro")
            datos = cursor.fetchall()

            cursor.close()
            conexion.close()
    # Mostrar los datos en la tabla
            for i, fila in enumerate(datos, start=1):
                tabla.insert("", "end", text=str(i), values=fila)

        except (Exception, psycopg2.Error) as error:
            messagebox.showwarning("Unsuccessful", "Consulta fracaso")
            print("Error al registrar libro:", error)
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

def consultar_libros_individual(tabla, entradaIsbnBusqueda):
    isbnBuscar = entradaIsbnBusqueda.get()
    conexion = establecer_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            if not isbnBuscar:
                messagebox.showwarning("Error", "Por favor ingrese el ISBN del libro.")
                return
            else: 
                cursor.execute("SELECT isbn, titulo, autor, editorial, año_public, num_ejemplar, estado FROM libro WHERE isbn = %s", (isbnBuscar,))
                libros = cursor.fetchall() 

            cursor.close()
            conexion.close()

            tabla.delete(*tabla.get_children())  # Limpiar la tabla

            if libros:
                for i, fila in enumerate(libros, start=1):
                    tabla.insert("", "end", text=str(i), values=fila)

            else:
                messagebox.showwarning("Error", "No se encontró ningún libro con el isbn proporcionado.")
                consultar_libros(tabla)

        except Exception as error:
            messagebox.showwarning("Error", "Error al consultar el libro.")
            print("Error al consultar el libro:", error)
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

def registrar_prestamo(codigo_cliente, correo_cliente, isbn, ejemplar, fecha_prestamo, fecha_limite):
    conexion = establecer_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) AS contador FROM prestamo WHERE codigo_cliente = %s AND fecha_entrega IS NULL", (codigo_cliente,))
            contador = cursor.fetchone()[0]  # Obtenemos el primer valor de la tupla resultante
            if int(contador) < 5:
                #REGISTRAR
                cursor.execute("INSERT INTO prestamo(codigo_cliente, correo_cliente, isbn, num_ejemplar, fecha_prestamo, fecha_limite, notificacion) VALUES (%s, %s, %s, %s, %s, %s, %s)", (codigo_cliente, correo_cliente, isbn, ejemplar, fecha_prestamo, fecha_limite, "No enviada"))
                #MARCAR COMO NO DISPONIBLE
                cursor.execute("UPDATE libro SET estado = %s WHERE isbn = %s AND num_ejemplar = %s", ("No disponible", isbn, ejemplar))
                conexion.commit()  # Confirmar la operación de inserción
                #EXTRAER NOMBRE
                messagebox.showinfo("Succesful", "Registro exitoso")
                return True
            else: 
                messagebox.showwarning("Error", "Usuario con exceso de prestamos")

        except (Exception, psycopg2.Error) as error:
            messagebox.showwarning("Unsuccessful", "Registro fracaso")
            print("Error al registrar prestamo:", error)
            return False
        
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

def consultar_prestamos(tabla):
    conexion = establecer_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id_prestamo, codigo_cliente, correo_cliente, isbn, num_ejemplar, fecha_prestamo, fecha_limite, fecha_entrega FROM prestamo")
            datos = cursor.fetchall()

            cursor.close()
            conexion.close()
    # Mostrar los datos en la tabla
            for i, fila in enumerate(datos, start=1):
                tabla.insert("", "end", text=str(i), values=fila)

            #for fila in datos:
                #tabla.insert("", "end", values=fila)

        #except (Exception, psycopg2.Error) as error:
        #    messagebox.showwarning("Unsuccessful", "Consulta fracaso")
        #    print("Error al registrar libro:", error)
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

def obtener_codigo_alumno(tabla,columna):
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    #Tomar colum

    cursor.execute(f"SELECT DISTINCT {columna} FROM {tabla}")
    #resultados = cursor.fetchall()
    resultados = [registro[0] for registro in cursor.fetchall()]
    
    cursor.close()
    conexion.close()

    return resultados

def obtener_numero_ejemplar(libro_seleccionado):
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    cursor.execute("SELECT num_ejemplar FROM libro WHERE isbn = %s and estado = %s", (libro_seleccionado,"Disponible",))
    ejemplaresDisponibles = [registro[0] for registro in cursor.fetchall()]

    cursor.close()
    conexion.close()

    return ejemplaresDisponibles

def obtener_correo_cliente(codigo,tabla):
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    cursor.execute(f"SELECT correo FROM {tabla} WHERE codigo = %s", (codigo,))
    correoCliente = cursor.fetchall()

    cursor.close()
    conexion.close()

    return correoCliente

def obtener_datos_cliente(id_prestamo, columna):
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    cursor.execute(f"SELECT {columna} FROM prestamo WHERE id_prestamo = %s", (id_prestamo,))
    datoCliente = cursor.fetchall()

    cursor.close()
    conexion.close()

    # Verificar si se encontraron datos
    if datoCliente:
        # Extraer el primer valor de la primera tupla
        primer_valor = datoCliente[0][0]
        return primer_valor
    else:
        return None  # O un valor predeterminado si no se encontraron datos

def entrega_libro(isbn,ejemplar,fecha_entrega, id_prestamo, multa, codigo_cliente):
    conexion = establecer_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("UPDATE libro SET estado = %s WHERE isbn = %s AND num_ejemplar = %s", ("Disponible", isbn, ejemplar))
            cursor.execute("UPDATE prestamo SET fecha_entrega = %s WHERE id_prestamo = %s", (fecha_entrega, id_prestamo))
            #cursor.execute("UPDATE prestamo SET fecha_entrega = %s WHERE id_prestamo = %s", (fecha_entrega, id_prestamo))

            cursor.execute("SELECT * FROM alumno WHERE adeudo IS NULL AND codigo = %s",(codigo_cliente,))
            nulo = cursor.fetchone()
            if nulo:
                cursor.execute("UPDATE alumno SET adeudo = %s WHERE codigo = %s", (multa,codigo_cliente,))
                if cursor.rowcount > 0:
                    multa_archivo = multa
                    pass
                else:
                    cursor.execute("UPDATE profesor SET adeudo = %s WHERE codigo = %s", (multa,codigo_cliente,))
                    multa_archivo = multa
                conexion.commit() 
            else:
                cursor.execute("UPDATE alumno SET adeudo = adeudo + %s WHERE codigo = %s",(multa,codigo_cliente,))
                if cursor.rowcount > 0:
                    multa_archivo = multa
                    pass
                else:
                    cursor.execute("UPDATE profesor SET adeudo = adeudo + %s WHERE codigo = %s",(multa,codigo_cliente,))
                    multa_archivo = multa
                conexion.commit()
                
                if multa_archivo != 0:
                    cursor.execute("SELECT * FROM prestamo WHERE codigo_cliente = %s AND id_prestamo = %s", (codigo_cliente,id_prestamo,))
                    datos_notificacion = cursor.fetchone()
                                
                    #codigo_cliente = datos_notificacion[1]
                    cursor.execute("SELECT nombre FROM alumno WHERE codigo = %s", (codigo_cliente,))
                    nombre_cliente_alumno = cursor.fetchone()
                    if nombre_cliente_alumno:  
                        nombre_cliente_multa = nombre_cliente_alumno[0]  # Acceder al primer elemento de la tupla
                    else:
                        cursor.execute("SELECT nombre FROM profesor WHERE codigo = %s", (codigo_cliente,))
                        nombre_cliente_profesor = cursor.fetchone()
                        nombre_cliente_multa = nombre_cliente_profesor[0]

                    codigo_cliente_multa = datos_notificacion[1]
                    correo_cliente_multa = datos_notificacion[2]
                    isbn_multa = datos_notificacion[3]
                    ejemplar_multa = datos_notificacion[4]
                    fecha_prestamo_multa = datos_notificacion[5]
                    fecha_limite_multa = datos_notificacion[6]
                    fecha_formateada = fecha_limite_multa.strftime("%d/%m/%Y")
                    fecha_entrega_multa = datos_notificacion[7]
                    fecha_entrega_formateada = fecha_entrega_multa.strftime("%d/%m/%Y")
                                    
                    if enviar_mensaje_multa(nombre_cliente_multa,codigo_cliente_multa,correo_cliente_multa,isbn_multa,ejemplar_multa,fecha_prestamo_multa,fecha_formateada,fecha_entrega_formateada,multa_archivo):
                        messagebox.showwarning("Aviso", "Multa por entrega tardia aplicada")

            cursor.close()
            conexion.close()
            messagebox.showinfo("Succesful", "Entrega exitosa")
            #enviar_mensaje_fecha_limite(nombre_cliente,codigo_cliente,correo_cliente,isbn,ejemplar,fecha_prestamo,fecha_limite)
            return True

        except (Exception, psycopg2.Error) as error:
            messagebox.showwarning("Unsuccessful", "Registro fracaso")
            print("Error al regresar prestamo:", error)
            return False
        
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()


def obtener_dato(isbn,num_ejemplar,columna,tabla):
    conexion = establecer_conexion()
    cursor = conexion.cursor()
    cursor.execute(f"SELECT {columna} FROM {tabla} WHERE isbn = %s AND num_ejemplar = %s", (isbn,num_ejemplar,))
    estado = cursor.fetchone()
    estadoEncontrado = estado[0]

    cursor.close()
    conexion.close()

    return estadoEncontrado

def enviar_notificacion():
    conexion = establecer_conexion()
    if conexion:
        try:
            fecha_actual = datetime.datetime.now() 
            posible_fecha_notificacion = fecha_actual + timedelta(days=1)
            posible_fecha_notificacion_formateada = posible_fecha_notificacion.strftime("%Y/%m/%d")
            #print(posible_fecha_notificacion_formateada)
            cursor = conexion.cursor()
            cursor.execute("SELECT*  FROM prestamo WHERE fecha_limite = %s AND fecha_entrega IS NULL AND notificacion = %s", (posible_fecha_notificacion_formateada,"No enviada",))
            datos_notificacion = cursor.fetchall()
            
            for tupla in datos_notificacion:
                codigo_cliente = tupla[1]
                cursor.execute("SELECT nombre FROM alumno WHERE codigo = %s", (codigo_cliente,))
                nombre_cliente_alumno = cursor.fetchone()
                if nombre_cliente_alumno:  
                    nombre_cliente = nombre_cliente_alumno[0]  # Acceder al primer elemento de la tupla
                else:
                    cursor.execute("SELECT nombre FROM profesor WHERE codigo = %s", (codigo_cliente,))
                    nombre_cliente_profesor = cursor.fetchone()
                    nombre_cliente = nombre_cliente_profesor[0]

                correo_cliente = tupla[2]
                isbn = tupla[3]
                ejemplar = tupla[4]
                fecha_prestamo = tupla[5]
                fecha_limite = tupla[6]
                fecha_formateada = fecha_limite.strftime("%d/%m/%Y")
                
                id_prestamo = tupla[0]
                if enviar_mensaje_notifiacion(nombre_cliente,codigo_cliente,correo_cliente,isbn,ejemplar,fecha_prestamo,fecha_formateada):
                    cursor.execute("UPDATE prestamo SET notificacion = %s WHERE id_prestamo = %s", ("Enviada", id_prestamo))
                    conexion.commit() 

        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

def consultar_prestamos_individual(tabla, entradaBusqueda):
    codigo_cliente = entradaBusqueda.get()
    conexion = establecer_conexion()
    if conexion:
        try:
            cursor = conexion.cursor()
            if not codigo_cliente:
                messagebox.showwarning("Error", "Por favor ingrese el codigo del cliente.")
                return
            else: 
                cursor.execute("SELECT id_prestamo, codigo_cliente, correo_cliente, isbn, num_ejemplar, fecha_prestamo, fecha_limite, fecha_entrega FROM prestamo WHERE codigo_cliente = %s", (codigo_cliente,))
                libros = cursor.fetchall() 

            cursor.close()
            conexion.close()

            tabla.delete(*tabla.get_children())  # Limpiar la tabla

            if libros:
                for i, fila in enumerate(libros, start=1):
                    tabla.insert("", "end", text=str(i), values=fila)

            else:
                messagebox.showwarning("Error", "No se encontró ningún cliente con el codigo proporcionado.")
                consultar_prestamos(tabla)

        except Exception as error:
            messagebox.showwarning("Error", "Error al consultar el libro.")
            print("Error al consultar el libro:", error)
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()