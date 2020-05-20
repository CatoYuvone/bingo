from src.bingo import carton
from src.bingo import avanzar_de_arriba_a_abajo

def test_ascendiente():
    carton =  (
        (1, 2, 3, 4, 0, 5, 6, 7, 8),
        (2, 5, 6, 0, 7, 0, 8, 0, 9), 
        (3, 0, 8, 14, 16, 67, 0, 0, 0)
      )
    assert avanzar_de_arriba_a_abajo(carton) == 1
    # Afirmo que los números de la columna asciendden de arriba a abajo