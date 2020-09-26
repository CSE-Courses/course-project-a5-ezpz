public class Main 
{
	private JFrame frame;
	private JFrame gameFr;
	private JPanel mainPanel;
	private JPanel mainPanel2;
	private JButton b1;
	private JButton b2;
	private JLabel gameLabel;
	
	gameFrame f = new gameFrame();
	
	public Main() {
		gui();	
	}
	
	public void gui() {
		
		//Creating frame
        JFrame.setDefaultLookAndFeelDecorated(true);
        frame = new JFrame("Version 1.0");
        gameFr = new JFrame("Version 1.0");
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
        
        
        
      //Creating Panel for game window
    	gameFr.add(f);
    	gameFr.setSize(800,600);
      	//mainPanel2 = new JPanel();
      	//mainPanel2.setBackground(Color.WHITE);//setting background of JPanel to be black 
        //BoxLayout boxlayout2 = new BoxLayout(mainPanel2, BoxLayout.Y_AXIS);//Setting Boxlayout for Jpanel
        //mainPanel2.setLayout(boxlayout2);//BoxLayout.Y_AXIS adds panel components from top to bottom 
        //Set border for the panel
        //mainPanel2.setBorder(new EmptyBorder(new Insets(150, 200, 150, 200)));
        //mainPanel.setBorder(new EmptyBorder(new Insets(50, 80, 50, 80)));     
        //gameFr.add(mainPanel2);
        //gameFr.pack();
            
        
        
        b1.addActionListener(new java.awt.event.ActionListener(){
            public void actionPerformed1(ActionEvent e){  
            		gameFr.setVisible(true);
               }

			@Override
			public void actionPerformed(ActionEvent e) {
				// TODO Auto-generated method stub
				gameFr.setVisible(true);
				
			}    
        });
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