import numpy as np

class LogisticRegression:

    """
        Modelo de regresión logística
    """

    def __init__(self) -> None:
        # W
        self.w =  np.random.uniform(-0.5,0.5, size=2)
        # Theta
        self.b = np.random.uniform(-0.5,0.5)

    def fit(self,X,Y, tasa = 0.1, iteraciones = 100):

        """
            Realiza el entrenamiento supervisado
            dado un conjunto de entrenamiento X
            y sus clases Y con el descenso
            por el gradiente.

            :param: X vector
            :param: Y vector
        """

        # Descenso por el gradiente
        n = len(X)
        for i in range(iteraciones):
            for j in range(n):                
                x = X[j]
                y = Y[j]
                self.w = self.w - tasa * self.delta_j_w(x,y)
                self.b = self.b - tasa * self.delta_j_b(x,y)

    def predict_proba(self, X):
        """
            Regresa las probabilidades
            de cada elemento en el conjunto
            X de pertenecer o no una clase.

            :param: X vector
            :return: probabilidades de X
        """
        return [self.sigmoide(x) for x in X]
    
    def predict(self, X):
        """
            Clasifica un conjunto y
            regresa sus predicciones.

            :param: X vector
            :return: clasificacion de X
        """
        return [1 if x > 0.5 else 0  for x in self.predict_proba(X)]

    def sigmoide(self,x):
        """
            Regresa la función logística
            o sigmoide de x.

            :return: sigmoide de x
        """
        return 1/(1+np.exp(-((np.dot(self.w,x) + self.b))))
    
    def delta_j_w(self,x,y):
        """
            Regresa la delta w

            :param: x
            :param: y
            :return: delta w
        """
        sigmoide = self.sigmoide(x)
        perdida_parcial = (sigmoide-y)*x
        return(perdida_parcial)

    def delta_j_b(self,x,y):
        """
            Regresa la delta b

            :param: x
            :param: y
            :return: delta b
        """
        sigmoide = self.sigmoide(x)
        perdida_parcial = (sigmoide-y)
        return(perdida_parcial)

def get_datos_cero(n):

    """
        Regresa un conjunto de
        entrenamiento compuesto con puros
        elementos de la clase cero,
        e.g. [0,0],[0,1],[1,0]

        :param: n cantidad de elementos
        :return: conjunto de entrenamiento de la clase cero.
    """

    resultado = []
    i = 0
    while i < n:
        arr = np.random.randint(2, size=2)
        if arr[0] == arr[1] and arr[0] == 1 and arr[1] == 1:
            pass
        else:
            resultado.append(arr)
            i+=1
    return np.array(resultado)
    
def conjunto_entrenamiento_clases():
        
        """
            Regresa el conjunto de entrenamiento
            solicitado en el pdf de la práctica
            con su respectiva lista de clases.

            : return entrenamiento

            : return clases
        """

        # 150 ejemplos clase 0
        num_datos_cero = 150
        datos_cero = get_datos_cero(num_datos_cero)
        clases_cero = np.array([0] * num_datos_cero)

        # 50 ejemplos clase 1
        num_datos_uno = 50
        datos_uno = np.ones((num_datos_uno,2), dtype=int)
        clases_uno = np.array([1] * num_datos_uno)

        # Conjunto entrenamiento
        conjunto_entrenamiento = np.vstack((datos_cero,datos_uno))

        # Conjunto de clases
        conjunto_clases = np.concatenate((clases_cero, clases_uno), axis=0)

        # Ruido
        num_ruido = len(conjunto_entrenamiento)
        ruido = np.random.normal(loc=0, scale=1, size=(num_ruido,2))
        factor_escala = np.random.uniform(0.1, 0.2)
        ruido_escalado = ruido * factor_escala

        # Conjunto de entrenamiento con ruido
        conjunto_entrenamiento_ruido = conjunto_entrenamiento + ruido_escalado

        return conjunto_entrenamiento_ruido, conjunto_clases

if __name__ == '__main__':

    # Modelo de regresion
    modelo = LogisticRegression()

    # Conjunto de entrenamiento solicitado en el pdf
    X, Y = conjunto_entrenamiento_clases()
    
    # Entrenamiento del modelo
    modelo.fit(X,Y)

    # Conjunto de prueba
    prueba = np.array([[0,0],[0,1],[1,0],[1,1]])

    # Resultados conjunto prueba
    resultados = modelo.predict(prueba)

    for i in range(4):
        print("{} -> {}".format(prueba[i], resultados[i]))

    