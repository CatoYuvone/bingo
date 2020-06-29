from src.bingo import carton
from src.bingo import validar_no_columnas_totalmente_llenas

def test_no_tres_celdas_por_columna():
    micarton = carton()
    assert validar_no_columnas_totalmente_llenas(micarton) == 1