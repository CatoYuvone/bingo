
# Los 0 representan celdas vacías en el cartón
# Los 1 representan celdas ocupadas en el cartón

def carton():
    carton = (
       (1,0,0,1,1,0,1,0,1),
       (0,1,1,1,0,1,1,1,0),
       (0,1,0,0,1,1,0,1,0)
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
       celda_aux = 0                              # Igualo celda_aux a 0       
        for celda in fila:                        # Recorro la fila por celdas
            if celda != 0:                        # Si la celda no está vacía
               if celda <= celda_aux:             # Comparo celda con celda_aux
                  bandera = 0                     # Si la celda es menor o igual a celda_aux igualo bandera a 0
               celda_aux = celda                  # Para comparar la celda con la anterior celda de la fila             

    return bandera                                # Retorno 1 si en ninguna fila hay una celda con un número menor o igual al número de la celda de su izquierda, 0 en caso contrario
 
             