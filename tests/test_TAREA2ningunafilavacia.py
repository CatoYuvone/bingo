from src.bingo import carton

def test_no_filas_vacias():
    mi_carton = carton()
    contador_1 = 0
    contador_2 = 0
    contador_3 = 0 
    for celda_1 in mi_carton[0]:
        contador_1= contador_1 + celda_1
    for celda_2 in mi_carton[1]:
        contador_2= contador_2 + celda_1
    for celda_3 in mi_carton[2]:
        contador_3= contador_3 + celda_1
    assert (contador_1 * contador_2 * contador_3) > 0
