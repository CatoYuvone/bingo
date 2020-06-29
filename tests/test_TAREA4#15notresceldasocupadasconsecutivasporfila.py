from src.bingo import carton
from src.bingo import validar_no_tres_celdas_ocupadas_consecutivas_por_fila

def test_no_tres_celda_ocupadas_consecutivas():
    micarton = carton()
    assert validar_no_tres_celdas_ocupadas_consecutivas_por_fila(micarton) == 1