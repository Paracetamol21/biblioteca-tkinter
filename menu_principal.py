import tkinter as tk
from PIL import Image,ImageTk 
from altasAlumnos import accederInterfaz
from consultasAlumnos import accederInterfazConsultas
from altasProfesores import accederInterfazProfesores
from consultasProfesores import accederInterfazConsultasProfesores
from altasLibros import accederInterfazLibros
from consultasLibros import accederInterfazConsultasLibros
from altasPrestamos import accederInterfazPrestamos
from consultasPrestamos import accederInterfazConsultasPrestamos
from elementos import CustomMenuButton

def deshabilitar(menuButtonAlumnos,menuButtonProfesores,menuButtonLibros):
    menuButtonAlumnos.config(state="disabled")
    menuButtonProfesores.config(state="disabled")
    menuButtonLibros.config(state="disabled")

def crearMenu(root):
    global imagen_tk
    #Crear ventana
    menu_prin = tk.Toplevel(root)
    menu_prin.title("Menu principal")
    menu_prin.geometry("1000x520+200+100") 
    menu_prin.resizable(False, False)
    # Cargar la imagen con PIL
    imagen_pil = Image.open("librero.png")                                         
    imagen_tk = ImageTk.PhotoImage(imagen_pil)                                         
    # Crear un widget Canvas y mostrar la imagen                                    
    canvas = tk.Canvas(menu_prin, width=imagen_pil.width, height=imagen_pil.height)
    canvas.place(x=0, y=0)                                                                                                      
    canvas.create_image(0, 0, anchor=tk.NW, image=imagen_tk)                       
    return menu_prin

def mostrarMenuPrincipal(menu_prin,tipo_privilegio):
    #Frame que contiene el labelTitulo
    tittlebar = tk.Frame(menu_prin, bd=2, relief=tk.RAISED)
    tittlebar.pack(side=tk.TOP, fill=tk.X)

    labelTitulo = tk.Label(tittlebar, text="Biblioteca Universidad Tecnologica", font=("Arial", 14), bg="#663300", fg="#F59622", borderwidth=2)
    labelTitulo.pack(fill=tk.X)
    #labelBienvenida.grid(row=0,column=0)
    
    #Frame que contiene el boton desplegable
    toolbar = tk.Frame(menu_prin, bd=1, relief=tk.RAISED, bg="#663300")
    toolbar.pack(side=tk.TOP, fill=tk.X)

    # Creamos el menú desplegable para ALUMNOS
    menuButtonAlumnos = tk.Menubutton(toolbar, width=15, height=1, text="Alumnos", relief="raised",  font=("Arial", 10), bg="#663300", fg="#F59622", borderwidth=2)
    menuButtonAlumnos.grid(row=1, column=0)

    menuButtonAlumnos = CustomMenuButton(toolbar,width=15, height=1, text="Alumnos")
    menuButtonAlumnos.grid(row=1, column=0)

    menuAlumnos = menuButtonAlumnos.menu
    menuAlumnos.add_command(label="Altas" + " " * 16, command=lambda: accederInterfaz(menu_prin))
    menuAlumnos.add_separator()
    menuAlumnos.add_command(label="Consultas", command=lambda: accederInterfazConsultas(menu_prin))
    menuAlumnos.add_separator()

    #Creamos el menu desplegable para PROFESORES
    menuButtonProfesores = tk.Menubutton(toolbar, width=15, height=1, text="Profesores", relief="raised",  font=("Arial", 10), bg="#663300", fg="#F59622", borderwidth=2)
    menuButtonProfesores.grid(row=1, column=1)

    menuButtonProfesores = CustomMenuButton(toolbar, width=15, height=1, text="Profesores")
    menuButtonProfesores.grid(row=1, column=1)

    menuProfesores = menuButtonProfesores.menu
    menuProfesores.add_command(label="Altas" + " " * 16, command=lambda: accederInterfazProfesores(menu_prin))
    menuProfesores.add_separator()
    menuProfesores.add_command(label="Consultas", command=lambda: accederInterfazConsultasProfesores(menu_prin))
    menuProfesores.add_separator()
    
    #Creamos el menu desplegable para LIBROS
    menuButtonLibros = tk.Menubutton(toolbar, width=15, height=1, text="Libros", relief="raised",  font=("Arial", 10), bg="#663300", fg="#F59622", borderwidth=2)
    menuButtonLibros.grid(row=1, column=2)

    menuButtonLibros = CustomMenuButton(toolbar, width=15, height=1, text="Libros")
    menuButtonLibros.grid(row=1, column=2)

    menuLibros = menuButtonLibros.menu
    menuLibros.add_command(label="Altas" + " " * 16, command=lambda: accederInterfazLibros(menu_prin))
    menuLibros.add_separator()
    menuLibros.add_command(label="Consultas", command=lambda: accederInterfazConsultasLibros(menu_prin))
    menuLibros.add_separator()

    #Creamos el menu desplegable para PRESTAMOS
    menuButtonPrestamos = tk.Menubutton(toolbar, width=15, height=1, text="Prestamos", relief="raised",  font=("Arial", 10), bg="#663300", fg="#F59622", borderwidth=2)
    menuButtonPrestamos.grid(row=1, column=3)

    menuButtonPrestamos = CustomMenuButton(toolbar, width=15, height=1, text="Prestamos")
    menuButtonPrestamos.grid(row=1, column=3)

    menuPrestamos = menuButtonPrestamos.menu
    menuPrestamos.add_command(label="Altas" + " " * 16, command=lambda: accederInterfazPrestamos(menu_prin))
    menuPrestamos.add_separator()
    menuPrestamos.add_command(label="Consultas", command=lambda: accederInterfazConsultasPrestamos(menu_prin))
    menuPrestamos.add_separator()

    #Creamos el boton de salida
    buttonCancelar = tk.Button(toolbar, text="Salir", width=15, height=1, relief="raised",  font=("Arial", 10), bg="#663300", fg="#F59622", borderwidth=2, command=menu_prin.quit)
    buttonCancelar.grid(row=1,column=4)

    if tipo_privilegio == 'Empleado':
        menuAlumnos.entryconfig(0, state="disabled")
        menuProfesores.entryconfig(0, state="disabled")
        menuLibros.entryconfig(0, state="disabled")

def accederMenu(root,tipo_privilegio):
    menu_prin = crearMenu(root)
    root.withdraw()
    mostrarMenuPrincipal(menu_prin,tipo_privilegio)


'''if __name__ == "__main__":

    menu_prin = tk.Tk()
    #menu_prin.geometry("300x160") 
    menu_prin.title("Menu principal")
    mostrarMenuPrincipal(menu_prin)
    
    menu_prin.mainloop()
    #return menu_prin'''