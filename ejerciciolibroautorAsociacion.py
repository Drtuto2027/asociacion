class Autor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def listar_libros(self):
        print(f"Libros de {self.nombre}:")
        for libro in self.libros:
            print(f" - {libro.titulo}")

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        autor.agregar_libro(self)

# Crear autores
autor1 = Autor("Gabriel García Márquez")
autor2 = Autor("J.K. Rowling")

# Crear libros y asignarlos a autores
libro1 = Libro("Cien Años de Soledad", autor1)
libro2 = Libro("El Amor en los Tiempos del Cólera", autor1)
libro3 = Libro("Harry Potter y la Piedra Filosofal", autor2)

# Listar los libros de cada autor
autor1.listar_libros()
autor2.listar_libros()
