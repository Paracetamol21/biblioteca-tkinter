
import tkinter as tk
from tkinter import ttk
from elementos import BotonText
from conectar import consultar_prestamos, consultar_prestamos_individual, enviar_notificacion
from entregasPrestamos import accederInterfazEntregas

def manejar_prestamo(event, treeview, root):
    item = treeview.focus()  # Obtener el ítem seleccionado
    if item:  # Verificar si hay algún ítem seleccionado
        # Obtener el contenido del item seleccionado
        selected_item = treeview.selection()[0]
        contenido = treeview.item(selected_item)['values']
        id_prestamo = contenido[0] #Codigo de la tupla seleccionada
        # Imprimir el contenido
        accederInterfazEntregas(root,id_prestamo)

        #print(dato2)
        #print("Elemento seleccionado:", treeview.item(item)['text'])

def crearInterfazConsultasPrestamos(root):
    interfaz_consultas_prestamos = tk.Toplevel(root)
    interfaz_consultas_prestamos.geometry("1300x600+20+50") 
    interfaz_consultas_prestamos.resizable(False, False) 
    interfaz_consultas_prestamos.title("Consultas de prestamos")
    return interfaz_consultas_prestamos

def mostrarConsulta(interfaz_consultas_prestamos,menu_principal):
#Contenedor de todo
    canvas = tk.Canvas(interfaz_consultas_prestamos)
    canvas.pack(side="bottom", fill="both", expand=True)

    scrollbar = tk.Scrollbar(interfaz_consultas_prestamos, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    #scrollbar.pack(side="right", fill="y")
    scrollbar.place(relx=0.99, rely=0.1, relheight=0.9)
    
    tittlebar = tk.Frame(canvas, bd=2, relief=tk.RAISED)
    tittlebar.pack(side=tk.TOP, fill=tk.X)
    labelTitulo = tk.Label(canvas, text="Consultas prestamos")
    labelTitulo.pack()

# Crear la tabla
    tabla = ttk.Treeview(canvas, columns=("ID prestamo","Codigo cliente","Correo cliente", "ISBN", "N° Ejemplar", "Fecha prestamo", "Fecha limite", "Fecha entrega"))
    
    tabla.column("#0", width=5) 
    tabla.column("ID prestamo", width=6)  
    tabla.column("Codigo cliente", width=6)  
    tabla.column("Correo cliente", width=80)
    tabla.column("ISBN", width=100)
    tabla.column("N° Ejemplar", width=5)
    tabla.column("Fecha prestamo", width=5)
    tabla.column("Fecha limite", width=5)
    tabla.column("Fecha entrega", width=5)
    
    tabla.heading("#0", text="Index")
    tabla.heading("ID prestamo", text="ID prestamo")
    tabla.heading("Codigo cliente", text="Codigo cliente")
    tabla.heading("Correo cliente", text="Correo cliente")
    tabla.heading("ISBN", text="ISBN")
    tabla.heading("N° Ejemplar", text="N° Ejemplar")
    tabla.heading("Fecha prestamo", text="Fecha prestamo")
    tabla.heading("Fecha limite", text="Fecha limite")
    tabla.heading("Fecha entrega", text="Fecha entrega")

    #EVENTO DE CLICK EN TABLA
    tabla.bind('<ButtonRelease-1>',  lambda event: manejar_prestamo(event, tabla, interfaz_consultas_prestamos))

# Obtener y mostrar los datos
    consultar_prestamos(tabla)
    tabla.pack(expand=True, fill="both")

    frame_opciones = tk.Frame(interfaz_consultas_prestamos)
    frame_opciones.pack(side="top", pady=(10, 0))

    entradaBusqueda = tk.Entry(frame_opciones)
    entradaBusqueda.grid(row=0,column=0)

    buscar_button = BotonText(frame_opciones, "Buscar", 6, command=lambda:consultar_prestamos_individual(tabla, entradaBusqueda))
    buscar_button.grid(row=0,column=1)

    buttonCancelar = BotonText(frame_opciones, "Salir", 6, command=lambda:cancelar(interfaz_consultas_prestamos,menu_principal))
    buttonCancelar.grid(row=0,column=2)

    buttonRecargar = BotonText(frame_opciones, " ⟳", 2, command=lambda:recargar_tabla(tabla))
    buttonRecargar.grid(row=0,column=3)
    enviar_notificacion()

def recargar_tabla(tabla):
    tabla.delete(*tabla.get_children())  # Borra todos los elementos de la tabla
    consultar_prestamos(tabla)

def accederInterfazConsultasPrestamos(root):
    interfaz_altas_prestamos = crearInterfazConsultasPrestamos(root)
    root.withdraw()
    mostrarConsulta(interfaz_altas_prestamos,root)

def cancelar(root, menu_principal):
    root.destroy()  # Destruye la ventana actual
    menu_principal.deiconify()  # Muestra la ventana del menú principal

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300") 
    root.title("Registro de profesores")
    accederInterfazConsultasPrestamos(root)
    root.mainloop()