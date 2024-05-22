import numpy as np
from PerceptronOR import PerceptronOR
from PerceptronAND import PerceptronAND
import colorama
from colorama import Fore

colorama.init(autoreset=True)

def reporte(perceptron, i):
    print(Fore.LIGHTBLUE_EX+f"\n\t{perceptron.nombre}\n")
    print(Fore.LIGHTGREEN_EX + f"Conjunto de entrenamiento {i}: \n")
    conjunto_entrenamiento = np.concatenate((perceptron.conjunto.datos, perceptron.conjunto.clases[:, np.newaxis]), axis=1)
    for renglon in conjunto_entrenamiento:
        print(renglon)
    print("\nPesos iniciales: {}".format(perceptron.pesos))
    print("Umbral inicial: {}".format(perceptron.b))
    # Entrenamiento
    print(Fore.CYAN + "\n... Entrenamiento ...\n")
    perceptron.entrenamiento()
    print("Pesos finales: {}".format(perceptron.pesos))
    print("Umbral final: {}".format(perceptron.b))
    print("\nProgreso del error: \n")
    j = 0
    print("[")
    for e in perceptron.progreso:
        if j < 9:
            print(e, end=" ")
            j += 1
        else:
            print(e, end="\n")
            j = 0
    print("]")
    print("\nConjunto de prueba: \n")
    for p in perceptron.conjunto_prueba:
        print(p)
    print(Fore.BLUE + "\n... Prueba ...\n")
    perceptron.prueba() 
    print(Fore.CYAN + "Resultados: \n")
    for i in range(len(perceptron.conjunto_prueba)):
        print("{} -> {}".format(perceptron.conjunto_prueba[i], perceptron.resultados_prueba[i]), end=" ")
        if (perceptron.resultados_prueba[i] == perceptron.conjunto_clases_prueba[i]):
            print(Fore.LIGHTGREEN_EX+"CHECK")
        else:
            print(Fore.RED+"FAIL")

    asserts = 0
    for i in range(len(perceptron.resultados_prueba)):
        if perceptron.resultados_prueba[i] == perceptron.conjunto_clases_prueba[i]:
            asserts += 1
    print("\nEntradas evaluadas correctamente: {}".format(asserts))

    if asserts == len(perceptron.resultados_prueba):
        print(Fore.LIGHTGREEN_EX +"El perceptron SI logro aprender la funcion")
    else:
        print(Fore.YELLOW+"El perceptron NO logro aprender la funcion")


    print(Fore.LIGHTGREEN_EX + "---\n")

def getOpcionConjunto(perceptron):

    menu_conjunto = None

    if perceptron == 'AND':
        menu_conjunto = PerceptronAND(1).menuConjuntos()
    if perceptron == 'OR':
        menu_conjunto = PerceptronOR(1).menuConjuntos()
    
    while True:
        print(menu_conjunto)
        op = input("\nElige un conjunto de entrenamiento: ")
        if op == '1':
            return 1
        if op == '2':
            return 2
        if op == '3':
            return 3
        if op == '4':
            return 4
        if op == '5':
            return 5
        else:
            print("\nElige una opcion valida\n")
        
if __name__ == "__main__":

    menu_perceptron = "\n[1]: PerceptronAND\n[2]: PerceptronOR\n"

    while True:
        print(menu_perceptron)
        op = input("\nElige un perceptron: ")
        print()
        if op == '1':
            menu_and = PerceptronAND(1).menuConjuntos()
            conjunto = getOpcionConjunto('AND') 
            perceptron = PerceptronAND(conjunto)
            reporte(perceptron, conjunto)
        elif op == '2':
            menu_or = PerceptronOR(1).menuConjuntos()
            conjunto = getOpcionConjunto('OR')     
            perceptron = PerceptronOR(conjunto)
            reporte(perceptron, conjunto)
        else:
            print("\nIngresa una opcion valida\n")
