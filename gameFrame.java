package GUI;

import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;


public class gameFrame extends JPanel implements ActionListener, KeyListener {
	
	Timer t = new Timer(5,this);
	double x = 0;
	double y = 0;
	double velx = 0;
	double vely = 0;
	
	public gameFrame() {
		t.start();
		addKeyListener(this);
		setFocusable(true);
		setFocusTraversalKeysEnabled(false);
		
	}
	
	public void paint(Graphics g) {
		super.paint(g);
		Graphics2D g2 = (Graphics2D) g;
		g2.fill(new Ellipse2D.Double(x,y,40,40));
	}
	
	public void actionPerformed(ActionEvent e) {
		repaint();
		x = x + velx;
		y = y + vely;
	}
	
	public void up() {
		velx = 0;
		vely = -1.5;
	}
	
	public void down() {
		velx = 0;
		vely = 1.5;
	}
	
	public void left() {
		velx = -1.5;
		vely = 0;
	}
	
	public void right() {
		velx = 1.5;
		vely = 0;
	}
	
	public void keyPressed(KeyEvent e) {
		int k = e.getKeyCode();
		if (k == KeyEvent.VK_W) {
			up(); 
		}
		if (k == KeyEvent.VK_A) {
			left(); 
		}
		if (k == KeyEvent.VK_S) {
			down(); 
		}
		if (k == KeyEvent.VK_D) {
			right(); 
		}
	}
	@Override
	public void keyTyped(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void keyReleased(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}


}
