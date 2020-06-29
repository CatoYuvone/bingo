from src.bingo import carton
from src.bingo import validar_matriz_3x9

def test_matriz3x9():
    micarton = carton()
    assert validar_matriz_3x9(micarton) == 1
