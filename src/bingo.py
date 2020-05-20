
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
    for fila in carton:
        celda_aux = 0
        for celda in fila:
            if celda != 0:
               if celda <= celda_aux:
                  bandera = 0
               celda_aux = celda

    return bandera
             