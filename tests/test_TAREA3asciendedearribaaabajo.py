from src.bingo import carton
from src.bingo import avanzar_de_arriba_a_abajo

def test_ascendiente():
    micarton = carton() 
    assert avanzar_de_arriba_a_abajo(micarton) == 1
    # Afirmo que los números de la columna ascienden de arriba a abajo