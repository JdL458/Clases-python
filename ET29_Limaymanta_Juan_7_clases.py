
class Banco:
    def __init__(self,nombre,interes):
        self.nombre = nombre
        self.interes = interes
    def nombres(self):
        return self.nombre

    def calcular_interes(self,dinero, años):
        monto = dinero*(1 + self.interes/100) ** años
        return monto
    def duplicar(self):
        d= 72 /(self.interes)
        return d
if __name__ == "__main__":

    Banco1= Banco("Naranja",20.0)
    dinero= 1000
    años= 3.7
    
    print(f"Nombre del banco: {Banco1.nombre}")
    print(f"Tasa de interes (años): {Banco1.calcular_interes(dinero,años):.1f}")
    print(f"Tiempo estimado para duplicarlo (años): {Banco1.duplicar():.1f}")
