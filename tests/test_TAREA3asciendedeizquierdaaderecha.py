from src.bingo import carton
from src.bingo import avanzar_de_izquierda_a_derecha

def test_ascendiente():
    carton =  (
        (1, 2, 3, 4, 0, 5, 6, 7, 8),
        (1, 5, 6, 0, 7, 0, 8, 0, 9), 
        (3, 0, 5, 14, 16, 67, 0, 0, 0)
      )
    assert avanzar_de_izquierda_a_derecha(carton) == 1