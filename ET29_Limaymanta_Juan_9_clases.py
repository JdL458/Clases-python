
class Empleado:
    def __init__(self,nombre,edad,salario,cargo):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargo = cargo
    
    def nombres(self):
        return self.nombre
    def edad(self):
        return self.edad
    def salario(self):
        return self.salario
    def cargo(self):
        return self.cargo

    def establecer_nombre(self,nombre):
        self.nombre = nombre
    def establecer_edad(self,edad):
        self.edad = edad
    def establecer_salario(self,salario):
        self.salario = salario
    def establecer_cargo(self, cargo):
        self.cargo = cargo
    
    def calcular(self):
        return self.salario*12
    
if __name__ == "__main__":

    empleado1= Empleado("Mauricio",20,1000,"Contador")
    
    print(f"Nombre: {empleado1.nombre}")
    print(f"Edad: {empleado1.edad}")
    print(f"Salario: {empleado1.salario}")
    print(f"Cargo: {empleado1.cargo}")
    print(f"Salario Anual {empleado1.calcular()}")

    empleado1.establecer_nombre("Anuel")
    empleado1.establecer_edad(23)
    empleado1.establecer_salario(1500)
    empleado1.establecer_cargo("Recepcionista")

    print("*Restablecer*")
    print(f"Nombre: {empleado1.nombre}")
    print(f"Edad: {empleado1.edad}")
    print(f"Salario: {empleado1.salario}")
    print(f"Cargo: {empleado1.cargo}")
