/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.proyect1;
import javax.swing.*;
import java.text.DecimalFormat;
/**
 *
 * @author Efra
 */
public class PruebaThis {
    
    public static void main(String[] args) {
        HoraSimple hora = new HoraSimple(12, 30, 19);
        
        JOptionPane.showMessageDialog(null, hora.crearCadena(), "Demostración de la referencia \"this\"",JOptionPane.INFORMATION_MESSAGE);
        System.exit(0);
    }
}
class HoraSimple{
    private int hora;
    private int minuto;
    private int segundo;
    public HoraSimple(int hora, int minuto,int segundo){
        this.hora = hora;
        this.minuto = minuto;
        this.segundo = segundo;
    }
    public String crearCadena()
    {
        return "this.aStringEsandar(): " + this.aStringEstandar() + "\naStringEstandar(): " + aStringEstandar();
        
    }
    
    public String aStringEstandar(){
        DecimalFormat dosDigitos = new DecimalFormat("00");
        return dosDigitos.format(this.hora) + ":" + dosDigitos.format(this.minuto) + ":" + dosDigitos.format(this.segundo);
        
    }
}