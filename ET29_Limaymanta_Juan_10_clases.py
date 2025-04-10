
class Libro:
    def __init__(self,titulo,autor,genero,numero_pagina):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.numero_pagina = numero_pagina
    
    def titulos(self):
        return self.titulo
    def autor(self):
        return self.autor
    def genero(self):
        return self.genero
    def numero_pagina(self):
        return self.numero_pagina

    def establecer_titulo(self,titulo):
        self.titulo = titulo
    def establecer_autor(self,autor):
        self.autor = autor
    def establecer_genero(self,genero):
        self.genero = genero
    def establecer_numero_pagina(self, numero_pagina):
        self.numero_pagina = numero_pagina

    def comprobar(self):
        if(self.genero == "Ficcion"):
            return "es ficcion"
        return "no es ficcion"
        
if __name__ == "__main__":

    empleado1= Libro("Harry Potter","J.K.Rowling","Ficcion",15)
    
    print(f"Titulo: {empleado1.titulo}")
    print(f"Autor: {empleado1.autor}")
    print(f"Genero: {empleado1.genero}")
    print(f"Numero_pagina: {empleado1.numero_pagina}")
    print(f"¿El libro es ficcion? {empleado1.comprobar()}")
    
    empleado1.establecer_titulo("Crimen y Castigo")
    empleado1.establecer_autor("Fiódor Dostoyevski")
    empleado1.establecer_genero("Policial")
    empleado1.establecer_numero_pagina(10)

    print("*Restablecer*")
    print(f"Titulo: {empleado1.titulo}")
    print(f"Autor: {empleado1.autor}")
    print(f"Genero: {empleado1.genero}")
    print(f"Numero_pagina: {empleado1.numero_pagina}")
    print(f"¿El libro es ficcion? {empleado1.comprobar()}")
