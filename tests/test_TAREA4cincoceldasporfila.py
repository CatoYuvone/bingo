from src.bingo import carton
from src.bingo import validar_5_celdas_por_fila

def test_5porfila():
    micarton = carton()
    assert validar_5_celdas_por_fila(micarton) == 1
