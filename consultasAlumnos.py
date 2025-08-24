import tkinter as tk
from tkinter import ttk
from elementos import BotonText
from conectar import consultar_alumnos, consultar_alumno_individual, enviar_notificacion

def crearInterfazConsultas(root):
    interfaz_consultas = tk.Toplevel(root)
    interfaz_consultas.geometry("1300x600+20+50") 
    interfaz_consultas.resizable(False, False) 
    interfaz_consultas.title("Consulta de alumnos")
    return interfaz_consultas

def mostrarConsulta(interfaz_consultas,menu_principal):
#Contenedor de todo

    canvas = tk.Canvas(interfaz_consultas)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(interfaz_consultas, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    tittlebar = tk.Frame(canvas, bd=2, relief=tk.RAISED)
    tittlebar.pack(side=tk.TOP, fill=tk.X)
    labelTitulo = tk.Label(canvas, text="Consultas Alumnos")
    labelTitulo.pack()

# Crear la tabla
    tabla = ttk.Treeview(canvas, columns=("Codigo","Nombre", "Carrera", "Correo", "Adeudo"))
    tabla.heading("#0", text="Index")
    tabla.heading("Codigo", text="Código")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Carrera", text="Carrera")
    tabla.heading("Correo", text="Correo")
    tabla.heading("Adeudo", text="Adeudo")

# Obtener y mostrar los datos
    consultar_alumnos(tabla)
    tabla.pack(expand=True, fill="both")
    
# Frame para el botón de búsqueda
    frame_busqueda = tk.Frame(canvas)
    frame_busqueda.pack(side="top", pady=(10, 0))

# Campo de entrada de texto para el código del alumno
    entradaCodigoBusqueda = tk.Entry(frame_busqueda)
    entradaCodigoBusqueda.pack(side="left")

    buscar_button = BotonText(frame_busqueda, "Buscar", 6, command=lambda:consultar_alumno_individual(tabla,entradaCodigoBusqueda))
    buscar_button.pack(side="left", padx=(10, 0))

# Botón para salir
    buttonCancelar = BotonText(frame_busqueda, "Salir", 6, command=lambda:cancelar(interfaz_consultas, menu_principal))
    buttonCancelar.pack(side="left", padx=(10, 0))
    enviar_notificacion()
    
def accederInterfazConsultas(root):
    interfaz_altas = crearInterfazConsultas(root)
    root.withdraw()
    mostrarConsulta(interfaz_altas,root)

def cancelar(root, menu_principal):
    root.destroy()  # Destruye la ventana actual
    menu_principal.deiconify()  # Muestra la ventana del menú principal


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300") 
    root.title("Registro de profesores")
    accederInterfazConsultas(root)
    root.mainloop()