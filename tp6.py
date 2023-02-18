class vehiculo():
    def color(self):
        self.color = "verde"

    def ruedas(self):
        self.ruedas = 4

    def puertas(self):
        self.puertas = 5


class Coche(vehiculo):
    def velocidad(self):
        self.velocidad = 0
    

    def cilindrada(self):
        self.cilindrada = 0

p = Coche()
p.cilindrada()
p.color()
p.puertas()
p.velocidad()
p.ruedas()

print(p.color)
print(p.cilindrada)
print(p.puertas)
print(p.ruedas)
print(p.velocidad)