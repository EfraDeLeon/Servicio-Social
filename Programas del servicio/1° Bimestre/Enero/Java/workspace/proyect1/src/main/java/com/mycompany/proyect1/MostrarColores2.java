/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.proyect1;

import java.awt.*;
import java.awt.event.*;
import javax.swing.*;
/**
 *
 * @author Efra
 */
public class MostrarColores2 extends JFrame{
    private JButton cambiarColorBoton;
    private Color color = Color.lightGray;
    private Container contenedor;
    
    public MostrarColores2(){
        super("Uso de JColorChooser");
        
        contenedor = getContentPane();
        contenedor.setLayout(new FlowLayout());
        
        cambiarColorBoton = new JButton("Cambia de color");
        cambiarColorBoton.addActionListener( new ActionListener() {
            
            public void actionPerformed(ActionEvent evento) {
                color = JColorChooser.showDialog(MostrarColores2.this, "Seleccione un color", color);
                if(color == null)
                    color = Color.lightGray;
                
                contenedor.setBackground(color);
            }
            
        }
    );
    
    contenedor.add(cambiarColorBoton);
    
    setSize(400, 130);
    setVisible(true);
    }
    public static void main(String args[]){
    MostrarColores2 aplicacion = new MostrarColores2();
    aplicacion.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}

