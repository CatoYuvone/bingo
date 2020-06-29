from src import bingo

micarton = (
      (0, 0, 0, 6, 0, 0, 0, 0, 0),
      (0, 0, 0, 4, 0, 0, 0, 0, 0),
      (0, 0, 0, 0, 0, 0, 0, 0, 0),
      (0, 0, 0, 0, 0, 43, 0, 0, 0)
)


def test_15_celdas():
    assert not bingo.validar_quince_numeros(micarton)