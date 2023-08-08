class Review:
    def __init__ (self, id: int, id_destino: int,
    id_usuarios: int, calificacion: int,
    comentario: str, animo:str):
        """
        calificacion int 1 a 5 
        animo str "positivo" o "negativo"
        """
        self.id = id
        self.id_destino = id_destino
        self.calificacion = calificacion
        self.comentario = comentario
        self.animo = animo
    
    def to_json (self):
        pass

    @classmethod
    def from_json (cls,data):
        pass