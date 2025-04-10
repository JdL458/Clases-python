
class Círculo:
    def __init__(self,radio,diametro):
        self.radio = radio
        self.diametro = diametro
    def rd(self):
        return self.radio
    def dia(self):
        return self.diametro
    def area(self):
        area = 3.14*(self.radio*self.radio)
        return round(area)
    def curcuferencia(self):
        perimetro = 3.14*self.diametro
        return round(perimetro)

if __name__ == "__main__":

    Circ = Círculo(10,20)
    print(f"Radio: {Circ.rd()}")
    print(f"Diametro: {Circ.dia()}")
    print(f"Area: {Circ.area()}")
    print(f"Circuferencia: {Circ.curcuferencia()}")
