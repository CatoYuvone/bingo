[![Build Status](https://travis-ci.org/CatoYuvone/bingo.svg?branch=master)](https://travis-ci.org/CatoYuvone/bingo)
[![Coverage Status](https://coveralls.io/repos/github/CatoYuvone/bingo/badge.svg?branch=master)](https://coveralls.io/github/CatoYuvone/bingo?branch=master)
[![Scrutinizer Code Quality](https://scrutinizer-ci.com/g/CatoYuvone/bingo/badges/quality-score.png?b=master)](https://scrutinizer-ci.com/g/CatoYuvone/bingo/?branch=master)

# BINGO
En este repositorio encuéntrase código en Python que genera un cartón de bingo. Este proyecto fue hecho para la materia "Adaptación al Ambiente de Trabajo", de 6ª Informática del Instituo Politécnico Superior "General San Martín" de Rosario, 2020.

## Condiciones para cartón válido
Un cartón considérase válido si y sólo si se cumplen las siguientes condiciones:
- Los números del cartón encuéntranse en el rango 1 a 90.
- Cada columna de un cartón (contando de izquierda a derecha) contiene números que van del 1 al 9, 10 al 19, 20 al 29 ..., 70 al 79 y 80 al 90.
- No hay números repetidos en el cartón.
- Cada fila de un cartón tiene exactamente 5 celdas ocupadas.
- Cada cartón es una matrix de 3 x 9.
- Cada cartón tiene 15 celdas ocupadas.
- Los números de las columnas izquierdas son menores que los de las columnas a la derecha.
- Para una misma columna, sus números están ordenados de menor a mayor de arriba hacia abajo.
- No pueden existir columnas vacias.
- No pueden existir columnas con sus tres celdas ocupadas.
- Cada cartón debe tener 3 y solo 3 columas con solo una celda ocupada.
- En una fila no existen más de dos celdas vacías consecutivas.
- En una fila no existen más de dos celdas ocupadas consecutivas.

## USO
Para clonar el repositorio:
```
https://github.com/CatoYuvone/bingo.git
```
Para ejecutar el código:
```
python bingo_web.py
```
Y abrir el archivo bingo.html para ver el resultado.

Para ver el resultado en consola:
```
python carton_bingo_consola.py
```

## Ejemplo resultado
### Web
![Bingo Web](Images/Bingo_web.png)

### Ejemplo consola
```
[3, 11, 0, 37, 0, 0, 61, 71, 0]
[6, 12, 0, 0, 45, 0, 0, 75, 81]
[0, 0, 24, 30, 0, 53, 64, 0, 83]
```

## LICENCIA
Este repositorio está bajo la licencia GPU GPLv3. <br>
Para más información sobre esta licencia consultar el archivo "LICENSE.md".
