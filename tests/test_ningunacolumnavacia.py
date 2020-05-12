from src.bingo import carton

def test_no_columnas_vacias():
    mi_carton = carton() 
    contador = 0 
    fila_aux = [0,0,0,0,0,0,0,0,0]  # Creo una fila auxiliar
    for fila in mi_carton:          # Recorro el cartón
        contador = 0                # Pongo el contador en cero antes de recorrer cada fila
        for celda in fila:          # Recorro las filas del cartón
            fila_aux[contador] = fila_aux[contador] + celda    # El elemento en la posición "contador" se le suma la celda número "contador"
            contador = contador + 1  # Sumole 1 al valor de contador
    for celda_aux in fila_aux:       # Recorro la fila auxiliar
         assert celda_aux > 0        # Afirmo que cada celda de la fila auxiliar es mayor a 0
                                     # O sea que la suma de las celdas de cada columna ddel cartón
                                     # es mayor  a 0, o sea que cada columna tiene al menos una
                                     # celda ocupada
                                     