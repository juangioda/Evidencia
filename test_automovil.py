import pytest
from automovil import Automovil  # Asegúrate de que `automovil.py` esté en el mismo directorio

def test_acelerar():
    auto = Automovil(150, 0.1, 50)
    resultado = auto.acelerar()
    assert auto.velocidad == 10  # La velocidad inicial es 0, así que debe aumentar a 10
    assert resultado == "Velocidad actual: 10 km/h"

def test_frenar():
    auto = Automovil(150, 0.1, 50)
    auto.acelerar()  # Subimos la velocidad a 10 km/h
    resultado = auto.frenar()
    assert auto.velocidad == 0  # Frenamos y debe bajar a 0
    assert resultado == "Velocidad actual: 0 km/h"

def test_conducir_con_combustible():
    auto = Automovil(150, 0.1, 50)
    auto.acelerar()
    resultado = auto.conducir(100)
    assert auto.combustible == 40.0  # 100 km * 0.1 litros/km = 10 litros consumidos
    assert resultado == "Has conducido 100 km. Combustible restante: 40.00 litros."

def test_conducir_sin_combustible():
    auto = Automovil(150, 0.1, 5)  # Solo 5 litros de combustible
    auto.acelerar()
    resultado = auto.conducir(100)
    assert auto.combustible == 5  # No debe cambiar porque no hay suficiente combustible
    assert resultado == "No hay suficiente combustible para esa distancia."

def test_str():
    auto = Automovil(150, 0.1, 50)
    resultado = str(auto)
    assert "Automóvil:" in resultado