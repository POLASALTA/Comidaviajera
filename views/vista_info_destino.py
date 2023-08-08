import tkinter as tk

class Vistainfo(tk.frame):
    def__init__ (self,master=None, controlador=None)
    super().__init__(master)
    self.master=master
    self.controlador=controlador
    self.destino_label=tk.label(self,text*"")
    self.destino_label.pack(pady=50)
    self.destino_label.config(justify=tk.LEFT)
    Self.boton_regresar=tk.Button(
        self,
        text="Regresa a lista de destinos"
        command=self.controlador.regresar_destinos_culinarios,
    )
    self.boton_regresar.pack(pady=10)

def mostrar_info_destino_culinario(self,destino):
    info=f"Destino:(destino.nombre)\nTipodecocina:(destino_tipo_cocina:)"
    self.destino_label(*text*)=info
    