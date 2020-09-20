package GUI;

import java.awt.*;

import javax.swing.*;
import javax.swing.border.EmptyBorder;


public class Main 
{
	private JFrame frame;
	private JPanel mainPanel;
	private JButton b1;
	private JButton b2;
	private JLabel gameLabel;
	

	
	public Main() {
		gui();	
	}
	
	public void gui() {
		
		//Creating frame
        JFrame.setDefaultLookAndFeelDecorated(true);
        frame = new JFrame("Version 1.0");
        frame.setVisible(true);
        //frame.setSize(600, 400);//setting size of frame 600 width and 400 height.
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//Allows frame to exit, without it frame will not close
         
		//Creating Panel
		mainPanel = new JPanel();
		mainPanel.setBackground(Color.BLACK);//setting background of JPanel to be black 
        BoxLayout boxlayout = new BoxLayout(mainPanel, BoxLayout.Y_AXIS);//Setting Boxlayout for Jpanel
        mainPanel.setLayout(boxlayout);//BoxLayout.Y_AXIS adds panel components from top to bottom 
        //Set border for the panel
        mainPanel.setBorder(new EmptyBorder(new Insets(150, 200, 150, 200)));
        //mainPanel.setBorder(new EmptyBorder(new Insets(50, 80, 50, 80)));     
        
        
        //Creating Label that will contain Game title and adding it to our JPanel
        gameLabel = new JLabel("AMONG US");
		gameLabel.setForeground(Color.RED);//setting color of label text to Red
		gameLabel.setFont(new Font("Phosphate", Font.BOLD, 42));//setting font type and size for label
		mainPanel.add(gameLabel);
		mainPanel.add(Box.createRigidArea(new Dimension(0, 40)));//(width,height); used to insert spacing between the 2 components of 40pixels
		
		//Creating Button components to be placed on JPanel 
        b1 = new JButton("Online");
        b2 = new JButton("How To Play"); 
        mainPanel.add(b1);
        mainPanel.add(b2);
       /* 
        //Setting background image as Jlabel
        ImageIcon icon = new ImageIcon("/AmongUs_CSE442/src/GUI/pic.png"); 
        JLabel backG = new JLabel();
        backG.setIcon(icon);
        //Dimension d = new Dimension(icon.getIconWidth() + 10, icon.getIconHeight() + 10);
	    //backG.setSize(d);
	    //backG.setPreferredSize(d);
	    //backG.setMaximumSize(d);
	    //backG.setMinimumSize(d);
        mainPanel.add(backG);
         */
        
		//Adding panel with components to frame
		frame.add(mainPanel);
		frame.pack();//automatically sizes frame with all its contents to be at an appropriate size if frame.setSize is not used
	
	}
	
	public static void main(String[] args) { 
		new Main();
		
	}
	
}