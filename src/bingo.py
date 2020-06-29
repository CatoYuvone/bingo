
# Los 0 representan celdas vacías en el cartón
# Los 1 representan celdas ocupadas en el cartón

def carton():
    carton = (
       (0,0,27,36,0,56,62,0,80),
       (0,11,0,37,41,0,0,75,88),
       (3,12,0,0,48,0,65,76,0)
    )
    return carton


def validar_quince_numeros(carton):
    celdas_vacias = 0
    for fila in carton:
        for celda in fila:
            if celda == 0:
               celdas_vacias = celdas_vacias + 1
           
    return celdas_vacias == 27 -15



def avanzar_de_izquierda_a_derecha(carton):
    bandera = 1
    for fila in carton:                           # Recorro el carton por filas
        celda_aux = 0                             # Igualo celda_aux a 0       
        for celda in fila:                        # Recorro la fila por celdas
            if celda != 0:                        # Si la celda no está vacía
               if celda <= celda_aux:             # Comparo celda con celda_aux
                  bandera = 0                     # Si la celda es menor o igual a celda_aux igualo bandera a 0
               celda_aux = celda                  # Para comparar la celda con la anterior celda de la fila             

    return bandera                                # Retorno 1 si en ninguna fila hay una celda con un número menor o igual al número de la celda de su izquierda, 0 en caso contrario
 


def avanzar_de_arriba_a_abajo(carton):
    fila = 0
    columna = 0
    bandera = 1
    for fila in range(0, 2):
        for columna in range(0, 9):
            if carton[fila][columna] >= carton[fila+1][columna]  and carton[fila][columna] != 0 and carton[fila+1][columna] != 0:        # Si la celda de arriba es mayor o igual que la de abajo y las dos están ocupadas 
               bandera = 0                                              # Entonces bandera = 0
            columna = columna + 1                                       # Súmole uno al contador de columnas
        fila = fila + 1                                                 # Súmole  al contador de filas
    
    return bandera   # Retorno 0 si alguna celda no es menor que la celda de debajo suya, 1 en caso contrario                  
             

