
class Estudiante:
    def __init__(self,nombre,edad,carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.examenes = []
    def nombres(self):
        return self.nombre
    def edads(self):
        return self.edad
    def carreras(self):
        return self.carrera
    
    def establecer_nombres(self,nombre):
        self.nombre = nombre
    def establecer_edads(self,edad):
        self.edad = edad
    def establecer_carreras(self,carrera):
        self.carrera = carrera
        
    def agregar_nota(self,nota):
        self.examenes.append(nota)
    def calcular_nota(self):
        a=0
        if not self.examenes:
            return 0
        for n in self.examenes:
            a+=n
        return a/len(self.examenes)

if __name__ == "__main__":
    Alumno1= Estudiante("Jose",20,"Contabilidad")
    print(f"Nombre: {Alumno1.nombres()}")
    print(f"Edad: {Alumno1.edads()}")
    print(f"Carrera: {Alumno1.carreras()}")

    Alumno1.agregar_nota(10)
    Alumno1.agregar_nota(8)
    Alumno1.agregar_nota(7)
    #recordatorio: .2f en los print formatea los números flotantes y muestra solo dos cifras decimales
    print(f"La nota de {Alumno1.nombres()} es {Alumno1.calcular_nota():.2f}")
    
    Alumno1.establecer_nombres("Carlos")
    Alumno1.establecer_edads(21)
    Alumno1.establecer_carreras("Economia")
    print("*Restablecer*")
    print(f"Nombre: {Alumno1.nombres()}")
    print(f"Edad: {Alumno1.edads()}")
    print(f"Carrera: {Alumno1.carreras()}")
