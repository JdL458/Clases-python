
class Tienda:
    def __init__(self,nombre):
        self.nombre= nombre
        self.lista=[]
    def agregar(self,producto):
        self.lista.append(producto)
    def quitar(self,producto):
        if(producto in self.lista):
            self.lista.remove(producto)
    def mostrar(self):
        return self.lista

if __name__  == "__main__":

    tienda1=Tienda("Argenchino")

    tienda1.agregar("Pan")
    tienda1.agregar("Huevo")

    print(f"Lista: {tienda1.mostrar()}")

    tienda1.quitar("Pan")

    print(f"Lista: {tienda1.mostrar()}")
