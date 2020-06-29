from src.bingo import carton
from src.bingo import validar_no_tres_celdas_vacias_consecutivas_por_fila

def test_no_tres_celda_vacias_consecutivas():
    micarton = carton()
    assert validar_no_tres_celdas_vacias_consecutivas_por_fila(micarton) == 1