import tkinter as tk
from models.actividad import Actividad
from models.destinoculinario import DestinoCulinario
from models.review import Review
from models.rutavisita import RutaVisita
from models.usuario import Usuario

from views.vista_inicio import VistaInicio
from views.vista_destinoculinario import DestinoCulinario
from views.vista_info_destinos import VistaInfoDestinos

from controllers.controlador_inicio import ControladorInicio
from controllers.controlador_destinoculinario import DestinoCulinario
from controllers.controlador_info_destino import ControladorInfoDestino


class Myapp(tk,Tk):
    def __init__ (self):
        tk.Tk.__init__(self)

        self.title("Comida Viajera")
        self.geometry("500x500")
        self.resizable(False,False)
        self.inicializar()
        self.cambiar_frame(self.vista_inicio)

    def inicializar(self):
        destinos=DestinoCulinario.cargar_de_json("data/destinos_culinarios.json")

        controlador_inicio= ControladorInicio(self)
        controlador_destinoculinario=ControladorDestinoCulinario(self.destinos)
        Controlador_info_destino = ControladorInfoDestino(self)

        self.vista_inicio=VistaInicio(self, controlador_inicio)
        self.vista_destinoculinario = VistaDestinoCulinario(self,controlador_destinoculinario)
        self.vista_info_destino= VistaInfoDestinos(self,controlador_info_destino)

        self.ajustar_frame(self.vista_inicio)
        self.ajustar_frame(self.vista_destinoculinario)
        self.ajustar_frame(self.vista_info_destino)

    def ajustar_frame(self,frame):
        frame.grid(row=0, column=0, sticky="nsew")
                   
    def cambiar_frame(self,frame_destino):
        frame_destino.tkraise()


if __name__=="__main__":
    app= MyApp()
    app.mainloop()



    

