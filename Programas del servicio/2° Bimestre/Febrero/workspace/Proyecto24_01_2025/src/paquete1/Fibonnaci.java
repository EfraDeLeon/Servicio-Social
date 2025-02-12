/*
 * Programa que arroje los primeros 15 números de la serie de Fibonacci
 */
package paquete1;

public class Fibonnaci {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int a = 15;
		fibonnaci(a);
		
	}
	public static void fibonnaci(int a) {
		int one = 0, two = 1;
		System.out.println("Serie de Fibonacci hasta " + a + " términos:");
		for (int i = 0; i < a; i++) {
            System.out.print(one + " ");
            int siguiente = one + two;
            one = two;
            two = siguiente;
		}
	}
}

