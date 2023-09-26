class Personaje:
    nombre = "John Doe"
    fuerza = 0
    inteligencia = 0
    defensa = 0
    vida = 0

    def __init__ (self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre
        self.fuerza
        self.inteligencia
        self.defensa
        self.vida

    def atributos(self):
        print(self.nombre, ":", sep="")
        print("Fuerza", self.fuerza)
        print("inteligencia", self.inteligencia)
        print("defensa", self.defensa)
        print("vida", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza = self.fuerza + fuerza
        self.inteligencia = self.inteligencia + inteligencia
        self.defensa = self.defensa + inteligencia
    
if __name__ == "__main__":
    mi_personaje = Personaje("And", 10, 7, 5, 100)
    mi_personaje.atributos()
    #subir de nivel
    mi_personaje.subir_nivel(3, 5, 8)
    mi_personaje.atributos