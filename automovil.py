class Automovil:
    def __init__(self, max_velocidad, consumo_por_km, combustible):
        self.velocidad = 0  
        self.max_velocidad = max_velocidad
        self.consumo_por_km = consumo_por_km 
        self.combustible = combustible  

    def acelerar(self):
        if self.velocidad + 10 <= self.max_velocidad:
            self.velocidad += 10
        else:
            self.velocidad = self.max_velocidad
        return f"Velocidad actual: {self.velocidad} km/h"

    def frenar(self):
        if self.velocidad - 15 >= 0:
            self.velocidad -= 15
        else:
            self.velocidad = 0
        return f"Velocidad actual: {self.velocidad} km/h"

    def conducir(self, distancia):
        consumo = self.consumo_por_km * distancia
        if consumo <= self.combustible:
            self.combustible -= consumo
            return f"Has conducido {distancia} km. Combustible restante: {self.combustible:.2f} litros."
        else:
            return "No hay suficiente combustible para esa distancia."

    def __str__(self):
        return f"Automóvil: Velocidad: {self.velocidad} km/h, Combustible: {self.combustible:.2f} litros"