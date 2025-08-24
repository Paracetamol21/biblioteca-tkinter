
import tkinter as tk
from tkinter import ttk 
from tkcalendar import DateEntry
from datetime import datetime
from conectar import obtener_codigo_alumno,obtener_numero_ejemplar

class LabelEntryFrame(tk.Frame):
    def __init__(self, master, label_text , ancho, longitud, show_entry=False):
        super().__init__(master)
        
        self.label = tk.Label(self, text=label_text, width=longitud)
        if show_entry:
            self.entry = tk.Entry(self, width=ancho, show="*")
        else:
            self.entry = tk.Entry(self, width=ancho)

        self.label.grid(row=0, column=0,padx=5, pady=5,sticky=tk.E)
        self.entry.grid(row=0, column=1,padx=5, pady=5,sticky=tk.W)
    
    def get_entry(self):
        #if self.validar_datos():
        return self.entry.get()
    
    def insert_entry(self,element):
        self.entry.insert(0,element)
    
    def limpiar_entry(self):
        self.entry.delete(0,tk.END)
    
    def deshabilitar(self):
        self.entry.config(state="disabled")

    def habilitar(self):
        self.entry.config(state="normal")
    
class LabelCombobox(tk.Frame):
    def __init__(self, master, label_text, opciones, ancho):
        super().__init__(master)
        
        self.label = tk.Label(self, text=label_text,width=10)
        self.combo = ttk.Combobox(self,values=opciones, width=ancho)
        
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.combo.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

    def get_combobox(self):
        return self.combo.get()
    
    def limpiar_combo(self):
        self.combo.delete(0,tk.END)


class BotonText(tk.Frame):
    def __init__(self, master, text_button, ancho, command=None):
        super().__init__(master)
        self.button = tk.Button(self, text=text_button, command=command, width=ancho, bg="#663300", fg="#F59622")
        
        
        self.button.grid(row=0,column=0,padx=5, pady=5)

class CustomMenuButton(tk.Menubutton):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.configure(
            relief="raised",
            font=("Arial", 10),
            bg="#663300",
            fg="#F59622",
            borderwidth=2
        )
        self.menu = tk.Menu(self, tearoff=False)
        self.configure(menu=self.menu)

    def add_command(self, **kwargs):
        self.menu.add_command(**kwargs)

class ComboboxPrestamos(tk.Frame):
    def __init__(self, master, label_text, tabla, columna, ancho, libroSeleccionado,show_disponibles=False):
        super().__init__(master)
        
        self.label = tk.Label(self, text=label_text,width=15)
        self.combo = ttk.Combobox(self, width=ancho)
        
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.E)
        self.combo.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)

        if show_disponibles:
            ejemplares_disponibles = obtener_numero_ejemplar(libroSeleccionado)
            self.combo['values'] = ejemplares_disponibles

        else:
            datos_columna = obtener_codigo_alumno(tabla, columna)
            self.combo['values'] = datos_columna
            self.combo.bind("<KeyRelease>",lambda event: self.handle_keyrelease(event, tabla, columna))
            self.combo.bind("<<ComboboxSelected>>",lambda event: self.actualizar_combobox(event,libroSeleccionado))

    def handle_keyrelease(self, event, tabla, columna):
        texto = self.combo.get().lower()  # Obtener el texto ingresado en el ComboBox
        datos_columna = obtener_codigo_alumno(tabla, columna)
        datos_columna = [str(item) for item in datos_columna]  # Convertir todos los elementos a cadenas de texto
        self.combo['values'] = [item for item in datos_columna if texto in item.lower()]  # Filtrar los elementos que coincidan con el texto ingresado

    def actualizar_combobox(self,event,libroSeleccionado):
        ejemplares_disponibles = obtener_numero_ejemplar(libroSeleccionado)
        self.combo['values'] = ejemplares_disponibles

    def disabled_combo(self):
        self.combo.config(state=tk.DISABLED)

    def enabled_combo(self):
        self.combo.config(state=tk.NORMAL)

    def get_combobox(self):
        return self.combo.get()
    
    def limpiar_combo(self):
        self.combo.delete(0,tk.END)
        
class SeleccionadorFecha(tk.Frame):
    def __init__(self, master, label_text, ancho):
        super().__init__(master)

        #fecha_actual = datetime.now().date()

        self.label = tk.Label(self, text=label_text, width=15)
        #self.cal = DateEntry(self, width=ancho, background='darkblue', foreground='white', borderwidth=2, mindate=fecha_actual)
        self.cal = DateEntry(self, width=ancho, background='darkblue', foreground='white', borderwidth=2)

        self.cal.grid(row=0, column=1, padx=5, pady=5, sticky=tk.E)
        self.label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.EW)

    def get_fecha(self):
        return self.cal.get_date()
    
    def set_fecha(self,fecha):
        self.cal.set_date(fecha)
    
    def deshabilitar(self):
        self.cal.config(state="disabled")

    def habilitar(self):
        self.cal.config(state="normal")



    