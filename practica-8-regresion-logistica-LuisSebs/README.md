[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-718a45dd9cf7e7f842a935f5ebbe5719a5e09af4491e668f4dbf3b35d5cca122.svg)](https://classroom.github.com/online_ide?assignment_repo_id=12535949&assignment_repo_type=AssignmentRepo)
# Práctica 8 - Regresión Logística

Para ejecutar el programa intenta con alguno de los siguientes comandos:

```bash
python3 LogisticRegresion.py

python LogisticRegresion.py
```

Esto mostrará en terminal la clasificación de la tabla de verdad AND
con el modelo de regresión logística lineal.

# Comparación con el Perceptrón

## Representación de los datos

La representación de los datos de entrenamiento en ambos modelos (modelo de regresión logística lineal y perceptrón) es la misma, consiste en un arreglo de arreglos que representan las **x's** 
y un arreglo unidimensional para las clases, i.e. los valores esperados.

En cuanto a la representación de resultados, hay pequeñas diferencias, en el modelo de regresión logística dado un conjunto de entradas, se calculan las probabilidades de pertenecer a una clase
o no y en base a esta probabilidad se le asigna un valor 0 o 1. Mientras que en el perceptrón se puede regresan valores de clasificación directamente dada la función de activación.

## ¿Cuál fue más fácil/claro?

En lo personal el perceptrón, me pareción más sencillo de implementar y entender, dado que no hay mucha teoría por detrás a comparación del modelo de regresión incluido en esta práctica. Sin embargo, me parece un modelo bastante más preciso para este problema de clasificar valores de la tabla de verdad del AND.

## ¿En qué se parecen?

Ambos son modelos supervisados que se utilizan para problemas de clasificación binaria, el entrenamiento consiste utilizar conjuntos de entrenamiento y pruebas para ajustar los pesos y el umbral/sesgo, además de utilizr funciones y umbrales para
clasificar.

## ¿En qué difieren?

Las diferencias más notorias están en las funciones, el perceptrón ocupó como función lineal de activación (función escalón), mientras que el modelo de regresión utiliza una combinación de función de regresión lineal con la función sigmoide, la cuál nos ayuda tanto a clasificar como a calcular la probabilidad de las predicciones. Además, el modelo de regresión utiliza una optimización llamada **descenso por el gradiente** para ajustar los pesos y el sesgo.

# Punto extra +1

Para correr el punto extra es necesario activar el entorno virtual:

```bash
myenv/Scripts/activate
```

Se hace uso de las librerias:

    - numpy
    - colorama

Al correr el punto extra se mostrará en terminal un reporte comparando los resultados del perceptrón y el modelo de regresión lineal.


