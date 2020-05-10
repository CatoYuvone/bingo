from src.bingo import carton

def test_casilas():
    mi_carton = carton() 
    contador = 0 
    fila_aux = [0,0,0,0,0,0,0,0,0]
    for fila in mi_carton:
        contador = 0
        for celda in fila:
            fila_aux[contador] = fila_aux[contador] + celda
            contador = contador + 1
    for celda_aux in fila_aux:
         assert celda_aux > 0

        