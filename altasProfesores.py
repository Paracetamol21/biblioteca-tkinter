import tkinter as tk
from elementos import LabelEntryFrame,BotonText,LabelCombobox
from conectar import registrar_profesor, enviar_notificacion
from tkinter import messagebox

def validarSiEsVacio(dato,nombreCampo):
    if not dato or dato == "@academicos.udg.mx":
        messagebox.showerror("Error", "Por favor, llene el campo de " + nombreCampo)
        return True
    
def registrar(entradaCodigo,entradaNombre,entradaCarrera,entradaCorreo):
    campo = ['codigo', 'nombre', 'carrera', 'correo']

    codigo = entradaCodigo.get_entry().replace(',','')
    if validarSiEsVacio(codigo,campo[0]):
        return
    
    nombre = entradaNombre.get_entry()
    if validarSiEsVacio(nombre,campo[1]):
        return
    
    carrera = entradaCarrera.get_combobox()
    if validarSiEsVacio(carrera,campo[2]):
        return
    
    correoIncompleto = entradaCorreo.get_entry()
    correo = correoIncompleto + "@academicos.udg.mx"
    if validarSiEsVacio(correoIncompleto,campo[3]):
        return
    
    if registrar_profesor(codigo,nombre,carrera,correo) == True:
        limpiarEntry(entradaCodigo,entradaNombre,entradaCarrera,entradaCorreo)
    #validar_credenciales(usuarios,contraseñas,root)

def limpiarEntry(entradaCodigo,entradaNombre,entradaCarrera,entradaCorreo):
    entradaCodigo.limpiar_entry()
    entradaNombre.limpiar_entry()
    entradaCarrera.limpiar_combo()
    entradaCorreo.limpiar_entry()

def crearInterfazAltasProfesores(root):
    interfaz_altas_profesores = tk.Toplevel(root)
    interfaz_altas_profesores.geometry("350x300+550+200")
    interfaz_altas_profesores.resizable(False, False) 
    interfaz_altas_profesores.title("Altas de profesores")
    return interfaz_altas_profesores

def mostrarRegistroProfesores(interfaz_altas_profesores, menu_principal):
    entradaCodigo = LabelEntryFrame(interfaz_altas_profesores, "Codigo:", 20, 10)
    entradaCodigo.grid(row=0,column=0,pady=10, sticky=tk.W)
    
    entradaNombre = LabelEntryFrame(interfaz_altas_profesores, "Nombre:", 40, 10)
    entradaNombre.grid(row=1,column=0,pady=10, sticky=tk.W)

    opciones = ["ICOM", "QFB", "INNI"]
    entradaCarrera = LabelCombobox(interfaz_altas_profesores, "Carrera:", opciones, 17)
    entradaCarrera.grid(row=2,column=0,pady=10, sticky=tk.W)

    entradaCorreo = LabelEntryFrame(interfaz_altas_profesores, "Correo:", 20, 10)
    entradaCorreo.grid(row=3,column=0,pady=10, sticky=tk.W)

    labelExtension = tk.Label(interfaz_altas_profesores, text="@academicos.udg.mx")
    labelExtension.grid(row=3,column=0,pady=10, sticky=tk.E)

    buttonAceptar = BotonText(interfaz_altas_profesores, "Aceptar", 6, command=lambda:registrar(entradaCodigo,entradaNombre,entradaCarrera,entradaCorreo))
    buttonAceptar.place(x=88, y=205)

    buttonCancelar = BotonText(interfaz_altas_profesores, "Salir", 6, command=lambda:cancelar(interfaz_altas_profesores,menu_principal))
    buttonCancelar.place(x=210, y=205)

    # Asociar la función insertar_caracter al evento de soltar una tecla en el Entry
    entradaCodigo.entry.bind("<KeyRelease>", lambda event: insertar_caracter(event, entradaCodigo.entry))
    enviar_notificacion()
    
def accederInterfazProfesores(root):
    interfaz_altas_profesores = crearInterfazAltasProfesores(root)
    root.withdraw()
    mostrarRegistroProfesores(interfaz_altas_profesores,root)

def cancelar(root, menu_principal):
    root.destroy()  # Destruye la ventana actual
    menu_principal.deiconify()  # Muestra la ventana del menú principal

def insertar_caracter(event, entry):
    texto = entry.get()
    longitud = len(texto.replace(",", ""))  # Ignora los guiones para el conteo de caracteres
    if longitud % 3 == 0 and longitud != 0:
        entry.insert(tk.END, ",")  # Inserta un guión cada 3 caracteres


'''if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("400x300") 
    root.title("Registro de profesores")
    accederInterfazProfesores(root)
    root.mainloop()'''
