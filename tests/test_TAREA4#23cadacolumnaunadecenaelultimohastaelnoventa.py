from src.bingo import carton
from src.bingo import validar_cada_columna_una_decena_hasta_el_90

def test_cada_columna_una_decena():
    micarton = carton()
    assert validar_cada_columna_una_decena_hasta_el_90(micarton) == 1