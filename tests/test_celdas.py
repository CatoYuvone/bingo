from src.bingo import carton
from src.bingo import validar_quince_numeros

def test_contar_celdas_ocupadas():
    carton =  (
       (1, 0, 1, 1, 0, 0, 0, 0, 1),
       (1, 1, 1, 0, 1, 0, 1, 1, 1),
       (1, 0, 0, 1, 0, 1, 0, 1, 0)
    )
    contador = 0
    for fila in carton:
        for celda in fila:
            contador = contador + celda

    #Esperamos encontrar 15 celdas ocupadas.
    assert validar_quince_numeros(carton) == True