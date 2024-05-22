/*
 * Código utilizado para el curso de Inteligencia Artificial.
 * Se permite consultarlo para fines didácticos en forma personal,
 * pero no esta permitido transferirlo resuelto a estudiantes actuales o potenciales.
 */
package pacman.personajes.navegacion;

import java.util.logging.Level;
import java.util.logging.Logger;

import java.util.HashMap;
import java.util.LinkedList;
import java.util.PriorityQueue;
import javafx.scene.paint.Color;
import pacman.personajes.Movimiento;

/**
 * Clase donde se define en algoritmo de A* para que se use en el fantasma.
 * @author baruch
 * @author blackzafiro
 */
public class AEstrella extends Algoritmo {
	
	private final static Logger LOGGER = Logger.getLogger("pacman.personajes.navegacion.AEstrella");
	static { LOGGER.setLevel(Level.FINE); }
	
	private PriorityQueue<NodoBusqueda> listaAbierta;   // Cola de prioridad de donde obtendremos los nodos
	                                                    // sobre los que se realizará el algoritmo.
	private HashMap<Estado, Estado> listaCerrada;       // Tabla de dispersión donde se agregan todos los estados
                                                        // que se terminó de revisar.
    private Estado estadoFinal;                         // Casilla donde se encuentra pacman.
    private boolean terminado;                          // Define si nuestro algoritmo ha terminado.
    private NodoBusqueda nodoSolucion;                  // Nodo a partir del cual se define la solución,
	                                                    // porque ya se encontró la mejor rutal al estado meta.
    
    // Atributos extra
    private NodoBusqueda nodoActual; // Nodo actual en el espacio de busqueda
	
    /**
     * Inicializador del algoritmo.
	 * Se debe mandar llamar cada vez que cambien el estado incial y el estado
	 * final.
     * @param estadoInicial Pasillo donde se encuentra el fantasma.
     * @param estadoFinal Pasillo donde se encuentra pacman.
     */
    private void inicializa(Estado estadoInicial, Estado estadoFinal){
		this.estadoFinal = estadoFinal;
        this.terminado = false;
		this.nodoSolucion = null;
        this.listaAbierta = new PriorityQueue<>();
        this.listaCerrada = new HashMap<>();
        estadoInicial.calculaHeuristica(estadoFinal);
        this.listaAbierta.offer(new NodoBusqueda(estadoInicial));
    }
    
    /**
     * Función que realiza un paso en la ejecución del algoritmo.
     */
    private void expandeNodoSiguiente(){
        
        // Sacamos al nodo actual de la lista abierta
        nodoActual = listaAbierta.poll();
        
        // Lo agregamos a la lista cerrada
        listaCerrada.put(nodoActual.estado(),nodoActual.estado());
        
        // Si llegamos a la meta
        if (nodoActual.estado() == estadoFinal){
            terminado = true;
            return;
        }
        
        // Nos fijamos en los vecinos alcanzables
        for (NodoBusqueda vecino : nodoActual.getSucesores()){
            // Si no esta en la lista Cerrada
            if (!listaCerrada.containsKey(vecino.estado())){
                // Si no esta en la lista bierta
                if (!listaAbierta.contains(vecino)){
                    // Asignamos el padre
                    vecino.setPadre(nodoActual);
                    // Asignamos h(n)
                    vecino.estado().calculaHeuristica(estadoFinal);
                    // g(n) ya esta calculado
                    // Lo agregamos a la lista abierta
                    listaAbierta.add(vecino);
                }else{
                    // Verificamos si del nodo actual al nodo vecino se llega con menor
                    // costo que desde su padre actual.
                    NodoBusqueda nodoListaAbierta = null;
                    for (NodoBusqueda nodo : listaAbierta){
                        // Usamos equals para verificar si la informacion es la misma,
                        // no la referencia
                        if (vecino.equals(nodo)){
                            nodoListaAbierta = nodo;
                            break;
                        }
                    }
                    if (nodoListaAbierta.gn() > vecino.gn()){
                        vecino.setPadre(vecino);
                        // h(n) ya esta calculada
                        // g(n) ya esta calculada
                        listaAbierta.remove(nodoListaAbierta);
                        listaAbierta.add(vecino);
                    }
                }
            }
        }
    }
	
    /**
     * Se puede llamar cuando se haya encontrado la solución para obtener el
     * plan desde el nodo inicial hasta la meta.
     * @return secuencia de movimientos que llevan del estado inicial a la meta.
     */
    private LinkedList<Movimiento> generaTrayectoria() {
         LinkedList<Movimiento> trayecto = new LinkedList<>();

        // Iterador de estados
        NodoBusqueda iterador = this.nodoActual;
        // Mientras no hayamos llegado a la raiz
        while(iterador.padre() != null){
            // Guardamos las acciones realizadas en reversa (por eso insertamos al inicio)
            trayecto.add(0, iterador.accionPadre());
            iterador = iterador.padre();
        }
        return trayecto;
    }

    /**
     * Pinta las celdas desde el nodo solución hasta el nodo inicial
     */
    private void pintaTrayectoria(Color color) {
            if (nodoSolucion == null) return;
            NodoBusqueda temp = nodoSolucion.padre();
            while(temp.padre() != null) {
                    temp.estado().pintaCelda(color);
                    temp = temp.padre();
            }
    }
    
    /**
     * Función que ejecuta A* para determinar la mejor ruta desde el fantasma,
	 * cuya posición se encuetra dentro de <code>estadoInicial</code>, hasta
	 * Pacman, que se encuentra en <code>estadoFinal</code>.
	 * @return Una lista con la secuencia de movimientos que Sombra debe
	 *         ejecutar para llegar hasta PacMan.
     */
	@Override
    public LinkedList<Movimiento> resuelveAlgoritmo(Estado estadoInicial, Estado estadoFinal){
		
        // TODO:
        // Reemplaza este código para que ejecute el algoritmo A* desde
        // estadoInicial hasta estadoFinal y genere la lista de acciones
        // Verificamos si aún no hemos llegado a pacman

        this.inicializa(estadoInicial, estadoFinal);

        // Mientras no hayamos llegado a pacman (estado final)
        while(!this.terminado){
            // Buscamos la mejor ruta para llegar a el
            this.expandeNodoSiguiente();
        }

        // Regresamos el trayecto
        return this.generaTrayectoria();
		
    }
	
}
