package recocido;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;


public class SolucionTSP extends Solucion{

    // Problema a resolver
    DatosPAV problema;

    // Ruta del viajero
    public int[] ruta;

    /**
     * Constructor que recibe un problema y inicializa
     * en base al problema la ruta.
     * @param problema problema del viajero
     */
    public SolucionTSP(DatosPAV problema){
    
        // Ciudades
        List<Integer> ciudades = new ArrayList<>();

        // Calculamos de manera aleatoria la ruta
        int numCiudades = problema.numCiudades();
        for (int i = 0; i < numCiudades; i++){
            int codigoCiudad = problema.código(i);
            ciudades.add(codigoCiudad);
        }

        // Permutamos
        Collections.shuffle(ciudades);

        // Agregamos la ciudad inicial al final de la ruta
        ciudades.add(ciudades.get(0));

        // Tamaño de la ruta
        int n = ciudades.size();

        // Inicializacion ruta
        this.ruta = new int[n];

        // Agregamos la ruta inicial
        for (int i = 0 ; i < n; i++){
            ruta[i] = ciudades.get(i);
        }

        // Guardamos el problema
        this.problema = problema;
    }

    /**
     * Constructor que recibe un problema y la ruta
     * del ajente viajero. Ya no es necesario inicializarla
     * a base del problema.
     * @param problema problema del viajero
     * @param ruta ruta del viajero
     */
    public SolucionTSP(DatosPAV problema, int[] ruta){
        this.problema = problema;
        this.ruta = ruta;
    }

    @Override
    public SolucionTSP siguienteSolucion() {
        // Numero de ciudades
        int n = ruta.length;

        // Ciudades intermedias
        int[] ciudadesIntermedias = Arrays.copyOfRange(ruta, 1, n-1);

        // Numero de ciudades intermedias
        int m = ciudadesIntermedias.length;
        
        // Seleccionamos indices aleatorios de dos ciudades intermedias
        int indiceR1 = (int) (m * Math.random());
        int indiceR2 = (int) (m * Math.random());

        // Obtenemos las ciudades a intercambiar
        int c1 = ciudadesIntermedias[indiceR1];
        int c2 = ciudadesIntermedias[indiceR2];

        // Intercambiamos las ciudades intermedias
        ciudadesIntermedias[indiceR2] = c1;
        ciudadesIntermedias[indiceR1] = c2;

        // Nueva ruta
        int[] newRuta = new int[n];

        // Agregamos el inicio y el final
        int inicioYFin = ruta[0];
        newRuta[0] = inicioYFin;
        newRuta[n-1] = inicioYFin;

        // Agregamos las ciudades a la nueva ruta
        for (int i = 0; i < m; i++){
            newRuta[i+1] = ciudadesIntermedias[i];
        }

        // Regresamos la nueva solucion
        return new SolucionTSP(this.problema, newRuta);
    }

    @Override
    public float evaluar() {
        // ciudades -> codigoCiudades
        double calificacion = 0;
        for (int i = 0; i < ruta.length - 1; i++){
            int ciudad1 = ruta[i];
            int ciudad2 = ruta[i+1];

            double x1 = this.problema.coordenadas(ciudad1)[0];
            double y1 = this.problema.coordenadas(ciudad1)[1];

            double x2 = this.problema.coordenadas(ciudad2)[0];
            double y2 = this.problema.coordenadas(ciudad2)[1];

            calificacion += distanciaEuclideana(x1, y1, x2, y2);
        }

        return (float) calificacion;
    }

    @Override
    public String toString() {
        String str = "[";
        // Tamaño de la ruta
        int n = this.ruta.length;
        for (int i = 0; i < n; i++){
            if (i == n-1){
                str += this.ruta[i];
            }else{
                str += this.ruta[i] + ", ";
            }
        }
        
        str += "]";
        return str;
    }
    
    /**
     * Funcion auxiliar que calcula la distancia Euclideana
     * entre dos ciudades en base a sus coordenadas
     * @param x1 coordenada x de la primer ciudad
     * @param y1 coordenada y de la primer ciudad
     * @param x2 coordenada x de la segunda ciudad
     * @param y2 coordenada y de la segunda ciudad
     * @return la distancia euclideana
     */
    public double distanciaEuclideana(double x1, double y1, double x2, double y2){
        // distancia = sqrt((x2-x1)² + (y2-y1)²)
        return Math.sqrt(Math.pow(x2-x1,2) + Math.pow(y2-y1,2));
    }
}
