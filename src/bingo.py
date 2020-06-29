import random
# Los 0 representan celdas vacías en el cartón
# Los 1 representan celdas ocupadas en el cartón

def carton():
    carton = (
       (0,0,27,36,0,56,62,0,88),
       (0,11,0,37,41,0,0,73,90),
       (9,12,0,0,48,0,65,79,0)
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
         

def validar_5_celdas_por_fila(carton):
    bandera = 0
    for fila in carton: 
        contador = 0
        for celda in fila:
            if celda != 0:
                contador = contador + 1
        if contador == 5:
            bandera = bandera + 1
    if bandera != 3:
         bandera = 0
    if bandera == 3:
         bandera = 1
    return bandera


def validar_matriz_3x9(carton):
    bandera1 = 0
    bandera2 = 0
    superbandera = 0
    contador2 = 0
    for fila in carton:
         contador1 = 0
         for celda in fila:
           contador1 = contador1 +1
         if contador1 == 9:
             bandera1 = bandera1 + 1
         contador2 = contador2 + 1
    if contador2 == 3:
       bandera2 = bandera2 + 1
    if bandera1 == 3 and bandera2 == 1:
       superbandera = 1
    return superbandera


def validar_no_columnas_vacias(carton):
    fila = 0
    columna = 0
    bandera = 1
    for fila in range(0, 1):
         for columna in range(0,9):
              if carton[fila][columna] == 0 and carton[fila+1][columna] == 0 and carton[fila+2][columna] == 0:
                  bandera = 0
              columna = columna + 1
         fila = fila + 1
    return bandera


def validar_no_columnas_totalmente_llenas(carton):
    fila = 0
    columna = 0
    bandera = 1
    for fila in range(0, 1):
         for columna in range(0,9):
              if carton[fila][columna] > 0 and carton[fila+1][columna] > 0 and carton[fila+2][columna] > 0:
                  bandera = 0
              columna = columna + 1
         fila = fila + 1
    return bandera  


def validar_solo_tres_columnas_con_solo_una_celda_ocupada(carton):
    fila = 0
    columna = 0
    contador = 0
    bandera = 0
    for fila in range(0, 1):
         for columna in range(0,9):
             if (carton[fila][columna] + carton[fila+1][columna] + carton[fila+2][columna]) == max([carton[fila][columna], carton[fila+1][columna], carton[fila+2][columna]]):
                contador= contador + 1
             columna = columna +1
         fila = fila +1
    if contador == 3:
       bandera = 1
    return bandera


def validar_no_tres_celdas_vacias_consecutivas_por_fila(carton):
    bandera = 1
    for fila in carton:
        consec = 0
        for celda in fila:
            if celda == 0:
               consec = consec +1
            elif celda > 0:
               consec = 0
            if consec > 2:
               bandera = 0
    return bandera

            

def validar_no_tres_celdas_ocupadas_consecutivas_por_fila(carton):
    bandera = 1
    for fila in carton:
        consec = 0
        for celda in fila:
            if celda > 0:
               consec = consec +1
            elif celda == 0:
               consec = 0
            if consec > 2:
               bandera = 0
    return bandera

     

def validar_cada_columna_una_decena_hasta_el_90(carton):   
    fila = 0
    columna = 0 
    bandera = 1
    for fila in range(0, 3):
        for columna in range(0,9): 
            if columna == 0:
                  if (carton[fila][columna] != 0) and 0 >= carton[fila][columna] >= 9:
                      bandera = 0
            elif  0 < columna < 8:
                  if (carton[fila][columna] != 0) and ((10 * (columna)) > carton[fila][columna]  or carton[fila][columna] > ((10 * columna) + 9)):
                      bandera = 0
            elif columna == 8:
                  if (carton[fila][columna] != 0) and 80 > carton[fila][columna] > 90:
                      bandera = 0
    return bandera
            

def intentoCarton():
    contador = 0
    carton = [
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    numerosCarton = 0

    while numerosCarton < 15:
          contador = contador + 1
          if (contador == 50): 
             return intentoCarton()

          numero = random.randint (1,90)

          columna = numero // 10
          if (columna == 9):
             columna = 8
          huecos = 0
          for i in range(3):
              if carton[columna][i] == 0:
                 huecos = huecos + 1 
              if carton[columna][i] == numero:
                 huecos = 0
                 break
          if huecos < 2:
             continue
          fila = 0
          for j in range(3):
              huecos = 0
              for i in range(9):
                  if (carton[i][fila] == 0):
                     huecos = huecos + 1
              if huecos < 5 or carton[columna][fila] != 0:
                   fila = fila + 1
              else:
                   break
              if (fila == 3):
                 continue

              carton[columna][fila] = numero
              numeroCarton = numeroCarton + 1
              contador = 0
      
    for x in range(9):
        huecos = 0 
        for y in range(3):
            if carton[x][y] == 0:
               huecos = huecos + 1
        if huecos == 3:
            return intentoCarton() 
    return carton


def intentoCartonPro():
    fila = 0
    columna = 0
    carton = intenntoCarton()
    cartonpro = [
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    ]
    for columna in range(0,9):
        for fila in range(0,3):
            cartonpro[fila][columna] = carton[columna][fila]
    return cartonpro


def intentoCartonRePro():
    contar = 0
    for contar in range(0, 100)
        carton = intentoCartonPro()
    contar = contar + 1
    if avanzar_de_izquierda_a_derecha(carton) == avanzar_de_arriba_a_abajo(carton) == validar_5_celdas_por_fila(carton) == validar_matriz_3x9(carton) == validar_no_columnas_vacias(carton) == validar_no_columnas_totalmente_llenas(carton) == validar_solo_tres_columnas_con_solo_una_celda_ocupada(carton) == validar_no_tres_celdas_vacias_consecutivas_por_fila(carton) == validar_no_tres_celdas_ocupadas_consecutivas_por_fila(carton) == validar_cada_columna_una_decena_hasta_el_90(carton) == 1 and validar_quince_numeros(carton):
       print (contar)
       break
    else:
       print ("Intentar después")
    return carton


