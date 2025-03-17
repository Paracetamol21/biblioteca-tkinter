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
from elementos import LabelEntryFrame,BotonText
from conectar import registrar_libro,enviar_notificacion
from tkinter import messagebox

def validarSiEsVacio(dato,nombreCampo):
    if not dato:
        messagebox.showerror("Error", "Por favor, llene el campo de " + nombreCampo)
        return True
    
def registrar(entradaISBN,entradaTitulo,entradaAutor,entradaEditorial,entradaAño,entradaEjemplar):
    campo = ['ISBN', 'titulo', 'autor', 'editorial', 'año de publicacion', 'ejemplar']

    isbn = entradaISBN.get_entry()
    if validarSiEsVacio(isbn,campo[0]):
        return
    
    titulo = entradaTitulo.get_entry()
    if validarSiEsVacio(titulo,campo[1]):
        return
    
    autor = entradaAutor.get_entry()
    if validarSiEsVacio(autor,campo[2]):
        return
    
    editorial = entradaEditorial.get_entry()
    if validarSiEsVacio(editorial,campo[3]):
        return
    
    año = entradaAño.get_entry()
    if validarSiEsVacio(año,campo[4]):
        return
    
    ejemplar = entradaEjemplar.get_entry()
    if validarSiEsVacio(ejemplar,campo[5]):
        return
    
    estado = "Disponible"
    
    if registrar_libro(isbn, titulo, autor, editorial, año, ejemplar, estado) == True:
        limpiarEntry(entradaISBN,entradaTitulo,entradaAutor,entradaEditorial,entradaAño,entradaEjemplar)
    #validar_credenciales(usuarios,contraseñas,root)

def limpiarEntry(entradaISBN,entradaTitulo,entradaAutor,entradaEditorial,entradaAño,entradaEjemplar):
    entradaISBN.limpiar_entry()
    entradaTitulo.limpiar_entry()
    entradaAutor.limpiar_entry()
    entradaEditorial.limpiar_entry()
    entradaAño.limpiar_entry()
    entradaEjemplar.limpiar_entry()

def crearInterfazAltasLibros(root):
    interfaz_altas_libros = tk.Toplevel(root)
    interfaz_altas_libros.geometry("470x350+500+150") 
    interfaz_altas_libros.resizable(False, False)
    interfaz_altas_libros.title("Altas de libros")
    return interfaz_altas_libros

def mostrarRegistroLibros(interfaz_altas_libros, menu_principal):
    entradaISBN = LabelEntryFrame(interfaz_altas_libros, "ISBN:", 20, 10)
    entradaISBN.grid(row=0,column=0,pady=10, sticky=tk.W)
    
    entradaTitulo = LabelEntryFrame(interfaz_altas_libros, "Titulo:", 60, 10)
    entradaTitulo.grid(row=1,column=0,pady=10, sticky=tk.W)

    entradaAutor = LabelEntryFrame(interfaz_altas_libros, "Autor:", 40, 10)
    entradaAutor.grid(row=2,column=0,pady=10, sticky=tk.W)
    
    entradaEditorial = LabelEntryFrame(interfaz_altas_libros, "Editorial:", 20, 10)
    entradaEditorial.grid(row=3,column=0,pady=10, sticky=tk.W)

    entradaAño = LabelEntryFrame(interfaz_altas_libros, "Publicacion:", 20, 10)
    entradaAño.grid(row=4,column=0,pady=10, sticky=tk.W)
    
    entradaEjemplar = LabelEntryFrame(interfaz_altas_libros, "Cantidad:", 10, 10)
    entradaEjemplar.grid(row=5,column=0,pady=10, sticky=tk.W)

    buttonAceptar = BotonText(interfaz_altas_libros, "Aceptar", 6, command=lambda:registrar(entradaISBN,entradaTitulo,entradaAutor,entradaEditorial,entradaAño,entradaEjemplar))
    buttonAceptar.place(x=88, y=305)

    buttonCancelar = BotonText(interfaz_altas_libros, "Salir", 6, command=lambda:cancelar(interfaz_altas_libros,menu_principal))
    buttonCancelar.place(x=210, y=305)
    enviar_notificacion()

def accederInterfazLibros(root):
    interfaz_altas_libros = crearInterfazAltasLibros(root)
    root.withdraw()
    mostrarRegistroLibros(interfaz_altas_libros,root)

def cancelar(root, menu_principal):
    root.destroy()  # Destruye la ventana actual
    menu_principal.deiconify()  # Muestra la ventana del menú principal

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("505x800") 
    root.title("Registro de profesores")
    accederInterfazLibros(root)
    root.mainloop()