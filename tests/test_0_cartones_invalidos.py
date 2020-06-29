from src import bingo

micarton = (
      (0, 0, 0, 6, 0, 90, 0, 2, 0),
      (0, 0, 0, 4, 0, 67, 0, 0, 0),
      (0, 0, 0, 0, 0, 44, 0, 0, 0),
      (0, 5, 5, 5, 0, 43, 0, 0, 0)
)


def test_15_celdas():
    assert not bingo.validar_quince_numeros(micarton)

def test_izq_a_der():
    assert bingo.avanzar_de_izquierda_a_derecha(micarton) != 1

def test_arriba_a_abajo():
    assert bingo.avanzar_de_arriba_a_abajo(micarton) != 1

def test_5_celdas_por_fila():
    assert bingo.validar_5_celdas_por_fila(micarton) != 1

def test_matriz_3x9():
    assert bingo.validar_matriz_3x9(micarton) != 1

def test_no_columnas_vacias():
    assert bingo.validar_no_columnas_vacias(micarton) != 1

def test_no_columnas_llenas():
    assert bingo.validar_no_columnas_totalmente_llenas(micarton) != 1

def test_solo_tres_columnas_con_solo_una_celda_ocupada():
    assert bingo.validar_solo_tres_columnas_con_solo_una_celda_ocupada(micarton) != 1

def test_no_tres_celdas_vacías_consecutivas():
    assert bingo.validar_no_tres_celdas_vacias_consecutivas_por_fila(micarton) != 1

def test_no_tres_celdas_ocupadas_consecutivas():
    assert bingo.validar_no_tres_celdas_ocupadas_consecutivas_por_fila(micarton) != 1

def test_cada_columna_una_decena():
    assert bingo.validar_cada_columna_una_decena_hasta_el_90(micarton) != 1
