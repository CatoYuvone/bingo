from src import bingo

micarton = bingo.intentoCartonRePro()

def test_15_celdas():
    assert bingo.validar_quince_numeros(micarton)

bingo.imprimirCarton(mi_carton)