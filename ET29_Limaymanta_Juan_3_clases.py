
class Producto:
    def __init__(self,nombre,precio,stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    def nmbr(self):
        return self.nombre
    def prc(self):
        return self.precio
    def sck(self):
        return self.stock
    def cambiar_stock(self,stock):
        self.stock += stock

if __name__ == "__main__":

    Arroz = Producto("Arroz",100,50)
    print(f"Nombre:{Arroz.nmbr()}")
    print(f"Precio:{Arroz.prc()}")
    print(f"Stock: {Arroz.sck()}")
    stc=-10
    print("Se redujo la stock en 10")
    Arroz.cambiar_stock(stc)
    print(f"Nuevo stock: {Arroz.sck()}")
