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
from tkinter import ttk, messagebox
from elementos import BotonText
from conectar import consultar_profesores,consultar_profesor_individual,enviar_notificacion

def crearInterfazConsultasProfesores(root):
    interfaz_consultas_profesores = tk.Toplevel(root)
    interfaz_consultas_profesores.geometry("1300x600+20+50") 
    interfaz_consultas_profesores.resizable(False, False) 
    interfaz_consultas_profesores.title("Altas de profesores")
    return interfaz_consultas_profesores

def mostrarConsultaProfesores(interfaz_consultas_profesores,menu_principal):
#Contenedor de todo
    canvas = tk.Canvas(interfaz_consultas_profesores)
    canvas.pack(side="left", fill="both", expand=True)

    scrollbar = tk.Scrollbar(interfaz_consultas_profesores, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side="right", fill="y")

    tittlebar = tk.Frame(canvas, bd=2, relief=tk.RAISED)
    tittlebar.pack(side=tk.TOP, fill=tk.X)
    labelTitulo = tk.Label(canvas, text="Consultas profesor")
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
    consultar_profesores(tabla)
    tabla.pack(expand=True, fill="both")
    
# Frame para el botón de búsqueda
    frame_busqueda = tk.Frame(canvas)
    frame_busqueda.pack(side="top", pady=(10, 0))

# Campo de entrada de texto para el código del alumno
    entradaCodigoProfesor = tk.Entry(frame_busqueda)
    entradaCodigoProfesor.pack(side="left")

    buscar_button = BotonText(frame_busqueda, "Buscar", 6, command=lambda:consultar_profesor_individual(tabla,entradaCodigoProfesor))
    buscar_button.pack(side="left", padx=(10, 0))

# Botón para salir
    buttonCancelar = BotonText(frame_busqueda, "Salir", 6, command=lambda:cancelar(interfaz_consultas_profesores, menu_principal))
    buttonCancelar.pack(side="left", padx=(10, 0))
    enviar_notificacion()

def accederInterfazConsultasProfesores(root):
    interfaz_altas_profesores = crearInterfazConsultasProfesores(root)
    root.withdraw()
    mostrarConsultaProfesores(interfaz_altas_profesores,root)

def cancelar(root, menu_principal):
    root.destroy()  # Destruye la ventana actual
    menu_principal.deiconify()  # Muestra la ventana del menú principal


'''if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300") 
    root.title("Registro de profesores")
    accederInterfazConsultasProfesores(root)
    root.mainloop()'''