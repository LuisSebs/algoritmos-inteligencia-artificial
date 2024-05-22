import random
import sys

class Poblacion:

    """
        Simula una poblacion de Individuos
        en un algoritmo genetico para el 
        problema de las n_reinas.
    """
    
    class Individuo:

        """
            Simula un indiviuo de una poblacion
            en un algoritmo genetico para el 
            problema de las n_reinas.
        """

        def __init__(self,cromosoma) -> None:
            self.cromosoma = cromosoma
            self.aptitud = None
        
        # CHECK
        def mutacion(self):

            """
                Muta el cromosoma del indiviuo con una
                probabilidad de 0.2 de ser mutado
            """

            n = len(self.cromosoma)
            probabilidad = 0.2
            # Recorremos el cromosoma del individuo
            for i in range(n):
                # Valor random entre [0,1]
                ran = random.random()
                if  ran < probabilidad:
                    # Mutamos
                    self.cromosoma[i] = random.randint(1,n)
                    break

    def __init__(self,n=0,q=8) -> None:
        self.q = q # Cantidad de reinas
        self.poblacion = [self.Individuo([random.randint(1,q) for j in range(q)]) for i in range(n)]
        self.optimo = None

    # CHECK
    def asignarAptitud(self):

        """
            Asigna a toda la poblacion la
            aptitud de los individuos
        """

        for i in self.poblacion:
            # Aptitud del individuo i
            ap = self.fitness(i.cromosoma)
            # Asignamos
            i.aptitud = ap

    # CHECK
    def fitness(self,arr):

        """
            Funcion auxiliar que determina la aptitud
            del arreglo pasado como parametro. Se basa
            en la cantidad de colisiones entre las reinas

            param: arr : cromosoma del individuo

            return: aptitud : aptitud del cromosoma
        """

        n = self.q
        # Contamos la cantidad de ataques en lineas horizontales
        ataques = sum([arr[i+1:].count(arr[i]) for i in range(n)])
        # Calculamos las colisiones en diagonales
        for i in range(n):
            for j in range(i,n):
                if i != j:
                    dx = abs(i-j)
                    dy = abs(arr[i] - arr[j])
                    if dx == dy:
                        ataques += 1

        # Lo optimo son la suma de los q primeros numeros naturales
        suma_gauss = int(((n-1) * ((n-1) + 1))/2)
        
        return suma_gauss - ataques

    # CHECK
    def elitismo(self):
        """
           Encuentra al Individuo con mejor aptitud. 
           Adicionalmente asigna al mejor Individuo 
           encontrado hasta el momento. (self.optimo)

           return: Individuo con mejor aptitud
        """

        # Mayor aptitud
        mayor = -1
        # Indice del indiviuo
        indice = -1

        for i in range(len(self.poblacion)):
            individuo = self.poblacion[i]
            if individuo.aptitud >= mayor:
                mayor = individuo.aptitud
                indice = i
        
        # Asignamos al Individuo con mayor aptitud
        self.optimo = self.poblacion[indice]
        
        return self.optimo

    # CHECK
    def seleccionRuleta(self):

        """
            Selecciona a un Individuo de la poblacion
            en base a su % de supervivencia. Mientras
            mayor sea más probabilidades tiene de ser
            seleccionado.

            return: Individuo de la poblacion
        """
        
        sumatoria = 0

        # Sumatoria de todas las aptitudes de la poblacion
        for i in self.poblacion:
            sumatoria += i.aptitud
        
        # Individuo seleccionado
        individuo = None

        # Longitud de la poblacion
        n = len(self.poblacion)

        # Mientras no seleccionemos a un individuo
        while individuo == None:
            indice = random.randint(0,n-1)
            # Individuo aleatorio
            individuo_ran = self.poblacion[indice]
            # random in [0,1] | lo dividimos entre n para ajustar la probabilidad (si no nunca se eligira un individuo)
            ran = random.random()/n
            # Porcentaje de supervivencia (individuo_ran.aptitud/sumatoria)
            if ran < (individuo_ran.aptitud/sumatoria):
                individuo = self.poblacion[indice]

        return individuo

    # CHECK
    def optimoEncontrado(self):

        """
            Determina si se ha encontrado al Individuo optimo. 
            La aptitud optima para el problema de las n_reinas
            es la suma de gauss

            return: True si se encontro al optimo, False en caso contrario
        """
        n = self.q
        suma_gauss = int(((n-1) * ((n-1) + 1))/2)
        return False if self.optimo == None else self.optimo.aptitud == suma_gauss
            
# CHECK
def recombinacion(p1,p2):

    """
        Regresa un Individuo hijo resultado de la mezcla de los
        cromosomas de ambos padres.

        return: Individuo
    """

    n = len(p1.cromosoma)
    corte = random.randint(0,n-2)
    hijo = Poblacion(0,0).Individuo(p1.cromosoma[0:corte+1]+p2.cromosoma[corte+1:n])
    return hijo

if __name__ == "__main__":

    n = int(sys.argv[1])

    iteraciones_base = 1000

    # SIMULACION BASADA EN EL PSEUDOCODIGO DEL PDF
    generaciones = 0

    poblacion = Poblacion(50,n)
    poblacion.asignarAptitud()
    while generaciones < int((n*iteraciones_base)/8) and (not poblacion.optimoEncontrado()):
        nuevaPoblacion = list()
        nuevaPoblacion.append(poblacion.elitismo()) 
        while len(nuevaPoblacion) < 50:
            individuo1 = poblacion.seleccionRuleta()
            individuo2 = poblacion.seleccionRuleta()
            hijo = recombinacion(individuo1,individuo2)
            hijo.mutacion()
            nuevaPoblacion.append(hijo)
        poblacion.poblacion = nuevaPoblacion
        poblacion.asignarAptitud()
        generaciones += 1
        # Cada 50 generaciones mostramos la mejor solucion
        if generaciones%50 == 0:
            print(f"Mejor solucion en iteracion {generaciones} es: {poblacion.optimo.cromosoma} | fitness: {poblacion.optimo.aptitud}")

    # En caso en el que hayamos encontrado al optimo
    if poblacion.optimoEncontrado():
        print(f"Se encontro el optimo en la generacion {generaciones}")
        print(f"{poblacion.optimo.cromosoma} | fitness: {poblacion.optimo.aptitud}")
