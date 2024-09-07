import pytest
from automovil import Automovil  
def test_acelerar():
    auto = Automovil(150, 0.1, 50)
    resultado = auto.acelerar()
    assert auto.velocidad == 10  
    assert resultado == "Velocidad actual: 10 km/h"

def test_frenar():
    auto = Automovil(150, 0.1, 50)
    auto.acelerar() 
    resultado = auto.frenar()
    assert auto.velocidad == 0  
    assert resultado == "Velocidad actual: 0 km/h"

def test_conducir_con_combustible():
    auto = Automovil(150, 0.1, 50)
    auto.acelerar()
    resultado = auto.conducir(100)
    assert auto.combustible == 40.0  
    assert resultado == "Has conducido 100 km. Combustible restante: 40.00 litros."

def test_conducir_sin_combustible():
    auto = Automovil(150, 0.1, 5)  
    auto.acelerar()
    resultado = auto.conducir(100)
    assert auto.combustible == 5  
    assert resultado == "No hay suficiente combustible para esa distancia."

def test_str():
    auto = Automovil(150, 0.1, 50)
    resultado = str(auto)
    assert "Automóvil:" in resultado