import numpy as np
from abc import ABC, abstractmethod

class Perceptron(ABC):

    def __init__(self) -> None:
        super().__init__()

    def __init__(self,num) -> None:
        super().__init__()
        self.progreso = list()
        self.conjunto = self.conjuntoEntrenamiento(num)
        self.conjunto_prueba = [[0,0,0],[1,0,1],[0,0,1],[1,1,1]]
        self.conjunto_clases_prueba = list()
        self.resultados_prueba = list()
        self.pesos = np.random.uniform(-0.5,0.5,size=3)
        self.b = np.random.uniform(-0.5,0.5)
        self.tasa_de_aprendizaje = 0.01
        self.iteraciones = 50 
        self.nombre = ""

    def entrenamiento(self):

        """
            Entrena el perceptron
        """

        for iteracion in range(self.iteraciones):
            error_progreso = 0
            for i in range(len(self.conjunto.datos)):
                resultado = self.activacion(self.pesos, self.conjunto.datos[i],self.b)
                error = self.conjunto.clases[i] - resultado
                error_progreso += error**2
                # Ajustar pesos
                self.pesos[0] += self.tasa_de_aprendizaje * self.conjunto.datos[i][0] * error
                self.pesos[1] += self.tasa_de_aprendizaje * self.conjunto.datos[i][1] * error
                self.pesos[2] += self.tasa_de_aprendizaje * self.conjunto.datos[i][2] * error
                # Ajustar umbral
                self.b += self.tasa_de_aprendizaje * error
            self.progreso.append(error_progreso)

    def prueba(self):

        """
            Ejecuta la funcion de activacion 
            con el conjunto de prueba
            del perceptron. Guarda los resultados
            en resultados_prueba.
        """

        for x in self.conjunto_prueba:
            self.resultados_prueba.append(self.activacion(self.pesos,x,self.b))

    def activacion(self,pesos, x, b):

        """
            Funcion de activacion

            pesos:  pesos
            x:      entradas
            b:      umbral
        """

        z = pesos * x
        if z.sum() + b > 0:
            return 1
        else:
            return 0
        
    @abstractmethod
    def conjuntoEntrenamiento(self,num):
        pass