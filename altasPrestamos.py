#Universidad de Guadalajara.
#Centro Universitario de Ciencias Exactas e Ingenierías.
#División de tecnologías para la integración ciber-humana.
#Departamento de ciencias computacionales.
#Proyecto final: Biblioteca virtual
#Equipo #1: Integrantes
#Alonso Lomelí Diego Alejandro.
#Arechiga Rojas Roman Antonio.
#Bailón Badillo Emmanuel.
#Caro Flores Christopher Tristán.
#M.A: Bases de datos. Sección: D03
#Calendario: lunes y miércoles (1100-1255)
#Nombre del profesor: Mariscal Lugo Luis Felipe

import tkinter as tk
from elementos import LabelEntryFrame,BotonText,ComboboxPrestamos,SeleccionadorFecha
from tkinter import messagebox
from conectar import obtener_numero_ejemplar,obtener_correo_cliente,registrar_prestamo,enviar_notificacion
from datetime import timedelta

def validarSiEsVacio(dato,nombreCampo):
    if not dato:
        messagebox.showerror("Error", "Por favor, llene el campo de " + nombreCampo)
        return True

def registrar(checkbox_var,entradaCodigoAlumno,entradaCodigoProfesor,entradaCorreoCliente,entradaCodigoIsbn,entradaEjemplaresDisponibles,entradaFechaPrestamo,entradaFechaLimite):
    campo = ['codigo del cliente', 'isbn del libro', 'numero del ejemplar', 'fecha del prestamo']
    if checkbox_var.get() == 1:
        codigo_cliente = entradaCodigoProfesor.get_combobox()
    else:
        codigo_cliente = entradaCodigoAlumno.get_combobox()

    if validarSiEsVacio(codigo_cliente,campo[0]):
        return
    
    entradaCorreoCliente.habilitar()
    correo_cliente = entradaCorreoCliente.get_entry()
    entradaCorreoCliente.deshabilitar()

    isbn = entradaCodigoIsbn.get_combobox()
    if validarSiEsVacio(isbn,campo[1]):
        return
    
    ejemplar = entradaEjemplaresDisponibles.get_combobox()
    if validarSiEsVacio(ejemplar,campo[2]):
        return
    
    fecha_prestamo_sinFormato = entradaFechaPrestamo.get_fecha()
    if validarSiEsVacio(fecha_prestamo_sinFormato,campo[3]):
        return
    fecha_prestamo = fecha_prestamo_sinFormato.strftime("%Y/%m/%d")

    entradaFechaLimite.habilitar()
    fecha_limite_sinFormato = entradaFechaLimite.get_fecha()
    fecha_limite = fecha_limite_sinFormato.strftime("%Y/%m/%d")
    entradaFechaLimite.deshabilitar()

    if registrar_prestamo(codigo_cliente,correo_cliente,isbn,ejemplar,fecha_prestamo,fecha_limite) == True:
        limpiarEntry(entradaCodigoAlumno,entradaCodigoProfesor,entradaCorreoCliente,entradaCodigoIsbn,entradaEjemplaresDisponibles)
        fecha_notificacion = encontrar_fecha_notificacion(entradaFechaLimite)
        #datos_notificacion(fecha_notificacion,codigo_cliente, correo_cliente, isbn, ejemplar, fecha_prestamo, fecha_limite)


def limpiarEntry(entradaCodigoAlumno,entradaCodigoProfesor,entradaCorreoCliente,entradaCodigoIsbn,entradaEjemplaresDisponibles):
    entradaCorreoCliente.habilitar()

    entradaCodigoAlumno.limpiar_combo()
    entradaCodigoProfesor.limpiar_combo()
    entradaCorreoCliente.limpiar_entry()
    entradaCodigoIsbn.limpiar_combo()
    entradaEjemplaresDisponibles.limpiar_combo()

    entradaCorreoCliente.deshabilitar()

def crearInterfazAltasPrestamos(root):
    interfaz_altas_prestamos = tk.Toplevel(root)
    interfaz_altas_prestamos.geometry("350x500+550+100")
    interfaz_altas_prestamos.resizable(False, False) 
    interfaz_altas_prestamos.title("Altas de prestamos")
    return interfaz_altas_prestamos

def toggle_checkbox(checkbox_var,entradaCodigoAlumno,entradaCodigoProfesor,entradaCorreoCliente):
    if checkbox_var.get() == 1:
        # Si el checkbox está marcado, deshabilita el Entry
        entradaCorreoCliente.habilitar()
        entradaCorreoCliente.limpiar_entry()
        entradaCorreoCliente.deshabilitar()

        entradaCodigoProfesor.enabled_combo()
        entradaCodigoAlumno.limpiar_combo()
        entradaCodigoAlumno.disabled_combo()
    else:
        # Si el checkbox no está marcado, habilita el Entry
        entradaCorreoCliente.habilitar()
        entradaCorreoCliente.limpiar_entry()
        entradaCorreoCliente.deshabilitar()
        
        entradaCodigoProfesor.limpiar_combo()
        entradaCodigoProfesor.disabled_combo()
        entradaCodigoAlumno.enabled_combo()

def toggle_checkbox_automatic_date(checkbox_var_automatic_date,entradaFechaPrestamo):
    if checkbox_var_automatic_date.get() == 1:
        # Si el checkbox está marcado, deshabilita el Entry
        entradaFechaPrestamo.habilitar()
    else:
        # Si el checkbox no está marcado, habilita el Entry
        entradaFechaPrestamo.deshabilitar()

def on_combobox_cliente_selected(event,entradaCodigoCliente,entradaCorreoCliente,tabla):
    codigoIngresado = entradaCodigoCliente.get_combobox()
    correoCliente = obtener_correo_cliente(codigoIngresado,tabla)
    entradaCorreoCliente.habilitar()
    entradaCorreoCliente.limpiar_entry()
    entradaCorreoCliente.insert_entry(correoCliente)
    entradaCorreoCliente.deshabilitar()

def on_combobox_selected(event,entradaCodigoIsbn,entradaEjemplaresDisponibles):
    seleccion = entradaCodigoIsbn.get_combobox()
    ejemplares_disponibles = obtener_numero_ejemplar(seleccion)
    entradaEjemplaresDisponibles.combo['values'] = ejemplares_disponibles

def encontrar_fecha_limite(event,entradaFechaPrestamo,entradaFechaLimite):
    fechaPrestamo = entradaFechaPrestamo.get_fecha()
    fecha_futura = fechaPrestamo + timedelta(days=7)
    fecha_formateada = fecha_futura.strftime("%m/%d/%y")
    entradaFechaLimite.habilitar()
    #entradaFechaLimite.limpiar_entry()
    entradaFechaLimite.set_fecha(fecha_formateada)
    entradaFechaLimite.deshabilitar()

def encontrar_fecha_notificacion(entradaFechaLimite):
    fechaLimite = entradaFechaLimite.get_fecha()
    fecha_notificacion = fechaLimite - timedelta(days=1)
    fecha_notificacion_formateada = fecha_notificacion.strftime("%m/%d/%y")
    #print (fecha_notificacion_formateada)
    return fecha_notificacion_formateada

def mostrarRegistroPrestamos(interfaz_altas_prestamos, menu_principal):
    checkbox_var = tk.IntVar()

    # Crear el Checkbutton
    checkbox = tk.Checkbutton(interfaz_altas_prestamos, text="PROFESOR", variable=checkbox_var, command=lambda: toggle_checkbox(checkbox_var,entradaCodigoAlumno,entradaCodigoProfesor, entradaCorreoCliente))
    checkbox.grid(row=0,column=0,pady=10)

    entradaCodigoAlumno = ComboboxPrestamos(interfaz_altas_prestamos, "Codigo alumno:", "alumno", "codigo", 17, None)
    entradaCodigoAlumno.grid(row=1,column=0,pady=10, sticky=tk.W)

    entradaCodigoProfesor = ComboboxPrestamos(interfaz_altas_prestamos, "Codigo profesor:", "profesor", "codigo", 17, None)
    entradaCodigoProfesor.grid(row=2,column=0,pady=10, sticky=tk.W)
    entradaCodigoProfesor.disabled_combo()

    entradaCorreoCliente = LabelEntryFrame(interfaz_altas_prestamos, "Correo:", 20, 15)
    entradaCorreoCliente.grid(row=3,column=0,pady=10, sticky=tk.W)
    entradaCorreoCliente.deshabilitar()

    entradaCodigoAlumno.combo.bind("<<ComboboxSelected>>",lambda event: on_combobox_cliente_selected(event,entradaCodigoAlumno,entradaCorreoCliente,"alumno"))
    entradaCodigoProfesor.combo.bind("<<ComboboxSelected>>",lambda event: on_combobox_cliente_selected(event,entradaCodigoProfesor,entradaCorreoCliente,"profesor"))

    entradaCodigoIsbn = ComboboxPrestamos(interfaz_altas_prestamos, "ISBN:", "libro", "isbn", 17, None)
    entradaCodigoIsbn.grid(row=4,column=0,pady=10, sticky=tk.W)

    entradaCodigoIsbn.combo.bind("<<ComboboxSelected>>",lambda event: on_combobox_selected(event,entradaCodigoIsbn,entradaEjemplaresDisponibles))

    entradaEjemplaresDisponibles = ComboboxPrestamos(interfaz_altas_prestamos, "Ejemplares:", "libro", "ejemplar", 17, None, show_disponibles=True)
    entradaEjemplaresDisponibles.grid(row=5,column=0,pady=10, sticky=tk.W)

    checkbox_var_automatic_date = tk.IntVar()

    # Crear el Checkbutton
    checkbox_automatic_date = tk.Checkbutton(interfaz_altas_prestamos, text="MANUAL", variable=checkbox_var_automatic_date, command=lambda: toggle_checkbox_automatic_date(checkbox_var_automatic_date,entradaFechaPrestamo))
    checkbox_automatic_date.grid(row=6,column=0,pady=10)

    entradaFechaPrestamo = SeleccionadorFecha(interfaz_altas_prestamos, "Fecha prestamo:", 17)
    entradaFechaPrestamo.grid(row=7,column=0,pady=10, sticky=tk.W)
    entradaFechaPrestamo.deshabilitar()

    entradaFechaPrestamo.cal.bind("<<DateEntrySelected>>", lambda event: encontrar_fecha_limite(event, entradaFechaPrestamo, entradaFechaLimite))
    #Activar cambio de fecha limite 

    entradaFechaLimite = SeleccionadorFecha(interfaz_altas_prestamos, "Fecha limite:", 17)
    entradaFechaLimite.grid(row=8,column=0,pady=10, sticky=tk.W)
    entradaFechaLimite.deshabilitar()

    interfaz_altas_prestamos.bind("<Map>",lambda event: encontrar_fecha_limite(event, entradaFechaPrestamo, entradaFechaLimite))

    buttonAceptar = BotonText(interfaz_altas_prestamos, "Aceptar", 6, command=lambda: registrar(checkbox_var,entradaCodigoAlumno,entradaCodigoProfesor,entradaCorreoCliente,entradaCodigoIsbn,entradaEjemplaresDisponibles,entradaFechaPrestamo,entradaFechaLimite))
    buttonAceptar.place(x=120, y=455)

    buttonCancelar = BotonText(interfaz_altas_prestamos, "Salir", 6, command=lambda:cancelar(interfaz_altas_prestamos,menu_principal))
    buttonCancelar.place(x=245, y=455)
    enviar_notificacion()
    
def accederInterfazPrestamos(root):
    interfaz_altas_prestamos = crearInterfazAltasPrestamos(root)
    root.withdraw()
    mostrarRegistroPrestamos(interfaz_altas_prestamos,root)

def cancelar(root, menu_principal):
    root.destroy()  # Destruye la ventana actual
    menu_principal.deiconify()  # Muestra la ventana del menú principal

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300") 
    root.title("Registro de profesores")
    accederInterfazPrestamos(root)
    root.mainloop()