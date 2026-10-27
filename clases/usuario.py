class Usuario:
    def __init__(self, nombre, id_usuario):
        self.nombre = nombre
        self.id = id_usuario

    def mostrar_informacion(self):
        return f"Usuario: {self.nombre}, ID: {self.id}"
        