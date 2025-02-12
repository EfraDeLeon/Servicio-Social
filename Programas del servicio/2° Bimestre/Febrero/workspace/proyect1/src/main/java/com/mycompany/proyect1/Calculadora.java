/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.proyect1;

/**
 *
 * @author Efra
 */

public class Calculadora  {
    public static void main(String[] args) {
        Main calc = new Main();
        
        System.out.println(calc.sumar(2, 3));          // Salida: 5
        System.out.println(calc.sumar(1, 2, 3));      // Salida: 6
        System.out.println(calc.sumar(2.5, 3.7));     // Salida: 6.2
    }
}

class Main {
    // Suma dos números enteros
    public int sumar(int a, int b) {
        return a + b;
    }

    // Suma tres números enteros
    public int sumar(int a, int b, int c) {
        return a + b + c;
    }

    // Suma dos números decimales
    public double sumar(double a, double b) {
        return a + b;
    }
}