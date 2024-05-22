/*
 * No redistribuir.
 */
package gatos;

import java.util.LinkedList;

/**
 * Clase para representar un estado del juego del gato. Cada estado sabe cómo
 * generar a sus sucesores.
 *
 * @author Vero
 */
public class Gato {

    public static final int MARCA1 = 1;             // Número usado en el tablero del gato para marcar al primer jugador.
    public static final int MARCA2 = 4;             // Se usan int en lugar de short porque coincide con el tamaÃ±o de la palabra, el código se ejecuta ligeramente más rápido.

    int[][] tablero = new int[3][3];     // Tablero del juego
    Gato padre;                          // Quién generó este estado.
    LinkedList<Gato> sucesores;          // Posibles jugadas desde este estado.
    boolean jugador1 = false;            // Jugador que tiró en este tablero.
    boolean hayGanador = false;          // Indica si la última tirada produjo un ganador.
    int tiradas = 0;                     // Número de casillas ocupadas.

    /**
     * Constructor del estado inicial.
     */
    Gato() {}

    /**
     * Constructor que copia el tablero de otro gato y el número de tiradas
     */
    Gato(Gato g) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                tablero[i][j] = g.tablero[i][j];
            }
        }
        tiradas = g.tiradas;
    }

    /**
     * Indica si este estado tiene sucesores expandidos.
     */
    int getNumHijos() {
        if (sucesores != null) {
            return sucesores.size();
        } else {
            return 0;
        }
    }

    /* Función auxiliar.
     * Dada la última posición en la que se tiró y la marca del jugador
     * calcula si esta jugada produjo un ganador y actualiza el atributo correspondiente.
     * 
     * Esta función debe ser lo más eficiente posible para que la generación del árbol no sea demasiado lenta.
     */
    private void hayGanador(int ren, int col, int marca) {
        // Horizontal
        if (tablero[ren][(col + 1) % 3] == marca && tablero[ren][(col + 2) % 3] == marca) {
            hayGanador = true;
            return;
        }
        // Vertical
        if (tablero[(ren + 1) % 3][col] == marca && tablero[(ren + 2) % 3][col] == marca) {
            hayGanador = true;
            return;
        }
        // Diagonal
        if ((ren != 1 && col == 1) || (ren == 1 && col != 1)) {
			hayGanador = false;  // No debiera ser necesaria.
            return; // No pueden hacer diagonal
        }      // Centro y esquinas
        if (col == 1 && ren == 1) {
            // Diagonal \
            if (tablero[0][0] == marca && tablero[2][2] == marca) {
                hayGanador = true;
                return;
            }
            if (tablero[2][0] == marca && tablero[0][2] == marca) {
                hayGanador = true;
                return;
            }
        } else if (ren == col) {
            // Diagonal \
            if (tablero[(ren + 1) % 3][(col + 1) % 3] == marca && tablero[(ren + 2) % 3][(col + 2) % 3] == marca) {
                hayGanador = true;
                return;
            }
        } else {
            // Diagonal /
            if (tablero[(ren + 2) % 3][(col + 1) % 3] == marca && tablero[(ren + 1) % 3][(col + 2) % 3] == marca) {
                hayGanador = true;
                return;
            }
        }
    }

    /* Función auxiliar.
     * Coloca la marca del jugador en turno para este estado en las coordenadas indicadas.
     * Asume que la casilla está libre.
     * Coloca la marca correspondiente, verifica y asigna la variable si hay un ganador.
     */
    private void tiraEn(int ren, int col) {
        tiradas++;
        int marca = (jugador1) ? MARCA1 : MARCA2;
        tablero[ren][col] = marca;
        hayGanador(ren, col, marca);
    }

    /**
     * Funcion auxiliar para generar los sucesores del juego
     * de gato sin considerar simetrias.
     */
    void generaSucesoresSinSimetrias() {
        // Obtenemos los espacios disponibles donde se puede tirar y creamos copias del gato
        for (int i = 0; i < tablero.length; i++){
            for (int j = 0; j < tablero[0].length; j++){
                // Si la posicion esta libre
                if(tablero[i][j] == 0){
                    // Creamos una copia del gato
                    Gato copia = new Gato(this);
                    // Asignamos al padre
                    copia.padre = this;
                    // Asignamos el jugador que tiro (true: jugador1, false: jugador2)
                    copia.jugador1 = !this.jugador1;
                    // Tiramos en la posicion libre
                    copia.tiraEn(i, j);
                    // Como no estamos considerando simetrias solo los agregamos a la lista de sucesores
                    sucesores.add(copia);
                }
            }
        }
    }

    /**
     * Funcion auxiliar para generar los sucesores del juego
     * de gato considerando simetrias.
     */
    void generaSucesoresConSimetrias() {
        // Obtenemos los espacios disponibles donde se puede tirar y creamos copias del gato
        for (int i = 0; i < tablero.length; i++){
            for (int j = 0; j < tablero[0].length; j++){
                // Si la posicion esta libre
                if(tablero[i][j] == 0){
                    // Creamos una copia del gato
                    Gato copia = new Gato(this);
                    // Asignamos al padre
                    copia.padre = this;
                    // Asignamos el jugador que tiro (true: jugador1, false: jugador2)
                    copia.jugador1 = !this.jugador1;
                    // Tiramos en la posicion libre
                    copia.tiraEn(i, j);
                    // Verificamos simetrias
                    if (sucesores.isEmpty()){
                        // Lo agregamos (puesto que no tenemos con quien compararlo)
                        sucesores.add(copia);
                    }else{
                        // Verificacion si es es igual a algun otro gato por simetria (suponemos que no)
                        boolean iguales = false;
                        for (Gato gato : sucesores){
                            if(gato.equals(copia)){
                                iguales = true;
                                break;
                            }
                        }
                        // Si pasa todas las comparaciones 
                        if (!iguales){
                            // Lo agregamos
                            sucesores.add(copia);
                        }
                    }
                }
            }
        }
    }
    
    /**
     * ------- *** ------- *** -------
     * Este es el método que se deja como práctica.
     * ------- *** ------- *** -------
     * Crea la lista sucesores y 
     * agrega a todos los estados que sujen de tiradas válidas. Se consideran
     * tiradas válidas a aquellas en una casilla libre. Además, se optimiza el
     * proceso no agregando estados con jugadas simétricas. Los estados nuevos
     * tendrán una tirada más y el jugador en turno será el jugador
     * contrario.
     */
    LinkedList<Gato> generaSucesores() {
        if (hayGanador || tiradas == 9) {
            return null; // Es un estado meta.
        }
        // Sucesores del gato actual
        sucesores = new LinkedList<>();

        //generaSucesoresSinSimetrias();
        generaSucesoresConSimetrias();
        
        return sucesores;
    }

    // ------- *** ------- *** -------
    // Serie de funciones que revisan la equivalencia de estados considerando las simetrías de un cuadrado.
    // ------- *** ------- *** -------
    // http://en.wikipedia.org/wiki/Examples_of_groups#The_symmetry_group_of_a_square_-_dihedral_group_of_order_8
    // ba es reflexion sobre / y ba3 reflexion sobre \.
    
    /**
     * Revisa si ambos gatos son exactamente el mismo.
     */
    boolean esIgual(Gato otro) {
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                if (tablero[i][j] != otro.tablero[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }

    /**
     * Al reflejar el gato sobre la diagonal \ son iguales (ie traspuesta)
     */
    boolean esSimétricoDiagonalInvertida(Gato otro) {
        
        boolean c1 = this.tablero[0][0] == otro.tablero[0][0];
        boolean c2 = this.tablero[0][1] == otro.tablero[1][0];
        boolean c3 = this.tablero[0][2] == otro.tablero[2][0];
        
        boolean c4 = this.tablero[1][0] == otro.tablero[0][1];
        boolean c5 = this.tablero[1][1] == otro.tablero[1][1];
        boolean c6 = this.tablero[1][2] == otro.tablero[2][1];

        boolean c7 = this.tablero[2][0] == otro.tablero[0][2];
        boolean c8 = this.tablero[2][1] == otro.tablero[1][2];
        boolean c9 = this.tablero[2][2] == otro.tablero[2][2];
        
        return c1 && c2 && c3 && c4 && c5 && c6 && c7 && c8 && c9;
    }

    /**
     * Al reflejar el gato sobre la diagonal / son iguales (ie traspuesta)
     */
    boolean esSimétricoDiagonal(Gato otro) {
        
        boolean c1 = this.tablero[0][0] == otro.tablero[2][2];
        boolean c2 = this.tablero[0][1] == otro.tablero[1][2];
        boolean c3 = this.tablero[0][2] == otro.tablero[0][2];

        boolean c4 = this.tablero[1][0] == otro.tablero[2][1];
        boolean c5 = this.tablero[1][1] == otro.tablero[1][1];
        boolean c6 = this.tablero[1][2] == otro.tablero[0][1];

        boolean c7 = this.tablero[2][0] == otro.tablero[2][0];
        boolean c8 = this.tablero[2][1] == otro.tablero[1][0];
        boolean c9 = this.tablero[2][2] == otro.tablero[0][0];
        
        
        return c1 && c2 && c3 && c4 && c5 && c6 && c7 && c8 && c9;
    }

    /**
     * Al reflejar el otro gato sobre la vertical son iguales
     */
    boolean esSimétricoVerticalmente(Gato otro) {
        
        // Tenemos que hacer las siguientes comparaciones
        boolean c1 = this.tablero[0][0] == otro.tablero[0][2];
        boolean c2 = this.tablero[0][1] == otro.tablero[0][1];
        boolean c3 = this.tablero[0][2] == otro.tablero[0][0];

        boolean c4 = this.tablero[1][0] == otro.tablero[1][2];
        boolean c5 = this.tablero[1][1] == otro.tablero[1][1];
        boolean c6 = this.tablero[1][2] == otro.tablero[1][0];

        boolean c7 = this.tablero[2][0] == otro.tablero[2][2];
        boolean c8 = this.tablero[2][1] == otro.tablero[2][1];    
        boolean c9 = this.tablero[2][2] == otro.tablero[2][0];
        
        return c1 && c2 && c3 && c4 && c5 && c6 && c7 && c8 && c9;
    }

    /**
     * Al reflejar el otro gato sobre la horizontal son iguales
     */
    boolean esSimétricoHorizontalmente(Gato otro) {
        
        /*
         * Se hicieron las comparaciones de esta manera ya que la estructura
         * del tablero de gato nunca cambia, por lo que podemos hacer las comparaciones
         * de manera directa, así tenemos mas certesa de las comparaciones que 
         * estamos haciendo. 
         */

        boolean c1 = this.tablero[0][0] == otro.tablero[2][0];
        boolean c2 = this.tablero[0][1] == otro.tablero[2][1];
        boolean c3 = this.tablero[0][2] == otro.tablero[2][2];

        boolean c4 = this.tablero[1][0] == otro.tablero[1][0];
        boolean c5 = this.tablero[1][1] == otro.tablero[1][1];
        boolean c6 = this.tablero[1][2] == otro.tablero[1][2];

        boolean c7 = this.tablero[2][0] == otro.tablero[0][0];
        boolean c8 = this.tablero[2][1] == otro.tablero[0][1];
        boolean c9 = this.tablero[2][2] == otro.tablero[0][2];

        return c1 && c2 && c3 && c4 && c5 && c6 && c7 && c8 && c9;
    }

    /**
     * Rota el otro tablero 90Â° en la dirección de las manecillas del reloj.
     */
    boolean esSimétrico90(Gato otro) {
        
        // Realizamos las siguientes comparaciones

        boolean c1 = this.tablero[0][0] == otro.tablero[2][0];
        boolean c2 = this.tablero[0][1] == otro.tablero[1][0];
        boolean c3 = this.tablero[0][2] == otro.tablero[0][0];
        
        boolean c4 = this.tablero[1][0] == otro.tablero[2][1];
        boolean c5 = this.tablero[1][1] == otro.tablero[1][1];
        boolean c6 = this.tablero[1][2] == otro.tablero[0][1];

        boolean c7 = this.tablero[2][0] == otro.tablero[2][2];
        boolean c8 = this.tablero[2][1] == otro.tablero[1][2];
        boolean c9 = this.tablero[2][2] == otro.tablero[0][2];
        
        return c1 && c2 && c3 && c4 && c5 && c6 && c7 && c8 && c9;
    }

    /**
     * Rota el otro tablero 180Â° en la dirección de las manecillas del reloj.
     */
    boolean esSimétrico180(Gato otro) {
        
        boolean c1 = this.tablero[0][0] == otro.tablero[2][2];
        boolean c2 = this.tablero[0][1] == otro.tablero[2][1];
        boolean c3 = this.tablero[0][2] == otro.tablero[2][0];

        boolean c4 = this.tablero[1][0] == otro.tablero[1][2];
        boolean c5 = this.tablero[1][1] == otro.tablero[1][1];
        boolean c6 = this.tablero[1][2] == otro.tablero[1][0];

        boolean c7 = this.tablero[2][0] == otro.tablero[0][2];
        boolean c8 = this.tablero[2][1] == otro.tablero[0][1];
        boolean c9 = this.tablero[2][2] == otro.tablero[0][0];
        
        return c1 && c2 && c3 && c4 && c5 && c6 && c7 && c8 && c9;
    }

    /**
     * Rota el otro tablero 270Â° en la dirección de las manecillas del reloj.
     */
    boolean esSimétrico270(Gato otro) {
        
        boolean c1 = this.tablero[0][0] == otro.tablero[0][2];
        boolean c2 = this.tablero[0][1] == otro.tablero[1][2];
        boolean c3 = this.tablero[0][2] == otro.tablero[2][2];

        boolean c4 = this.tablero[1][0] == otro.tablero[0][1];
        boolean c5 = this.tablero[1][1] == otro.tablero[1][1];
        boolean c6 = this.tablero[1][2] == otro.tablero[2][1];

        boolean c7 = this.tablero[2][0] == otro.tablero[0][0];
        boolean c8 = this.tablero[2][1] == otro.tablero[1][0];
        boolean c9 = this.tablero[2][2] == otro.tablero[2][0];
        
        return c1 && c2 && c3 && c4 && c5 && c6 && c7 && c8 && c9;
    }

    /**
     * Indica si dos estados del juego del gato son iguales, considerando
     * simetrías, de este modo el problema se vuelve manejable.
     */
    @Override
    public boolean equals(Object o) {
        Gato otro = (Gato) o;
        if (esIgual(otro)) {
            return true;
        }

        if (esSimétricoDiagonalInvertida(otro)) {
            return true;
        }
        if (esSimétricoDiagonal(otro)) {
            return true;
        }
        if (esSimétricoVerticalmente(otro)) {
            return true;
        }
        if (esSimétricoHorizontalmente(otro)) {
            return true;
        }
        if (esSimétrico90(otro)) {
            return true;
        }
        if (esSimétrico180(otro)) {
            return true;
        }
        if (esSimétrico270(otro)) {
            return true; // No redujo el diámetro máximo al agregarlo
        }
        return false;
    }

    /**
     * Devuelve una representación con caracteres de este estado. Se puede usar
     * como auxiliar al probar segmentos del código.
     */
    @Override
    public String toString() {
        char simbolo = jugador1 ? 'o' : 'x';
        String gs = "";
        for (int i = 0; i < 3; i++) {
            for (int j = 0; j < 3; j++) {
                gs += tablero[i][j] + " ";
            }
            gs += '\n';
        }
        return gs;
    }
}
