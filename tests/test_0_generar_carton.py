from src import bingo

mi_carton = bingo.intentoCartonRePro()

def test_15_celdas():
    assert bingo.validar_quince_numeros(mi_carton)

bingo.imprimirCarton(mi_carton)