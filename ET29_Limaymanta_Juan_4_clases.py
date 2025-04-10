
class Rectángulo:
    def __init__(self,longitud,ancho):
        self.longitud = longitud
        self.ancho = ancho
    def log(self):
        return self.longitud
    def anc(self):
        return self.ancho
    def area(self):
        area = self.longitud * self.ancho
        return area
    def perim(self):
        perimetro = 2*self.longitud + 2*self.ancho
        return perimetro

if __name__ == "__main__":

    Rec= Rectángulo(10,5)
    print(f"Longitud: {Rec.log()}")
    print(f"Ancho: {Rec.anc()}")
    print(f"Area: {Rec.area()}")
    print(f"Perimetro: {Rec.perim()}")
