class Prestamo:
    def __init__(self, libro, usuario, fecha):
        self.libro = libro
        self.usuario = usuario
        self.fecha = fecha

    def mostrar_informacion(self):
            return f"Libro: {self.libro.mostrar_informacion()}, {self.usuario.mostrar_informacion()}, Fecha: {self.fecha}"

    