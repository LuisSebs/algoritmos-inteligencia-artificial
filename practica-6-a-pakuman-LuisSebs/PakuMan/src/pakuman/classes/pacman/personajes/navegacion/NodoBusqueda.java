/*
 * Código utilizado para el curso de Inteligencia Artificial.
 * Se permite consultarlo para fines didácticos en forma personal,
 * pero no esta permitido transferirlo resuelto a estudiantes actuales o potenciales.
 */
package pacman.personajes.navegacion;

import java.util.logging.Level;
import java.util.logging.Logger;

import java.util.LinkedList;
import pacman.personajes.Movimiento;

/**
 * Clase que modela a los nodos de nuestra gráfica de búsqueda.
 * @author blackzafiro
 * @author baruch
 */
public class NodoBusqueda implements Comparable<NodoBusqueda> {
	
	private final static Logger LOGGER = Logger.getLogger("pacman.personajes.navegacion.NodoBusqueda");
	static { LOGGER.setLevel(Level.OFF); }
	
	private NodoBusqueda padre;     // Nodo que generó este nodo.
    private Movimiento accionPadre; // Acción que llevo al agente a este estado.
    private Estado estado;          // Referencia del estado al que se llego.
    private int gn;                 // costo de llegar a este nodo.
    
	/**
	 * Nodo que considera al estado indicado.
	 * @param estado 
	 */
    public NodoBusqueda(Estado estado){
        this.estado = estado;
    }
	
	/**
	 * Devuelve el estado en este nodo.
	 */
	public Estado estado() {
		return estado;
	}
	
	/**
	 * Devuelve la acción que permite llegar a este nodo.
	 * @return 
	 */
	public Movimiento accionPadre() {
		return accionPadre;
	}
	
	/**
	 * Devuelve al nodo búsqueda que generó a este nodo como sucesor.
	 * @return nodo antecesor en la solución.
	 */
	public NodoBusqueda padre() {
		return padre;
	}
	
	/**
	 * Devuelve la distancia de la mejor ruta conocida hasta el momento.
	 * @return Valor de la función g(n).
	 */
	public int gn() {
		return gn;
	}
    
    /**
     * Función para obtener el estado de la función fn.
     * @return Valor de la función f(n).
     */
    public int fn(){
        return gn + estado.hn();
    }
    
    /**
     * Obtenemos todos los sucesores posibles respecto al estado actual del nodo.
     * @return Lista con los sucesores al nodo actual.
     */
    public LinkedList<NodoBusqueda> getSucesores(){
        // TODO: lista de nodos con los estados sucesores, con sus
		// atributos configurados adecuadamente.
        // Sucesores
        LinkedList<NodoBusqueda> sucesores = new LinkedList<>();
        
        // Movimientos posibles
        Movimiento[] movimientos = {
                                    Movimiento.ARRIBA,
                                    Movimiento.ABAJO,
                                    Movimiento.DERECHA,
                                    Movimiento.IZQUIERDA};
        
        // Aplicamos todos los movimientos
        for (int i = 0 ; i < movimientos.length; i++){
            // Movimiento
            Movimiento  mov = movimientos[i];
            Estado e = this.estado.aplicaAccion(mov);
            // Verificamos cuales nos llevan a un estado valido
            if (e != null){
                // Nodo sucesor
                NodoBusqueda sucesor = new NodoBusqueda(e);
                // Asignamos el padre
                sucesor.padre = this;
                // Guardamos el movimiento realizado para llegar al nodo
                sucesor.accionPadre = mov;
                // Asignamos g(n)
                sucesor.gn = this.gn + mov.costo();
                // Agregamos el sucesor a sucesores
                sucesores.add(sucesor);
            }
        }
        
        // Regresamos la lista
        return sucesores;
    }
    
    /**
     * Guarda la referencia al padre
     * @param padre nuevo padre
     */
    public void setPadre(NodoBusqueda padre){
        this.padre = padre;
    }
    
    @Override
    public int compareTo(NodoBusqueda nb){
        return fn() - nb.fn();
    }
    
    @Override
    public boolean equals(Object o){
		if (!(o instanceof NodoBusqueda) || o == null) return false;
        NodoBusqueda otro = (NodoBusqueda)o;
        return estado.equals(otro.estado);
    }
}
