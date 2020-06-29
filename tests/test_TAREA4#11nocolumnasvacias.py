from src.bingo import carton
from src.bingo import validar_no_columnas_vacias

def test_nocolumnasvacias():
    micarton = carton()
    assert validar_no_columnas_vacias(micarton) == 1