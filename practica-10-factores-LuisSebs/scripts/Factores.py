from itertools import product

class Variable:

    """
        Variable Aleatoria
    """

    def __init__(self, nombre, valores_posibles) -> None:
        self.nombre = nombre
        self.valores_posibles = valores_posibles

    def __str__(self) -> str:
        return "Nombre: {} | Valores: {}".format(self.nombre, self.valores_posibles)

class Factor:

    """
        Factor
    """

    def __init__(self, alcance, valores) -> None:
        self.alcance = alcance
        self.valores = valores
        self.tabla = None
    
    def _generar_tabla_de_valores(self):

        """
            Genera la la tabla de valores del factor
        """

        # Variables aleatorias del factor
        variables = [var.valores_posibles for var in self.alcance]
        # Permutaciones
        combinaciones = list(product(*variables))

        # Resultado
        tabla_valores = []
        
        # Iteramos sobre las combinaciones y agregamos las filas
        for x in combinaciones:
            fila = dict(zip([var.nombre for var in self.alcance], x))
            fila['Prob'] = self.valores[combinaciones.index(x)] # Agrega el atributo valores del factor
            tabla_valores.append(fila)
        
        # Establecemos la tabla del factor
        self.tabla = tabla_valores

    def index(self,dir):

        """
            Metodo auxiliar que recibe como parametro
            un diccionario, cuyas llabes sean variables 
            y los valores sean el valor asignado a cada
            una.

            param: diccionario
            return: el indice del diccionario pasado
            como parametro en la tabla factor.
        """

        # Lista de los valores a buscar
        valores = []
        for i in range(len(self.alcance)):
            key = self.alcance[i]
            valor = dir[key]
            valores.append(valor)

        # Uso del polinomio de direccionamiento
        return self.pol(0,valores)

    def pol(self, i, valores):

        """
            Implementacion recursiva del polinomio
            de direccionamiento. Regresa el indice
            de un conjunto de valores a buscar en 
            la tabla.

            param: i : indice de la variable aleatoria actual
            param: valores: lista de valores a buscar
            return: indice
        """

        if len(valores) == 1:
            return self.pos(valores[0],i)

        # Multiplicacion de longitudes
        mult = 1
        for v in self.alcance[i+1::]:
            mult *= len(v.valores_posibles)

        # Posicion del valor en la variable aleatoria
        pos = self.pos(valores[0],i)
        valores.pop(0)

        # Llamada recursiva
        return ( pos * mult) + self.pol(i+1,valores)

    def pos(self, valor, i):
        
        """
            Regresa el indice de un valor
            en los posibles valores de la
            variable.

            param: posible valor de la variable
            param: indice de la variable aleatoria 
            en el alcance del factor.
            return: indice
        """

        variable = self.alcance[i]
        indice = variable.valores_posibles.index(valor)
        return indice

    def multiply(self,factor):

        """
            Multiplicacion

            param: factor a multiplicar
            return: un nuevo factor resultado
            de la multiplicacion por el factor
            pasado como parametro.
        """

        # Encontrar variables comunes en ambos factores
        variables_comunes = set(self.alcance).intersection(factor.alcance)
        
        # Combinar alcance y valores de ambos factores
        nuevo_alcance = list(self.alcance) + [var for var in factor.alcance if var not in variables_comunes]
        nuevo_valores = []

        # Permutaciones sobre los posibles valores de las variables
        for combo in product(*[var.valores_posibles for var in nuevo_alcance]):
            fila_factor1 = {var: valor for var, valor in zip(nuevo_alcance, combo)}
            fila_factor2 = {var: valor for var, valor in zip(nuevo_alcance, combo)}
            nuevo_valores.append(self.valores[self.index(fila_factor1)] * factor.valores[factor.index(fila_factor2)])
        
        return Factor(nuevo_alcance, nuevo_valores)
    
    def reduce(self, variable, valor):

        """
            Reduccion

            param: variable: variable a reducir
            param: valor: valor a reducir
            return: nuevo factor resultado
            de la reduccion.
        """

        # Extraemos las variables existentes al aplicar la reduccion
        nuevas_variables = [var for var in self.alcance if var != variable]
        
        if not nuevas_variables:
            # Si no hay variables nuevas despues de la reduccion, devolver una copia del factor original
            return Factor(self.alcance, self.valores.copy())
        
        nuevo_alcance = tuple(nuevas_variables)
        nuevo_valores = []

        # Permutaciones sobre los posibles valores de las variables
        for combo in product(*[var.valores_posibles for var in nuevo_alcance]):
            fila_factor = {var: valor for var, valor in zip(nuevo_alcance, combo)}
            fila_completa = {**fila_factor, variable: valor}
            nuevo_valores.append(self.valores[self.index(fila_completa)])
        
        return Factor(nuevo_alcance, nuevo_valores)

    def normalize(self):

        """
            Normalizacion

            return: nuevo factor
            resultado de la 
            normalizacion
        """
        
        # Sumamos los valores
        suma_valores = sum(self.valores)
        if suma_valores != 0:
            # A cada valor lo dividimos por la suma de todos los valores
            valores_normalizados = [valor / suma_valores for valor in self.valores]
            return Factor(self.alcance, valores_normalizados)
        else:
            # Si la suma es 0 regresamos una copia del factor actual
            return Factor(self.alcance, self.valores.copy())
    
    def marginalize(self, variable):

        """
            Marginalizacion

            param: variable: La variable que se eliminara al marginalizar.
            return: nuevo factor resultado de la marginalización.
        """

        nuevas_variables = [var for var in self.alcance if var != variable]
        if not nuevas_variables:
            # Si no hay variables nuevas despues de la marginalizacion, devolver una copia del factor original
            return Factor(self.alcance, self.valores.copy())
        
        nuevo_alcance = tuple(nuevas_variables)
        nuevo_valores = []

        # Permutaciones de los valores de las variables en el nuevo alcance
        for combo in product(*[var.valores_posibles for var in nuevo_alcance]):
            fila_factor = {var: valor for var, valor in zip(nuevo_alcance, combo)}
            fila_completa = {**fila_factor, variable: None}
            
            # Sumar sobre la variable que se está marginalizando
            suma_valores = sum(self.valores[self.index({**fila_completa, variable: v})] for v in variable.valores_posibles)
            nuevo_valores.append(suma_valores)
        
        return Factor(nuevo_alcance, nuevo_valores)

    def __str__(self) -> str:
        
        self._generar_tabla_de_valores()
        
        resultado = ' '.join([v.nombre for v in self.alcance]) + ' | ' + 'Prob\n'
        for fila in self.tabla:
            valores = [str(fila[n]) for n in [v.nombre for v in self.alcance]]
            resultado += ' '.join(valores) + ' | ' + str(fila['Prob']) + '\n'

        return resultado

