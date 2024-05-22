[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12412554&assignment_repo_type=AssignmentRepo)
# Práctica 8 - Perceptrón

## Autor: Arrieta Mancera Luis Sebastian

Para correr el programa es necesario activar el entorno virtual:

```bash
source myenv/bin/activate
```

Posicionate en la carpeta src y ejecuta el siguiente comando:

```bash
python3 Main.py
```

En caso de no funcionar este comando intenta ejecutarlo con `python`

```bash
python Main.py
```

Se hace uso de las librerias:

    - numpy
    - colorama

Al correr el programa se mostrara un menu que te guiará por el flujo del programa. Este consiste en elegir un perceptron (AND/OR), eligir uno de entre 5 conjuntos de entrenamiento e inmediatamente generar un reporte con informacion sobre el entrenamiento y prueba del perceptron:

    - Tipo de perceptron
    - Conjunto de entrenamiento
    - Pesos
    - Umbral
    - Conjunto de prueba
    - Resultados

Adicionamente muestra cuantas entradas se respondieron correctamente y cuales.

# Reporte:

### Conjuntos de entrenamiento:

**Conjunto 1**
```bash
[0 0 0]
[1 1 1]
```
**Conjunto 2**
```bash
[0 0 0]
[0 0 1]
[0 1 0]
[0 1 1]
[1 0 0]
[1 0 1]
[1 1 0]
[1 1 1]
```
**Conjunto 3**
```bash
[0 0 0]
[0 1 0]
[1 0 0]
[1 1 0]
```
**Conjunto 4**
```bash
[0 0 1]
[0 1 1]
[1 0 1]
[1 1 1]
```
**Conjunto 5**
```bash
[0 0 0]
[0 0 1]
[1 1 0]
[1 1 1]
```

## Perceptron AND y OR

Con el conjunto de prueba 1 el perceptron algunas veces aprende y en otras no, es cuestion de suerte debido al
conjunto de entrenamiento tan pequeño. Es el mismo caso para ambos perceptrones.

Con el conjunto de prueba 2 el perceptron la mayoria de las veces aprende, esto con 50 iteraciones. Sin embargo, con 100 iteraciones el perceptron lograba aprender el 100% de las veces, nunca se equivocaba. Es el mismo caso 
para ambos perceptrones.

Con el conjunto de prueba 3 el perceptron AND falla la moyoria de las veces. El perceptron OR la mayoria de las veces aprende.

Con el conjunto de prueba 4 el perceptron AND y OR aprenden por igual, algunas veces fallan.

Con el conjunto de prueba 5 el conjunto AND aprende más veces que el perceptron OR. Algunas veces fallan.

Agradecimientos al creador del siguiente video, que ayudo a reforzar mi conocimiento para el desarrollo de esta practica:
[Perceptron](https://www.youtube.com/watch?v=dkhXGTersP0&t=1215s)
