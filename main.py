from clases.libro import Libro
from clases.usuario import Usuario
from clases.prestamo import Prestamo

def registrar_libro():
    titulo = input("Título del libro: ").strip()
    autor = input("Autor del libro: ").strip()
    isbn = input("ISBN del libro: ").strip()
    libro = Libro(titulo, autor, isbn)
    return libro

def registrar_usuario():
    nombre = input("Nombre del usuario: ").strip()
    id_usuario = int(input("ID del usuario: ").strip())
    usuario = Usuario(nombre, id_usuario)
    return usuario

def registrar_prestamo(libros, usuarios):
    isbn = input("ISBN del libro a prestar: ").strip()
    libro = next((l for l in libros if l.isbn == isbn), None)
    if not libro:
        print("Libro no encontrado")
        return

    if not libro.disponible:
        print("El libro no está disponible")
        return

    id_usuario = int(input("ID del usuario: ").strip())
    usuario = next((u for u in usuarios if u.id == id_usuario), None)
    if not usuario:
        print("Usuario no encontrado")
        return

    fecha = input("Fecha del préstamo (dd/mm/aaaa): ").strip()
    libro.prestar()
    prestamo = Prestamo(libro, usuario, fecha)
    return prestamo

def registrar_devolucion(libros):
    isbn = input("ISBN del libro a devolver: ").strip()
    libro = next((l for l in libros if l.isbn == isbn), None)

    if not libro:
        print("Libro no encontrado")
        return

    if libro.disponible:
        print("El libro no está prestado")
        return

    if libro.devolver():
        print("Libro devuelto correctamente")
    else:
        print("No se pudo devolver el libro")

def mostrar_menu():
    print("\n ---BIBLIOTECA---")
    print("1. Registrar libro")
    print("2. Registrar usuario")
    print("3. Registrar préstamo")
    print("4. Registrar devolución")
    print("5. Listar libros")
    print ("6. Listar usuarios")
    print("7. Listar préstamos")
    print("8. Salir")

def main():
    libros = []
    usuarios = []
    prestamos = []

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            libro = registrar_libro()
            libros.append(libro)
            print("Libro registrado.")

        elif opcion == "2":
            usuario = registrar_usuario()
            usuarios.append(usuario)
            print("Usuario registrado.")

        elif opcion == "3":
            prestamo = registrar_prestamo(libros, usuarios)
            if prestamo:
                prestamos.append(prestamo)
                print("Préstamo registrado.")

        elif opcion == "4":
            registrar_devolucion(libros)

        elif opcion == "5":
            if not libros:
                print("No hay libros registrados.")
            else:
                for libro in libros:
                    print(libro.mostrar_informacion())

        elif opcion == "6":
            if not usuarios:
                print("No hay usuarios registrados.")
            else:
                for usuario in usuarios:
                    print(usuario.mostrar_informacion())

        elif opcion == "7":
            if not prestamos:
                print("No hay préstamos registrados.")
            else:
                for prestamo in prestamos:
                    print(prestamo.mostrar_informacion())

        elif opcion == "8":
            print("Saliendo del sistema de la biblioteca...")
            break

        else:
            print("Opción inválida. Intente nuevamente")

if __name__ == "__main__":
    main()

