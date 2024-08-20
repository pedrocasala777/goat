class auto:
    ruedas=" "
    puertas=" "
    volante=" "
    marca= " "
    año= " "
    def __init__(self, ruedas, puertas, volante, marca, año):
      self.ruedas = ruedas
      self.puertas = puertas
      self.volante= volante
      self.marca= marca
      self.año= año
auto1=auto("4", "3","si", "Chevrolet corsa", "2008")
auto2=auto("2","0","no", "Zanella ZR 150", "2022")

print(auto1.marca)
print(auto2.año)