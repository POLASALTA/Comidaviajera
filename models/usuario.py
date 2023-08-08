class Usuario:
    def __init__ (self, id: int, nombre:str,
    Apellido: str, historial_rutas: list [int]):
        self.id =id
        self.nombre = nombre
        self.apellido = Apellido
        self.historial_rutas = historial_rutas
            
    def to_json(self):
        return {["id": self.id, "nombre": self.nombre,
        "historial_rutas": self.historial_rutas]} 

    @classmethod
    def from_json (cls,json_data):
        data = json.loads(json_data)
        return cls(data ["id"], data["nombre"], data["apellido"],
        data["historial_rutas"])
        
    
