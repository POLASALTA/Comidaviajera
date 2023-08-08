class Ubicacion:
    def __init__ (self, id: int, direccion:str,
    coordenadas: list [float]):
        self.id =id
        self.direccion = direccion
        self.coordenadas = coordenadas
    
    def to_json(self):
        pass

    @classmethod
    def from_json (cls,data):
        pass