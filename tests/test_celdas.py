from src.bingo import carton
from src.bingo import validar_quince_numeros

def test_contar_celdas_ocupadas():
    micarton = carton()
    contador = 0
    for fila in micarton:
        for celda in fila:
            contador = contador + celda

    #Esperamos encontrar 15 celdas ocupadas.
    assert validar_quince_numeros(micarton) == True