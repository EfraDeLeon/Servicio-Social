/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package Ene31;
import java.util.Arrays;

/**
 *
 * @author Efra
 */
class FuncionB {
    public static void bubblesort(int[] valores) {
        int n = valores.length;
        boolean intercambio;

        do {
            intercambio = false;
            for (int i = 0; i < n - 1; i++) {
                if (valores[i] > valores[i + 1]) {
                    // Intercambiar valores
                    int temp = valores[i];
                    valores[i] = valores[i + 1];
                    valores[i + 1] = temp;
                    intercambio = true;
                }
            }
        } while (intercambio);
    }
}
