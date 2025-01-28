/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.proyect1;
 
import javax.swing.JOptionPane;
/**
 *
 * @author Efra
 */
public class Proyect1 {

    public static void main(String[] args) {

		Panel mipanel = new Panel();
                mipanel.panelMostrar();
                mipanel.panelResta();
		
    }
}

class Panel{
    public void panelMostrar(){
        String primerNumero;
		String segundoNumero;
		
		int numero1;
		int numero2;
		int suma;
		
		primerNumero = JOptionPane.showInputDialog("Escriba el primer entero" );
		segundoNumero = JOptionPane.showInputDialog("Escriba el segundo entero" );
		
		numero1 = Integer.parseInt(primerNumero);
		numero2 = Integer.parseInt(segundoNumero);
		
		suma = numero1 + numero2;
		
		JOptionPane.showMessageDialog(null, "La suma es " + suma, "Resultados", JOptionPane.PLAIN_MESSAGE);
                //System.exit(0);
    }
    public void panelResta(){
        String primerNumero;
		String segundoNumero;
		
		int numero1;
		int numero2;
		int suma;
		
		primerNumero = JOptionPane.showInputDialog("Escriba el primer entero" );
		segundoNumero = JOptionPane.showInputDialog("Escriba el segundo entero" );
		
		numero1 = Integer.parseInt(primerNumero);
		numero2 = Integer.parseInt(segundoNumero);
		
		suma = numero1 - numero2;
		
		JOptionPane.showMessageDialog(null, "La resta es " + suma, "Resultados", JOptionPane.PLAIN_MESSAGE);
                System.exit(0);
    }
}