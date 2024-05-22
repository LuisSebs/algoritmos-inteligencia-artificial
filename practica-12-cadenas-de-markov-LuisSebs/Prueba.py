from CadenaMarkov import CadenaDeMarkov
import numpy as np

if __name__ == "__main__":

    # Ejemplo: El soldado

    print(
    """
    Sumpongamos que estamos modelando el comportamiento de un soldado en un videojuego 
    de acción. Este soldado está vigilando un área restringida y puede tener alguno de 
    tres comportamientos: estar caminando, quedarse de pie o dormido. El estado del
    soldado queda descrito por la variable S \in {caminando, dormido, de pie}, lo cual
    en ocasiones abreviaremos como S \in {cam,dor,d.p.} Para que su comportamiento no sea
    tan predecible, cambiará su actividad aleatoriamente según describe el autómata.
    """)

    estados_soldado = ["cam", "dor", "d.p."]
    print("Estados del soldado: {}".format(estados_soldado))

    print(
    """
    Entonces la matriz de transición se acomoda como en la tabla siguiente:
    """)

    matriz = np.array([[0.27, 0.03, 0.7], [0.3, 0.2, 0.5], [0.6, 0.2, 0.2]])
    print("Matriz de transicion: \n {}".format(matriz))

    print(
    """
    Inicialmente sea:
    """)

    s_0 = np.array([0.2, 0.2, 0.6])
    print("Probabilidad estados iniciales: \n {}".format(np.column_stack([estados_soldado, s_0.reshape(-1, 1)])))

    print(
    """
    Calculamos la distribución de probabilidad usando la Cadena de Markov
    """)
    
    cm = CadenaDeMarkov(estados_soldado, s_0, matriz)
    secuencia = cm.generaSecuenciaEstados(10)
    print("Secuencia de estados: {}".format(secuencia))
    probabilidad = proba_s1 = cm.calcular_probabilidad(secuencia)
    print("Probabilidad de la secuencia: {}".format(probabilidad))
    distribucion = distribucion_limite = cm.estimar_distribucion_largo_plazo()
    print(
    """
    Comportamiento del soldado en el estado estacionario:
    
    P(S) =
    {}
    """
    .format(distribucion)
    )
