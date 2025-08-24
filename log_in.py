import tkinter as tk
from elementos import LabelEntryFrame,BotonText
from conectar import validar_credenciales, enviar_notificacion
from menu_principal import accederMenu

#def irMenuPrincipal():

def validar():
    usuarios = frame1.get_entry()
    contraseñas = frame2.get_entry()
    tipo_privilegio = validar_credenciales(usuarios, contraseñas)  # Llama a validar_credenciales una vez y almacena el resultado
    if tipo_privilegio:  # Si el tipo de privilegio no es None o False
        accederMenu(root, tipo_privilegio)

def cancelar():
    root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x160+550+200")
    root.resizable(False, False)
    root.title("Inicio de sesion")
    
    frame1 = LabelEntryFrame(root, "Usuario:", 20, 10)
    frame1.grid(row=0,column=0,pady=10, sticky=tk.E)
    
    frame2 = LabelEntryFrame(root, "Contraseña:",20, 10, show_entry=True)
    frame2.grid(row=1,column=0,pady=10, sticky=tk.E)
    
    buttonAceptar = BotonText(root, "Aceptar", 6, command=validar)
    buttonAceptar.grid(row=3,column=0)

    buttonCancelar = BotonText(root, "Salir", 6, command=cancelar)
    buttonCancelar.grid(row=3,column=0, sticky=tk.E)
    enviar_notificacion()

    root.mainloop()
