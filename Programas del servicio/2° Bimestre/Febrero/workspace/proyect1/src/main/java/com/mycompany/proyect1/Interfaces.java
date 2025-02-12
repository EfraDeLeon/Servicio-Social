/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.proyect1;

/**
 *
 * @author Efra
 */
interface Main3 {
    void dibujar();
}

class Circulo implements Main3 {
    @Override
    public void dibujar() {
        System.out.println("Dibujando un círculo.");
    }
}

class Cuadrado implements Main3 {
    @Override
    public void dibujar() {
        System.out.println("Dibujando un cuadrado.");
    }
}

public class Interfaces {
    public static void main(String[] args) {
        Main3 figura1 = new Circulo();
        Main3 figura2 = new Cuadrado();

        figura1.dibujar();  // Salida: Dibujando un círculo.
        figura2.dibujar();  // Salida: Dibujando un cuadrado.
    }
}
