
import tkinter as tk
from elementos import LabelEntryFrame,BotonText,SeleccionadorFecha
from tkinter import messagebox
from conectar import obtener_datos_cliente,entrega_libro,obtener_dato,enviar_notificacion
from datetime import timedelta

def registrar(salidaCodigoIsbn,salidaEjemplaresPrestado,entradaFechaEntrega,id_prestamo,salidaFechaLimite,salidaCodigoCliente):
    codigo_cliente = salidaCodigoCliente.get_entry()    #Obtener el codigo del cliente del entry
    
    isbn = salidaCodigoIsbn.get_entry() #Obtener el ISBN del entry

    ejemplar = salidaEjemplaresPrestado.get_entry() #Obtener el numero del ejemplar del entry

    fecha_entrega_sinFormato = entradaFechaEntrega.get_fecha()  #Obtener la fecha de entrega directo del DateEntry

    fecha_entrega = fecha_entrega_sinFormato.strftime("%Y/%m/%d")   #Formatear la fecha para su almacenamiento en la base

    fecha_limite_sinFormato = salidaFechaLimite.get_fecha() #Obtener la fecha limite de entrega directo del DateEntry

    if fecha_entrega_sinFormato > fecha_limite_sinFormato:  #Verificar que la fecha de entrega sea menor a la fecha limite
        multa = verificar_entrega(fecha_entrega_sinFormato,fecha_limite_sinFormato) #Si es mayor se llama a la funcion "verificar_entrega", se le pasan los argumentos y se le asigna el valor retornado a multa
    else:
        multa = 0   #Si es menor , se le asigna valor de 0 a multa

    verificarEstado = obtener_dato(isbn,ejemplar,"estado","libro")  #Se llama a la funcion "obtener_dato" para buscar el estado del libro y se le asigna a verificarEstado

    if verificarEstado == "No disponible":  #Verificar que el estado sea "No disponible"
        if entrega_libro(isbn,ejemplar,fecha_entrega, id_prestamo, multa, codigo_cliente) == True:  #Se intenta la entrega del libro
            entradaFechaEntrega.deshabilitar()  #Asegurar que entradaFechaEntrega esta deshabilitado
    else:
        messagebox.showwarning("Error", "Libro ya fue entregado")   #Si no , se avisa que el libro ya fue entregado
    
def verificar_entrega(fecha_entrega,fecha_limite):
    atraso = fecha_entrega - fecha_limite
    dias_atraso = atraso.days
    multa = dias_atraso * 5
    return multa

def limpiarEntry(salidaCodigoCliente,salidaCorreoCliente,salidaCodigoIsbn,salidaEjemplaresPrestado,salidaFechaPrestamo,salidaFechaLimite):
    habilitar_salidas(salidaCodigoCliente,salidaCorreoCliente,salidaCodigoIsbn,salidaEjemplaresPrestado,salidaFechaPrestamo,salidaFechaLimite)

    salidaCodigoCliente.limpiar_entry()
    salidaCorreoCliente.limpiar_entry()
    salidaCodigoIsbn.limpiar_entry()
    salidaEjemplaresPrestado.limpiar_entry()

    deshabilitar_salidas(salidaCodigoCliente,salidaCorreoCliente,salidaCodigoIsbn,salidaEjemplaresPrestado,salidaFechaPrestamo,salidaFechaLimite)

def deshabilitar_salidas(salidaCodigoCliente,salidaCorreoCliente,salidaCodigoIsbn,salidaEjemplaresPrestado,salidaFechaPrestamo,salidaFechaLimite):
    salidaCodigoCliente.deshabilitar()
    salidaCorreoCliente.deshabilitar()
    salidaCodigoIsbn.deshabilitar()
    salidaEjemplaresPrestado.deshabilitar()
    salidaFechaPrestamo.deshabilitar()
    salidaFechaLimite.deshabilitar()

def habilitar_salidas(salidaCodigoCliente,salidaCorreoCliente,salidaCodigoIsbn,salidaEjemplaresPrestado,salidaFechaPrestamo,salidaFechaLimite):
    salidaCodigoCliente.habilitar()
    salidaCorreoCliente.habilitar()
    salidaCodigoIsbn.habilitar()
    salidaEjemplaresPrestado.habilitar()
    salidaFechaPrestamo.habilitar()
    salidaFechaLimite.habilitar()

def limpiarEntry(salidaCodigoCliente,salidaCorreoCliente,salidaCodigoIsbn,salidaEjemplaresPrestado,salidaFechaPrestamo,salidaFechaLimite):
    habilitar_salidas(salidaCodigoCliente,salidaCorreoCliente,salidaCodigoIsbn,salidaEjemplaresPrestado,salidaFechaPrestamo,salidaFechaLimite)
    salidaCodigoCliente.limpiar_entry()
    salidaCorreoCliente.limpiar_entry()
    salidaCodigoIsbn.limpiar_entry()
    salidaEjemplaresPrestado.limpiar_entry()
    deshabilitar_salidas(salidaCodigoCliente,salidaCorreoCliente,salidaCodigoIsbn,salidaEjemplaresPrestado,salidaFechaPrestamo,salidaFechaLimite)

def crearInterfazAltasPrestamos(root):
    interfaz_altas_prestamos = tk.Toplevel(root)
    interfaz_altas_prestamos.geometry("350x500+550+100")
    interfaz_altas_prestamos.resizable(False, False) 
    interfaz_altas_prestamos.title("Entregas de prestamos")
    return interfaz_altas_prestamos

def buscar_info_cliente(id_prestamo,salidaDato,columna):
    id_prestamo = str(id_prestamo)
    datoEncontrado = obtener_datos_cliente(id_prestamo,columna)
    salidaDato.habilitar()
    salidaDato.limpiar_entry()
    salidaDato.insert_entry(datoEncontrado)
    salidaDato.deshabilitar()

def buscar_info_cliente_fecha(id_prestamo,salidaFecha,columna):
    id_prestamo = str(id_prestamo)
    fechaEncontrada = obtener_datos_cliente(id_prestamo,columna)
    salidaFecha.habilitar()
    #salidaFecha.limpiar_entry()
    salidaFecha.set_fecha(fechaEncontrada)
    salidaFecha.deshabilitar()

def encontrar_fecha_limite(event,entradaFechaPrestamo,entradaFechaLimite):
    fechaPrestamo = entradaFechaPrestamo.get_fecha()
    fecha_futura = fechaPrestamo + timedelta(days=7)
    fecha_formateada = fecha_futura.strftime("%m/%d/%y")
    entradaFechaLimite.habilitar()
    #entradaFechaLimite.limpiar_entry()
    entradaFechaLimite.set_fecha(fecha_formateada)
    entradaFechaLimite.deshabilitar()

def mostrarRegistroPrestamos(interfaz_altas_prestamos, menu_principal, id_prestamo):

    salidaCodigoCliente = LabelEntryFrame(interfaz_altas_prestamos, "Codigo cliente:", 20, 15)
    salidaCodigoCliente.grid(row=0,column=0,pady=10, sticky=tk.W)
    salidaCodigoCliente.deshabilitar()

    salidaCorreoCliente = LabelEntryFrame(interfaz_altas_prestamos, "Correo cliente:", 40, 15)
    salidaCorreoCliente.grid(row=1,column=0,pady=10, sticky=tk.W)
    salidaCorreoCliente.deshabilitar()

    #salidaCodigoCliente.combo.bind("<<ComboboxSelected>>",lambda event: on_combobox_cliente_selected(event,entradaCodigoAlumno,entradaCorreoCliente,"alumno"))

    salidaCodigoIsbn = LabelEntryFrame(interfaz_altas_prestamos, "ISBN prestado:", 40, 15)
    salidaCodigoIsbn.grid(row=2,column=0,pady=10, sticky=tk.W)
    salidaCodigoIsbn.deshabilitar()

    salidaEjemplaresPrestado = LabelEntryFrame(interfaz_altas_prestamos, "Ejemplar prestado:", 20, 15)
    salidaEjemplaresPrestado.grid(row=3,column=0,pady=10, sticky=tk.W)
    salidaEjemplaresPrestado.deshabilitar()

    salidaFechaPrestamo = SeleccionadorFecha(interfaz_altas_prestamos, "Fecha prestamo:", 17)
    salidaFechaPrestamo.grid(row=4,column=0,pady=10, sticky=tk.W)
    salidaFechaPrestamo.deshabilitar()

    salidaFechaLimite = SeleccionadorFecha(interfaz_altas_prestamos, "Fecha limite:", 17)
    salidaFechaLimite.grid(row=5,column=0,pady=10, sticky=tk.W)
    salidaFechaLimite.deshabilitar()
    
    interfaz_altas_prestamos.bind("<Map>",lambda event: encontrar_fecha_limite(event, salidaFechaPrestamo, salidaFechaLimite))

    buscar_info_cliente(id_prestamo,salidaCodigoCliente,"codigo_cliente")
    buscar_info_cliente(id_prestamo,salidaCorreoCliente,"correo_cliente")
    buscar_info_cliente(id_prestamo,salidaCodigoIsbn,"isbn")
    buscar_info_cliente(id_prestamo,salidaEjemplaresPrestado,"num_ejemplar")
    buscar_info_cliente_fecha(id_prestamo,salidaFechaPrestamo,"fecha_prestamo")
    buscar_info_cliente_fecha(id_prestamo,salidaFechaLimite,"fecha_limite")

    entradaFechaEntrega = SeleccionadorFecha(interfaz_altas_prestamos, "Fecha entrega:", 17)
    entradaFechaEntrega.grid(row=6,column=0,pady=10, sticky=tk.W)
    entradaFechaEntrega.deshabilitar()

    buttonAceptar = BotonText(interfaz_altas_prestamos, "Aceptar", 6, command=lambda: registrar(salidaCodigoIsbn,salidaEjemplaresPrestado,entradaFechaEntrega,id_prestamo,salidaFechaLimite,salidaCodigoCliente))
    buttonAceptar.place(x=120, y=455)

    buttonCancelar = BotonText(interfaz_altas_prestamos, "Salir", 6, command=lambda:cancelar(interfaz_altas_prestamos,menu_principal))
    buttonCancelar.place(x=245, y=455)
    enviar_notificacion()

def accederInterfazEntregas(root,id_prestamo):
    interfaz_altas_prestamos = crearInterfazAltasPrestamos(root)
    root.withdraw()
    mostrarRegistroPrestamos(interfaz_altas_prestamos,root,id_prestamo)

def cancelar(root, menu_principal):
    root.destroy()  # Destruye la ventana actual
    menu_principal.deiconify()  # Muestra la ventana del menú principal

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300") 
    root.title("Registro de profesores")
    accederInterfazEntregas(root)
    root.mainloop()