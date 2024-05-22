import numpy as np
import colorama
from LogisticRegression import LogisticRegression
from LogisticRegression import conjunto_entrenamiento_clases
from colorama import Fore
from perceptron.PerceptronAND import PerceptronAND

colorama.init(autoreset=True)    
    
print("""
La finalidad de este reporte es conseguir el punto extra y comparar 
dos modelos de aprendizaje de máquina, un perceptrón y un modelo de
regresión lineal. En esta ocasión para resolver una compuerta AND.
""")


# Creamos dos modelos
print(f"Primero creamos dos modelos a los que llamaremos " + Fore.BLUE + "perceptron " + Fore.WHITE + "y " + Fore.GREEN + "regresion")

# Perceptron
perceptron = PerceptronAND(2)

# Modelo de regresion
regresion = LogisticRegression()

print("""
Veamos que resultados no arrojan antes de entrenar ambos modelos con
la tabla de verdad del AND
      
  A      B      A AND B
-----  -----  -----------
  0      0         0
  0      1         0
  1      0         0
  1      1         1
      
""")

# Conjunto de prueba Perceptron
print("Conjunto de prueba perceptron: "+ Fore.LIGHTYELLOW_EX + f"\n{perceptron.conjunto_prueba}\n")
# Conjunto de prueba Regresion
prueba_regresion = np.array([[0,0],[0,1],[1,0],[1,1]])
clases_regresion = np.array([0,0,0,1])
print("Conjunto de prueba regresion: "+ Fore.LIGHTYELLOW_EX + f"\n{prueba_regresion}")

print("""
Notemos que el la longitud de los elementos es distinta, en la practica
pasada se realizo para tres entradas y para la regresion dos entradas.
""")

# Ejecutamos con el conjunto de prueba perceptron
perceptron.prueba()
# Mostramos resultados
print(Fore.CYAN + "Resultados perceptron sin entrenar: \n")
for i in range(len(perceptron.conjunto_prueba)):
    print("{} -> {}".format(perceptron.conjunto_prueba[i], perceptron.resultados_prueba[i]), end=" ")
    if (perceptron.resultados_prueba[i] == perceptron.conjunto_clases_prueba[i]):
        print(Fore.LIGHTGREEN_EX+"CHECK")
    else:
        print(Fore.RED+"FAIL")
print("")
# Ejecutamos con el conjunto de prueba regresion
resultados_regresion_prueba = regresion.predict(prueba_regresion)
# Mostramos resultados
print(Fore.CYAN + "Resultados regresion sin entrenar: \n")
for i in range(len(resultados_regresion_prueba)):
    print("{} -> {}".format(prueba_regresion[i], resultados_regresion_prueba[i]), end=" ")
    if (resultados_regresion_prueba[i] == clases_regresion[i]):
        print(Fore.LIGHTGREEN_EX+"CHECK")
    else:
        print(Fore.RED+"FAIL")
print("")

print("""
Los conjuntos de entrenamiento de ambos modelos son distintos
en cuanto a longitud. Para el perceptron tomaremos su conjunto
mas grande, que consiste en todas las posibles combinaciones
de estados para tres entradas en la tabla de verdad. Mientras
que para la regresion utilizaremos el conjunto solicitado en 
el entrenamiento, el cual consiste en 200 muestras, 150 para
la clase cero y 50 muestras para la clase uno, agregando ruido
gaussiano para que sean datos variados. Como este conjunto de
entrenamiento es muy grande, solo mostraremos las primeras
10 entradas.
""")

print("Conjunto de entrenamiento perceptron: \n" + Fore.LIGHTYELLOW_EX + f"{perceptron.conjunto.datos}\n")
c, clases = conjunto_entrenamiento_clases()
conjunto_regresion = list()
i = 0
for x in c:
    if i == 10:
        break
    else:
        elem = list(x)
        elem[0] = round(elem[0],2)
        elem[1] = round(elem[1],2)
        conjunto_regresion.append(elem)
        i+=1
print("Conjunto de entrenamiento regresion: \n" + Fore.LIGHTYELLOW_EX + f"{conjunto_regresion}\n")

print(Fore.BLUE+"Parametros perceptron no entrenado: \n")
print(f"Pesos: " + Fore.LIGHTYELLOW_EX+f"{perceptron.pesos}")
print(f"Umbral: " + Fore.GREEN+f"{perceptron.b}")
print(f"Tasa de aprendizaje: " + Fore.LIGHTMAGENTA_EX+f"{perceptron.tasa_de_aprendizaje}")
print(f"Iteraciones: " + Fore.LIGHTCYAN_EX+f"{perceptron.iteraciones}\n")

print(Fore.BLUE+"Parametros regresion no entrenado: \n")
print(f"Pesos: " + Fore.LIGHTYELLOW_EX+f"{regresion.w}")
print(f"Umbral: "  + Fore.GREEN+f"{regresion.b}")
print(f"Tasa de aprendizaje: " + Fore.LIGHTMAGENTA_EX+f"{0.01}")
print(f"Iteraciones: " + Fore.LIGHTCYAN_EX+f"{100}")

print("""
Como podemos notar son conjuntos de entrenamiento muy diferentes, tanto
en el tamaño del conjunto, como en el tipo de dato, como en la longitud 
de cada entrada. Ahora vamos a entrenar los modelos con sus respectivos 
conjunto de entrenamiento.
""")

print(Fore.LIGHTCYAN_EX+"Entrenando perceptron . . .\n")
perceptron.entrenamiento()
perceptron.prueba()
print(Fore.LIGHTCYAN_EX+"Entrenando regresion . . .")
regresion.fit(c,clases)

print("""
Una vez entrenados ambos modelos podemos comenzar a revisar los 
resultados para los conjuntos de  prueba, así como  tambien los
respectivos parámetros de cada modelo despues el entrenamiento.
""")

print(Fore.BLUE+"Parametros perceptron si entrenado: \n")
print(f"Pesos: " + Fore.LIGHTYELLOW_EX+f"{perceptron.pesos}")
print(f"Umbral: " + Fore.GREEN+f"{perceptron.b}")
print(f"Tasa de aprendizaje: " + Fore.LIGHTMAGENTA_EX+f"{perceptron.tasa_de_aprendizaje}")
print(f"Iteraciones: " + Fore.LIGHTCYAN_EX+f"{perceptron.iteraciones}\n")

print(Fore.BLUE+"Parametros regresion si entrenado: \n")
print(f"Pesos: " + Fore.LIGHTYELLOW_EX+f"{regresion.w}")
print(f"Umbral: "  + Fore.GREEN+f"{regresion.b}")
print(f"Tasa de aprendizaje: " + Fore.LIGHTMAGENTA_EX+f"{0.01}")
print(f"Iteraciones: " + Fore.LIGHTCYAN_EX+f"{100}\n")

# Mostramos resultados
print(Fore.CYAN + "Resultados perceptron entrenado: \n")
for i in range(len(perceptron.conjunto_prueba)):
    print("{} -> {}".format(perceptron.conjunto_prueba[i], perceptron.resultados_prueba[i]), end=" ")
    if (perceptron.resultados_prueba[i] == perceptron.conjunto_clases_prueba[i]):
        print(Fore.LIGHTGREEN_EX+"CHECK")
    else:
        print(Fore.RED+"FAIL")
print("")
# Aciertos
asserts = 0
for i in range(len(perceptron.resultados_prueba)):
    if perceptron.resultados_prueba[i] == perceptron.conjunto_clases_prueba[i]:
        asserts += 1
print("\nEntradas evaluadas correctamente: {}".format(asserts))
if asserts == len(perceptron.resultados_prueba):
    print(Fore.LIGHTGREEN_EX +"El perceptron SI logro aprender la funcion")
else:
    print(Fore.YELLOW+"El perceptron NO logro aprender la funcion")


# Mostramos resultados
print(Fore.CYAN + "\nResultados regresion entrenado: \n")
resultados_regresion_prueba = regresion.predict(prueba_regresion)
for i in range(len(resultados_regresion_prueba)):
    print("{} -> {}".format(prueba_regresion[i], resultados_regresion_prueba[i]), end=" ")
    if (resultados_regresion_prueba[i] == clases_regresion[i]):
        print(Fore.LIGHTGREEN_EX+"CHECK")
    else:
        print(Fore.RED+"FAIL")
print("")
# Aciertos
asserts = 0
for i in range(len(resultados_regresion_prueba)):
    if resultados_regresion_prueba[i] == clases_regresion[i]:
        asserts += 1
print("\nEntradas evaluadas correctamente: {}".format(asserts))
if asserts == len(resultados_regresion_prueba):
    print(Fore.LIGHTGREEN_EX +"El perceptron SI logro aprender la funcion")
else:
    print(Fore.YELLOW+"El perceptron NO logro aprender la funcion")    







    
