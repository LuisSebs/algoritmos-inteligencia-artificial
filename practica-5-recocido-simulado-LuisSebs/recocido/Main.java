package recocido;

import java.io.File;
 
/**
 * Clase para ejecutar un proceso de optimización usando recocido simulado.
 * @author Benjamin Torres Saavedra
 * @author Verónica E. Arriola
 * @version 0.1
 */
public class Main{
	/**
	 * Recibe la dirección de un archivo .tsp y utiliza recocido simulado
	 * para encontrar una solución al problema del agente viajero en esa
	 * ciudad.
	 * El programa se podrá ejecutar como:
	 * java recocido.Main <archivo.tsp>
	 * @param args Nombre del archivo tsp.
	 */
	public static void main(String[] args){
		// Ruta del archivo:
		String ruta = args[0];

		// Problema archivo
		File problemaArchivo = new File(ruta);
		DatosPAV problema = new DatosPAV(problemaArchivo);
		Solucion inicial = new SolucionTSP(problema);
		
		int interacciones = 100;
		int temperaturaInicial = 20; // Temperatura inicial no muy grande ni muy pequeña
		float decaimiento = 0.03f; // Decaimiento

		Solucion[] soluciones = new SolucionTSP[interacciones];

		RecocidoSimulado recocido = new RecocidoSimulado(inicial,temperaturaInicial,decaimiento);
		Solucion s = null;		
		for(int i = 0; i < interacciones; i++){
			s = recocido.ejecutar();  
			soluciones[i] = s;
			System.out.println("La mejor solucion encontrada en la iteracion " + i + " es:");
			System.out.println(s);
			System.out.println("Con un valor de: " + s.evaluar());
		}
		System.out.println("------------------------------------------------------------------");
		System.out.println("La mejor solución encontrada fue:");
		System.out.println(s); // Ruta
		System.out.println("Valor sol inicial: "+inicial.evaluar()); // Valor inicial
		System.out.println("Valor sol   final: "+s.evaluar()); // Valor final (mientras mas bajo mejor)
		System.out.println("Nota: A menor valor es mejor, ya que es menor distancia recorrida");
	}
}
