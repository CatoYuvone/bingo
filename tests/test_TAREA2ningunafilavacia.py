from src.bingo import carton

def test_no_filas_vacias():
    mi_carton = carton()
    contador_1 = 0       
    contador_2 = 0
    contador_3 = 0      # Creo tres contadores auxiliares
    for celda_1 in mi_carton[0]:          # Recorro la primer fila del cartón
        contador_1= contador_1 + celda_1  # En el contador uno almaceno la suma de todas las celdas de la primer fila
    for celda_2 in mi_carton[1]:          # Recorro la segunda fila del cartón
        contador_2= contador_2 + celda_1  # En el contador dos almaceno la suma de todas las celdas de la segunda fila
    for celda_3 in mi_carton[2]:          # Recorro la tercer fila del cartón
        contador_3= contador_3 + celda_1  # En el contador tres almaceno la suma de todas las celdas de la tercer fila
    assert (contador_1 * contador_2 * contador_3) > 0 

# Afirmo que la multiplicación de los tres contadores sea mayor a cero, 
# O sea que no haya ningún contador igual a cero
# O sea que ninguna fila esté vacía
