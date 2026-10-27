class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True

    def mostrar_informacion(self):
        if self.disponible == True:
            estado = "Disponible" 
        else:
            estado = "Prestado"
        return f"Título: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Estado: {estado}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return True
        else:
            return False

    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return True
        else:
            return False



