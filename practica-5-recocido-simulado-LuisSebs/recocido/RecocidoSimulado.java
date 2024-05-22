package recocido;

/**
 * Clase con los métodos necesarios para implementar el algoritmo
 * de recocido simulado junto con la solución a un problema particular.
 * 
 * @author Benjamin Torres
 * @author Verónica E. Arriola
 * @version 0.1
 */
public class RecocidoSimulado{

	/** Parámetros del recocido. */
	private float temperatura;
	private float decaimiento;

	/** Solución actual. */
	private Solucion sol;

	/**
	 * Inicializa los valores necesarios para realizar el
	 * recocido simulado durante un número determinado de iteraciones.
	 * @param inicial Instancia de la clase para el problema particular que
	 * 	  se quiere resolver.  Contine la propuesta de solución inicial.
	 * @param temperatura <code>float</code> con el valor actual .
	 * @param decaimiento <code>float</code> que será usado para hacer decaer el valor de temperatura.
	 */
	public RecocidoSimulado(Solucion inicial,
		          float temperaturaInicial,
		          float decaimiento){ //escoge los parametros necesarios para inicializar el algoritmo
		sol = inicial;
		temperatura = temperaturaInicial;
		this.decaimiento = decaimiento;
	}

	/**
	 * Función que calcula una nueva temperatura en base a
	 * la anterior y el decaemiento usado.
	 * @return nueva temperatura
	 */
	public float nuevaTemperatura(){
		return this.temperatura * (1 - this.decaimiento);
	}

	/**
	 * Genera y devuelve la solución siguiente a partir de la solución
	 * actual. Dependiendo de su valor,
	 * si es mejor o peor que la que ya se tenía,
	 * y de la probabilidad actual de elegir una solución peor, puede devolver
	 * una solución nueva o quedarse con la que ya se tenía.
	 * @return Solución nueva
	 */
	public Solucion seleccionarSiguienteSolucion(Solucion sig){

		double valorSig = sig.evaluar();
		double valorAct = this.sol.evaluar();

		double probabilidad = Math.exp(-((valorSig - valorAct)/this.temperatura));

		if (Math.random() < probabilidad){
			return sig;
		}else{
			return this.sol;
		}
	}

	/**
	 * Ejecuta el algoritmo con los parámetros con los que fue inicializado y
	 * devuelve una solución.
	 * @param
	 * @return Solución al problema
	 */
	public Solucion ejecutar(){
		// Implementacion del pseudocódigo
		if (this.temperatura < 1){
			return this.sol;
		}
		Solucion siguiente = this.sol.siguienteSolucion();
		double deltaE = siguiente.evaluar() - this.sol.evaluar();
		if (deltaE < 0){
			this.sol = siguiente;
		}else{
			this.sol = this.seleccionarSiguienteSolucion(siguiente);
		}
		this.temperatura = this.nuevaTemperatura();
		return sol;
	}
}
