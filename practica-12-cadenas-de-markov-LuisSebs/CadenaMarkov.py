import numpy as np
import random

class CadenaDeMarkov:

    """
        Cadena de Markov
    """

    def __init__(self, estados, probabilidades_iniciales, probabilidades_transiciones):
        """
            Constructor Cadena de Markov:

            Params: 
                - estados: estados posibles
                - probabilidades_iniciales: probabilidades de iniciar en cada uno de los estados posibles
                - probabilidades_transiciones: probabilidades de transicionar de cada estado a los demás
        """
        self.estados = estados
        self.iniciales = probabilidades_iniciales
        self.transiciones = probabilidades_transiciones
    
    def generaSecuenciaEstados(self, n, semilla=None):

        """
            Genera una secuencia de estados a partir del modelo de Markov iniciado dado el número n
            de elementos que tendrá la secuencia.

            params:
                - n: cantidad de elementos de la secuencia a generar
                - semilla: numero aleatorio para determinar cual de los estados
                           correspondera a ese paso.

            return: secuencia de estados
        """

        if semilla:
            random.seed(semilla)
        
        secuencia = list()
        estado_actual = self.obtener_estado_inicial() # Obtenemos el estado inicial
        secuencia.append(estado_actual)

        for _ in range(1,n):
            # Obtenemos el siguiente estado a transicionar
            estado_actual = self.transicionar(estado_actual)
            # Lo agregamos a la secuencia
            secuencia.append(estado_actual)
        
        return secuencia
    
    def obtener_estado_inicial(self):
        """
            Regresa un estado aleatorio dada su probabilidad de iniciar
            en ese estado.

            return estado inicial
        """
        return random.choices(self.estados, weights=self.iniciales)[0]
    
    def transicionar(self, estado_actual):
        """
            A partir de un estado regresa el siguiente
            estado a transicionar dada su probabilidad de transicion

            params:
                - estado_actual: estado actual

            return: nuevo estado
        """
        indice_estado_inicial = self.estados.index(estado_actual)
        probabilidades_transicion = self.transiciones[indice_estado_inicial]
        nuevo_estado = random.choices(self.estados, weights=probabilidades_transicion)[0]
        return nuevo_estado
    
    def calcular_probabilidad (self, secuencia):
        """
            Regresa la probabilidad de una cadena de estados

            params:
                - secuencia: secuencia de estados
            
            return: probabilidad de que se cumpla esa secuencia de estados
        """
        probabilidad = self.iniciales[self.estados.index(secuencia[0])]

        # Probabilidad de distribucion conjunta P(s_0,s_1,...,s_n)
        for i in range(1, len(secuencia)):
            estado_anterior = secuencia[i-1]
            estado_actual = secuencia[i]
            probabilidad *= self.transiciones[self.estados.index(estado_anterior), self.estados.index(estado_actual)]

        return probabilidad
    
    def estimar_distribucion_largo_plazo(self, iteraciones=1000):

        """
            Calcula la distribucion limite, cuando sea posible

            param: cantidad de iteraciones
            return: la distribución a largo plazo como una lista
        """

        # Inicializar un vector de probabilidades uniformes como punto de partida
        distribucion_actual = np.ones(len(self.estados)) / len(self.estados)

        # Iterar para estimar la distribución a largo plazo
        for _ in range(iteraciones):
            # Multiplicar la distribución actual por la transpuesta de la matriz de transiciones
            distribucion_actual = np.dot(distribucion_actual, self.transiciones)

        return distribucion_actual.tolist()
    