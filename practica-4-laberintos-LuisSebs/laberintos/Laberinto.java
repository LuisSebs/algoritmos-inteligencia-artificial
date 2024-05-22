package laberintos;

import processing.core.PApplet;

import java.util.Collections;
import java.util.LinkedList;
import java.util.Random;
import java.util.Stack;

/**
 * Clase que crea un laberinto con Processing.
 * @author Sara
 * @author Baruch
 */
public class Laberinto extends PApplet {
    int alto = 10;            // Altura (en celdas) de la cuadricula.
    int ancho = 10;           // Anchura (en celdas) de la cuadricula.
    int celda = 40;           // Tamanio de cada celda cuadrada (en pixeles).
    ModeloLaberinto modelo;   // El objeto que representa el modelo del laberinto.

    @Override
    public void setup() {
        frameRate(60);
        background(50);
        modelo = new ModeloLaberinto(ancho, alto, celda);
    }
    
    @Override
    public void settings() {
        size(ancho * celda, (alto * celda));
    }
    
    /**
     * Pintar el mundo del modelo.
     */
    @Override
    public void draw() {

      // Color del fondo
      int rF = 69, gF = 25, bF = 82;

      // Color de las casillas visitadas
      int rC= 102, gC = 37, bC = 73;

      // Color de los muros
      int rM = 174, gM = 68, bM = 90;

      // Color casilla actual
      int rA = 243, gA = 159, bA = 90;

      for (int i = 0; i < alto; i++)
        for (int j = 0; j < ancho; j++){
                  // Si la celda es la actual
                  if (modelo.actual == modelo.mundo[i][j]){
                    fill(rA, gA, bA);
                    stroke(rA, gA, bA);
                  }else{
                    // En caso contrario
                    if (modelo.mundo[i][j].estado){
                      // Si la casilla no ha sido visitada
                      fill(rF, gF, bF);
                      stroke(rM,gM,bM);
                    }else{
                      // Si la casilla ya fue visitada
                      fill(rC, gC, bC);
                      stroke(rM,gM,bM);
                    }
                  }

                  // Pintamos los muros activos
                  rect(j * modelo.tamanio, i * modelo.tamanio, modelo.tamanio, modelo.tamanio);
                  // En caso de que las paredes de las celdas ya no se encuentren activas
                  if(!modelo.mundo[i][j].pared_1){
                      stroke(rC, gC, bC);
                      line(j * modelo.tamanio, i * modelo.tamanio, ((j + 1) * modelo.tamanio), i * modelo.tamanio);                    
                  }
                  if(!modelo.mundo[i][j].pared_2){
                      stroke(rC, gC, bC);
                      line((j * modelo.tamanio) + modelo.tamanio, i * modelo.tamanio, (j + 1) * modelo.tamanio, (((i + 1) * modelo.tamanio)));
                  }
                  if(!modelo.mundo[i][j].pared_3){
                      stroke(rC, gC, bC);
                      line(j * modelo.tamanio, (i * modelo.tamanio) + modelo.tamanio, ((j + 1) * modelo.tamanio), ((i + 1) * modelo.tamanio));                    
                  }
                  if(!modelo.mundo[i][j].pared_4){
                      stroke(rC, gC, bC);
                      line(j * modelo.tamanio, i * modelo.tamanio, j * modelo.tamanio, ((i + 1) * modelo.tamanio));               
                  }
          }
      // Ejecutamos el siguiente paso de la construcción del laberinto
      modelo.siguientePaso();
    }

    /**
     * Clase que representa cada celda de la cuadricula.
     */
    class Celda{
        int celdaX; 
        int celdaY;
        boolean pared_1;
        boolean pared_2;
        boolean pared_3;
        boolean pared_4;
        boolean estado;
        
        /** Constructor de una celda.
          *@param celdaX Coordenada en x
          *@param celdaY Coordenada en y
          *@param estado Estado de la celda. true si no ha sido visitada, false en otro caso.
        */
        Celda(int celdaX, int celdaY, boolean estado){
          this.celdaX = celdaX;
          this.celdaY = celdaY;
          this.estado = estado;
          this.pared_1 = true; // Booleano que representa la pared de arriba
          this.pared_2 = true; // Booleano que representa la pared de la derecha
          this.pared_3 = true; // Booleano que representa la pared de abajo
          this.pared_4 = true; // Booleano que representa la pared de la izquierda

          // Borramos las paredes correspondientes a los bordes del laberinto
          if (this.celdaX == 0){
            // La pared de la izquierda no esta disponible (se sale de la cuadricula)
            this.pared_4 = false;
          }
          if(this.celdaX == ancho-1){
            // La pared de la derecha no esta disponible (se sale de la cuadricula)
            this.pared_2 = false;
          }
          if(this.celdaY == 0){
            // la pared de arriba no esta disponible (se sale de la cuadricula)
            this.pared_1 = false;
          }
          if(this.celdaY == alto-1){
            // la pared de abajo no esta disponible (se sale de la cuadricula)
            this.pared_3 = false;
          }
        }
    }  

    /**
     * Clase que modela el laberinto, es decir, crea el mundo del laberinto.
     */
    class ModeloLaberinto extends Thread{
        int ancho, alto;  // Tamaño de celdas a lo largo y ancho de la cuadrícula.
        int tamanio;  // Tamaño en pixeles de cada celda.
        Celda[][] mundo;  // Mundo de celdas
        // Atrbituos extra
        /**
         * Celda actual
         */
        Celda actual; 
        /**
         * Pila para hacer backtracking
         */
        Stack<Celda> pila = new Stack<>();
        /**
         * Objeto random para obtener numeros random
         */
        Random rn = new Random();

      /** Constructor del modelo
       * @param ancho Cantidad de celdas a lo ancho en la cuadricula.
       * @param ancho Cantidad de celdas a lo largo en la cuadricula.
       * @param tamanio Tamaño (en pixeles) de cada celda cuadrada que compone la cuadricula.
       */
      ModeloLaberinto(int ancho, int alto, int tamanio){
        this.ancho = ancho;
        this.alto = alto;
        this.tamanio = tamanio;
        mundo = new Celda[alto][ancho];
        for(int i = 0; i < alto; i++)
          for(int j = 0; j < ancho; j++)
            mundo[i][j] = new Celda(j,i, true);
        // seleccionamos una celda aleatoria del mundo (inicial/actual)
        int x = rn.nextInt(alto);
        int y = rn.nextInt(ancho);
        this.actual = mundo[x][y];
        // marcamos la casilla como visitada
        this.actual.estado = false;
         // agregamos a la pila
        pila.add(actual);
      }

      /**
       * Realiza el siguiente paso
       * de recorrer un laberinto.
       */
      public void siguientePaso(){
        // Mientras haya elementos en la pila 
        // ó a partir de la celda actual ya no
        // se pueda expandir más.
        if (!pila.isEmpty() || (siguiente(actual)!=null)){
            // Obtenemos la siguiente casilla a la cual moverse (si la hay)
            Celda siguiente = siguiente(actual);
            if (siguiente == null){
              // Si no hay casilla a la que moverse se procede
              // a expulsar una celda de la pila y la cambiamos
              // con la casilla actual
              actual = pila.pop();
            }
        }
      }

      /**
       * Regresa la siguiente casilla a la que puede moverse
       * la celda c, esto es en base a las direcciones a las
       * que puede moverse, cuales de ellas no contienen 
       * casillas ya visitadas.
       * @param c casilla a partir de la cual determinamos
       * la siguiente casilla.
       * @return La siguiente casilla a la que puede moverse
       * regresa null si no puede moverse a ninguna otra casilla
       */
      public Celda siguiente(Celda c){
        // Posicion de la celda c
        int x = actual.celdaX;
        int y = actual.celdaY;
        Celda siguiente = null;
        // Extraemos todas las posiciones a las que puede moverse a partir de la celda actual (c)
        LinkedList<Integer> direcciones = direcciones(c);
        // De las direcciones a las que se puede mover debemos determinar
        // si en esa direccion no esta una casilla ya visitada
        LinkedList<Integer> direccionesSinCasillaVisitada = direccionesSinVisitar(c, direcciones);
        // Si hay alguna casilla a la cual moverse
        if (!direccionesSinCasillaVisitada.isEmpty()){
          // Regresamos una direccion aleatoria,
          // revolvemos la lista de direcciones
          Collections.shuffle(direccionesSinCasillaVisitada);
          // Obtenemos la primer direccion de la lista
          int direccionAleatoria = direccionesSinCasillaVisitada.pop();
          // Asignamos la siguiente casilla a la cual moverse
          switch (direccionAleatoria) {
            case 1:
              siguiente = mundo[y-1][x]; // Obtenemos la siguiente casilla
              c.pared_1 = false; // Borramos pared
              siguiente.pared_3 = false; // Borramos pared
              break;
            case 2:
              siguiente = mundo[y][x+1]; // Obtenemos la siguiente casilla
              c.pared_2 = false; // Borramos pared
              siguiente.pared_4 = false; // Borramos pared
              break;
            case 3:
              siguiente = mundo[y+1][x]; // Obtenemos la siguiente casilla
              c.pared_3 = false; // Borramos pared
              siguiente.pared_1 = false; // Borramos pared
              break;
            case 4:
              siguiente = mundo[y][x-1]; // Obtenemos la siguiente casilla
              c.pared_4 = false; // Borramos pared
              siguiente.pared_2 = false; // Borramos pared
              break;
          }
          // Marcamos la casilla como visitada
          siguiente.estado = false;
          // Empujamos la celda a la pila
          pila.add(siguiente);
          // Actualizamos la celda actual
          actual = siguiente;
        }
        // Regresamos la siguiente casilla a la que se movio
        // si nunca se cambio el valor de siguiente
        // significa que no hubo casilla a la cual moverse
        return siguiente;
      }

      /**
       * Regresa la direcciones a las que puede moverse
       * a partir de una casilla c.
       * @param c casilla cuyas paredes nos ayudan a 
       * determinar las direcciones disponibles.
       * @return una lista de direcciones a las
       * que se puede mover a partir de c.
       */
      public LinkedList<Integer> direcciones(Celda c){  
        // Extraemos todas las posiciones a las que puede moverse a partir de la celda actual (c)
        LinkedList<Integer> direcciones = new LinkedList<>();
        // Almacenamos las direcciones disponibles
        if (c.pared_1){
          direcciones.add(1);
        }
        if (c.pared_2){
          direcciones.add(2);
        }
        if (c.pared_3){
          direcciones.add(3);
        }
        if (c.pared_4){
          direcciones.add(4);
        }
        return direcciones;
      }

      /**
       * A partir de una celda y una lista de direcciones
       * a las que puede moverse una celda c, regresa
       * las direcciones donde hay celdas sin visitar.
       * @param c celda para obtener la posicion en 
       * el mundo.
       * @param dirs direcciones a las que movernos
       * a partir de la posicion de la casilla c.
       * @return direcciones a las que puede moverse
       * le casilla c donde no hay nodos visitados.
       */
      public LinkedList<Integer> direccionesSinVisitar(Celda c, LinkedList<Integer> dirs){
        // Posicion de la celda c
        int x = c.celdaX;
        int y = c.celdaY;
        
        LinkedList<Integer> direccionesSinCasillaVisitada = new LinkedList<>();
        
        for (int direccion : dirs){
          // Iterador de casillas
          Celda i = null;
          switch (direccion) {
            case 1:
              i = mundo[y-1][x];
              break;
            case 2:
              i = mundo[y][x+1];
              break;
            case 3:
              i = mundo[y+1][x];
              break;
            case 4:
              i = mundo[y][x-1];
              break;
          }
          // Si la casilla no ha sido visitada
          if (i.estado){
            // La agregamos a la lista
            direccionesSinCasillaVisitada.add(direccion);
          }
        }

        return direccionesSinCasillaVisitada;
      }

    }

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
         PApplet.main(new String[] { "laberintos.Laberinto" });
    }

}
