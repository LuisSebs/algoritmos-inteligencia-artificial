# Practica02: Gatos

### Alumno: Luis Sebastian Arrieta Mancera (318174116)

# Generar sucesores sin simetrías:

EL pdf especifica que corramos la simulación ***sin considerar*** simetrías y ***considerando*** simetrías, detallando las observaciones. Antes que nada para ambos comportamientos se implementaron sus correspondientes métodos `generaSucesoresConSimetrias()` y `generaSucesoresSinSimetrias()`.

<p align="center">
<img width="80%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/1.png"/>
</p>

La observación más notoria es que la cantidad de nodos en el arbol incrementa bastante a comparación de cuando se consideran simetrias, por lo que la computadora se vuelve más lenta, o eso ocurrió en mi caso, tardo algunos segundos en mostrar los últimos niveles del arbol (7, 8 y 9)
 
<p align="center"> 
<img width="50%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/2.png"/>
</p>

# Genera sucesores con simetrías:

Por default el metodo `generaSucesoresConSimetrias()` se encuentra descomentado en el método `generaSucesores()` por lo que cambiar entre generar simetrias y no generarlas solo es comentar y descomentar el metodo correspondiente.

<p align="center">
<img width="80%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/3.png"/>
</p>

Al considerar simetrías la cantidad de tableros generados se reduce significativamente.

<p align="center">
<img width="50%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/4.png"/>
</p>

# Lógica de la resolución de la práctica

Considero importante describir la resolución de la pŕactica, ya que a falta de pruebas o imagenes para validar los resultados correctos, de esta forma se puede argumentar el entendimiento de los resultados esperados por el alumno.

Nos piden implementar los métodos:

- boolean esSimétricoDiagonalInvertida
- boolean esSimétricoDiagonal
- boolean esSimétricoVerticalmente
- boolean esSimétricoHorizontalmente
- boolean esSimétrico90
- boolean esSimétrico180
- boolean esSimétrico270

Para implementar cada metodo se considero que un tablero de gato es un arreglo bidimensional de 3x3 de manera que los indices de cada casilla son los siguientes:

<p align="center">
<img width="50%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/gato.png">
</p>

Donde los indices en color <span style="color: #FFD43B">Amarillo</span> corresponden a la fila y los indices en color <span style="color: #306998">Azul</span> corresponden a la columna.

Para saber si dos casillas eran iguales bajo alguna de las simetrías lo que se realizó fue dibujar en una hoja de papel un tablero de gato, y en cada casilla se dibujaron los indices correspondientes a cada casilla justo como en la imagen anterior. Despúes se recortó la hoja y se procedió a realizar las tranformaciones solicitadas. Al rotar la hoja de paperl en `90`, `180` y `270` los indices se podrían ver claramente, pero para las transformaciones `horizontal`, `vertical`, `diagonal` y `diagonal invertida` se tenia que voltear la hoja, por lo que no se podian ver los indices a menos que usaras un marcador o lo pusieras a contral luz, al hacer esto se podían ver claramente los indices. 

Nos basamos en la siguiente imagen para realizar las transformaciones:

- a   = 90°
- a²  = 180°
- a³  = 270°
- ba³ = ab = diagonal invertida \
- ba  = a³b = diagonal / 
- b = vertical
- a²b = ba² = horizontal

<p align="center">
<img src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/referencia.png"/>
</p>

Los siguientes gift muestran las transformaciones solicitadas y los indices con los que hay que comparar los indices del tablero del gato previamente mostrado. 

Cabe aclarar que los gift's fueron realizados por mí mismo para clarificar el proceso que se siguió para llevar a cabo las transformaciones, estas simulan las simetrías aplicadas a la hoja de papel, este proceso fue el que se siguio para determinar que casillas de un tablero tenemos que comparar con otro, la posicion final de los indices en el tablero son las posiciones con las que tenemos que comparar.

| 90°  | 180° | 270° |
| ------------- |:-------------:| :-------------: |
|<img width="100%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/gato90.gif"/>|<img width="100%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/gato180.gif"/>|<img width="100%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/gato270.gif"/>|

| Horizontal  | Vertical |
| ------------- |:-------------:|
|<img width="70%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/gatoHorizontal.gif"/>|<img width="70%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/gatoVertical.gif"/>|

| Diagonal  | Diagonal Invertida |
| ------------- |:-------------:|
|<img width="70%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/gatoDiagonal.gif"/>|<img width="70%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/gatoDiagonalInvertida.gif"/>|

Una vez visualizado esto solo se procedio a copiar los indices que aparecian al final de los gifts para compararlos con los del otro gato.


<div align="center">
<img width="100%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/s1.png"/>
</div>

<div align="center">
<img width="100%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/s2.png"/>
</div>

<div align="center">
<img width="100%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/s3.png"/>
</div>

<div align="center">
<img width="100%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/s4.png"/>
</div>

<div align="center">
<img width="100%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/s5.png"/>
</div>

<div align="center">
<img width="100%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/s6.png"/>
</div>

<div align="center">
<img width="100%" src="https://raw.githubusercontent.com/LuisSebs/imgs/main/escuela/inteligencia-artificial/practica02/s7.png"/>
</div>

[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=11688975&assignment_repo_type=AssignmentRepo)

# Práctica 2 - Estados y espacio de búsqueda.
### Inteligencia Artificial 2021-2

Generación de los posibles estados del gato. 

Debe implementar los métodos que se le indican. Para más información consulte el pdf que se incluye.
Es el código base para la práctica correspondiente. Está prohibido compartir soluciones con compañeros o estudiantes fuera del curso.

## Ejecución
Para compilar y ejecutar este código desde la terminal, se recomiendan los comandos siguientes:

```
javac -d ./classes -cp lib/core.jar:. gatos/*.java
java -cp ./classes:lib/core.jar gatos.Gatos
```


