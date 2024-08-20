class jugador:
    edad=" "
    equipo=" "
    altura=" "
    velocidadKM= " "
    categoria= " "
    nombre= " "
    def __init__(self, edad, equipo, altura, velocidadKM, categoria, nombre):
      self.edad= edad
      self.equipo = equipo
      self.altura= altura
      self.velocidadKM= velocidadKM
      self.categoria= categoria
      self.nombre= nombre
     
jugador1=jugador("27", "Sheriff Tarastol","1.82", "20", "1996", "Peter Wilson")
jugador2=jugador("36", "Inter de Miami","1.70", "20", "1987", "Lionel messi")

print(jugador1.nombre)
print(jugador2.edad)