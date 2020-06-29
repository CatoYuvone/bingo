from src.bingo import carton
from src.bingo import validar_solo_tres_columnas_con_solo_una_celda_ocupada

def test_solo_tres_columnas_con_solo_una_celda():
    micarton = carton()
    assert validar_solo_tres_columnas_con_solo_una_celda_ocupada(micarton) == 1