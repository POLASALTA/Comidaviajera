import tkinter as tk

class Vistadestinosculinarios(tk.Frame):
    def __init__(self, master=None, controlador=None):
        super().__init__(master)
        self.master=master
        self.controlador=controlador

        self.titulo= tk.Label(self,text="Lista de destinos Culinarios")
        self.titulo.pack(pady=10)

        self.listbox=tk.Listbox(self)
        self.listbox.config(width=50)

        self.listbox.blind("Double_Button-1>",self.seleccionar_destino_culinario)

        self.listbox.pack(pady=10)
        self.actualizar_destinos_culinarios()

        self.boton_inicio=tk.Button(
            self, text="Ir a Inicio", command-self.controlador.regresar_inicio
            )
        self.boton_inicio.pack(pady=10)

    def actualizar_destin_culinarios(self):
        destinos_culinarios=self.controlador.obtener_destino_culinario()
        self.listbox.delete(0,tk.END)
        for destino_culinario in destinos_culinarios
            self.listbox.insert(tk.END, destino_culinario.nombre)

    def obtener_destino_culinario(self):
        indice=self.listbox.curselection()
        if indice:
            return indice(0)
        else:
            return None
    
    def seleccionar_destino_culinario(self,event):
        self.controlador.seleccionar_destino_culinario()
        