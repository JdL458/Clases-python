
class Coche:
    def __init__(self,marca,modelo,año):
        self.marca = marca
        self.modelo = modelo
        self.años = año

    def mrca(self):
        return self.marca
    def mdl(self):
        return self.modelo
    def añ(self):
        return self.años
    def mostraraños(self):
        años = 2025 - self.años
        return años
    
if __name__ == "__main__":

    Coche1 = Coche("Toyota","GR Supra",2019)
    
    print(f"Marca: {Coche1.mrca()}")
    print(f"Modelo: {Coche1.mdl()}")
    print(f"Año de creacion: {Coche1.añ()}")
    print(f"Años desde que se fabrico: {Coche1.mostraraños()}")
