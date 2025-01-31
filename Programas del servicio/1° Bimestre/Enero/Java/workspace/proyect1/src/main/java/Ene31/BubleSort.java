/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ene31;

import java.util.Scanner;
import Ene31.FuncionB;

/**
 *
 * @author Efra
 */
public class BubleSort {
    public static void main(String[] args) {
        System.out.println("Ingrese diez numeros");
        int[] valores = arreglo();
        imprimirArreglo(valores);
        FuncionB.bubblesort(valores);
        imprimirArreglo(valores);
    }
    public static int[] arreglo(){
        int[] valores = new int[10];
        try (Scanner scanner = new Scanner(System.in)) {
            for (int a = 0; a < 10; a++) {
                System.out.print("Numero " + (a + 1) + ": ");
                valores[a] = scanner.nextInt();
            }
        }
        return valores;
    }
    public static void imprimirArreglo(int[] arreglo) {
        for (int num : arreglo) {
            System.out.print(num + " ");
        }
        System.out.println();
    }
}

