class Jugador:
    def __init__(self,equipo,nombre,edad,altura,color):
        self.equipo=equipo
        self.nombre=nombre
        self.edad=edad
        self.altura=altura
        self.color=color

p1=Jugador("A","jhon","36","2.0","rojo")
p2=Jugador("B","Andres","37","2.1","blanco")
p3=Jugador("C","Julian","38","2.0","amarillo")

print(p1.equipo)
print(p2.nombre)
print(p1.edad)
        
