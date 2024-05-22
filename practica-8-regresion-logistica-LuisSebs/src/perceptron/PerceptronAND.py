import numpy as np
from perceptron.Perceptron import Perceptron

class PerceptronAND(Perceptron):

    class ConjuntoEntrenamientoAND:

        def __init__(self,num) -> None:
            self.datos = self.datos(num)
            self.clases = self.clases(num)

        def datos(self, num):
            datos = None

            if (num==1):
                datos = np.array([[0,0,0],
                                [1,1,1]])

            if (num==2):
                datos = np.array([[0,0,0],
                                [0,0,1],
                                [0,1,0],
                                [0,1,1],
                                [1,0,0],
                                [1,0,1],
                                [1,1,0],
                                [1,1,1]])

            if (num == 3):
                datos = np.array([[0,0,0],
                                [0,1,0],
                                [1,0,0],
                                [1,1,0]])

            if (num == 4):
                datos = np.array([[0,0,1],
                                [0,1,1],
                                [1,0,1],
                                [1,1,1]])

            if (num == 5):
                datos = np.array([[0,0,0],
                                [0,0,1],
                                [1,1,0],
                                [1,1,1]])
            
            return datos

        def clases(self, num):
            clases = None
            if (num==1): clases = np.array([0,1])
            if (num==2): clases = np.array([0,0,0,0,0,0,0,1])
            if (num == 3): clases = np.array([0,0,0,0])
            if (num == 4): clases = np.array([0,0,0,1])
            if (num == 5): clases = np.array([0,0,0,1])
            return clases

    def __init__(self, num) -> None:
        super().__init__(num)
        self.conjunto_clases_prueba = [0,0,0,1]
        self.nombre = "Perceptron AND"

    def conjuntoEntrenamiento(self, num):
        return self.ConjuntoEntrenamientoAND(num)

    def menuConjuntos(self):

        """
            Regresa un menu de los conjuntos de entrenamiento
            disponibles para este perceptron.
        """

        string = ""

        for i in range(1,6):
            conjunto = self.ConjuntoEntrenamientoAND(i)
            string += "[{}]: Conjunto {}\n".format(i,i)
            for j in range(len(conjunto.datos)):
                string += "\t {}\n".format(conjunto.datos[j])

        return string
