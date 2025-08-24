
import tkinter as tk
from tkinter import ttk, messagebox
from elementos import BotonText
from conectar import consultar_libros, consultar_libros_individual, enviar_notificacion

def crearInterfazConsultasLibros(root):
    interfaz_consultas_libros = tk.Toplevel(root)
    interfaz_consultas_libros.geometry("1300x600+20+50") 
    interfaz_consultas_libros.resizable(False, False) 
    interfaz_consultas_libros.title("Consultas de libros ")
    return interfaz_consultas_libros

def mostrarConsulta(interfaz_consultas_libros,menu_principal):
#Contenedor de todo
    canvas = tk.Canvas(interfaz_consultas_libros)
    canvas.pack(side="bottom", fill="both", expand=True)

    scrollbar = tk.Scrollbar(interfaz_consultas_libros, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    #scrollbar.pack(side="right", fill="y")
    scrollbar.place(relx=0.99, rely=0.1, relheight=0.9)

    tittlebar = tk.Frame(canvas, bd=2, relief=tk.RAISED)
    tittlebar.pack(side=tk.TOP, fill=tk.X)
    labelTitulo = tk.Label(canvas, text="Consultas libros")
    labelTitulo.pack()

# Crear la tabla
    tabla = ttk.Treeview(canvas, columns=("ISBN","Titulo", "Autor", "Editorial", "Año de publicacion", "Ejemplar", "Estado"))
    tabla.column("#0", width=5)  
    tabla.column("ISBN", width=100)  
    tabla.column("Titulo", width=150)
    tabla.column("Autor", width=100)
    tabla.column("Editorial", width=5)
    tabla.column("Año de publicacion", width=5)
    tabla.column("Ejemplar", width=5)
    tabla.column("Estado", width=5)
    
    tabla.heading("#0", text="Index")
    tabla.heading("ISBN", text="ISBN")
    tabla.heading("Titulo", text="Titulo")
    tabla.heading("Autor", text="Autor")
    tabla.heading("Editorial", text="Editorial")
    tabla.heading("Año de publicacion", text="Año de publicacion")
    tabla.heading("Ejemplar", text="Ejemplar")
    tabla.heading("Estado", text="Estado")

# Obtener y mostrar los datos
    consultar_libros(tabla)
    tabla.pack(expand=True, fill="both")
    
# Frame para el botón de búsqueda
    frame_busqueda = tk.Frame(interfaz_consultas_libros)
    frame_busqueda.pack(side="top", pady=(10, 0))

# Campo de entrada de texto para el código del libro
    entradaIsbnBusqueda = tk.Entry(frame_busqueda)
    #entradaIsbnBusqueda.pack(side="left")
    entradaIsbnBusqueda.grid(row=0,column=0)

    buscar_button = BotonText(frame_busqueda, "Buscar", 6, command=lambda:consultar_libros_individual(tabla, entradaIsbnBusqueda))
    #buscar_button.pack(side="left", padx=(10, 0))
    buscar_button.grid(row=0,column=1)

# Botón para salir
    buttonCancelar = BotonText(frame_busqueda, "Salir", 6, command=lambda:cancelar(interfaz_consultas_libros, menu_principal))
    buttonCancelar.grid(row=0,column=2)
    #buttonCancelar.pack(side="left", padx=(10, 0))

    buttonRecargar = BotonText(frame_busqueda, " ⟳", 2, command=lambda:recargar_tabla(tabla))
    buttonRecargar.grid(row=0,column=3)
    #buttonCancelar.pack(side="left", padx=(10, 0))
    enviar_notificacion()

def recargar_tabla(tabla):
    tabla.delete(*tabla.get_children())  # Borra todos los elementos de la tabla
    consultar_libros(tabla)

def accederInterfazConsultasLibros(root):
    interfaz_altas_libros = crearInterfazConsultasLibros(root)
    root.withdraw()
    mostrarConsulta(interfaz_altas_libros,root)

def cancelar(root, menu_principal):
    root.destroy()  # Destruye la ventana actual
    menu_principal.deiconify()  # Muestra la ventana del menú principal

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300") 
    root.title("Registro de profesores")
    accederInterfazConsultasLibros(root)
    root.mainloop()