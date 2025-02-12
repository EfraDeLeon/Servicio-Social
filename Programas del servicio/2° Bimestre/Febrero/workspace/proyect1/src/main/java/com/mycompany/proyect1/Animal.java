/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.proyect1;

/**
 *
 * @author Efra
 */

public class Animal {
    public static void main(String[] args) {
        Main2 animal1 = new Perro();  // Polimorfismo: Animal se comporta como Perro
        Main2 animal2 = new Gato();  // Polimorfismo: Animal se comporta como Gato

        animal1.hacerSonido();  // Salida: El perro ladra: ¡Guau guau!
        animal2.hacerSonido();  // Salida: El gato maúlla: ¡Miau!
    }
}

class Main2 {
    public void hacerSonido() {
        System.out.println("El animal hace un sonido.");
    }
}

class Perro extends Main2 {
    @Override
    public void hacerSonido() {
        System.out.println("El perro ladra: ¡Guau guau!");
    }
}

class Gato extends Main2 {
    @Override
    public void hacerSonido() {
        System.out.println("El gato maúlla: ¡Miau!");
    }
}
