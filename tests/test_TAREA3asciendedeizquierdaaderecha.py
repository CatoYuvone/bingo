from src.bingo import carton
from src.bingo import avanzar_de_izquierda_a_derecha

def test_ascendiente():
    micarton = carton()
    assert avanzar_de_izquierda_a_derecha(micarton) == 1
    # Afirmo que los números de la fila asciendan de izquierda a derecha
