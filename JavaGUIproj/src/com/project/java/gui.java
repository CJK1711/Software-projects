package com.project.java;

import java.awt.Color;

import java.awt.FlowLayout;
import java.awt.GridBagConstraints;
import java.awt.GridBagLayout;
import java.awt.GridLayout;
import java.awt.TextField;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.IOException;
import java.util.ArrayList;

import javax.swing.Box;
import javax.swing.BoxLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextField;
import javax.swing.ScrollPaneConstants;

import java.util.Scanner;



import javax.swing.JTextArea;



public class gui extends JFrame implements ActionListener, MouseListener {
	JButton button1, button2, button3;
	JPanel panel1, panel2, panel3, panel4, panel5;
	JLabel label1;
	JTextField field1,field2, field3, field4, field5, field6;
	
	JTextArea area1;
	JScrollPane scroll;
	JFrame frame;
	int i = 0;
	
	file f1 = new file("CK.txt");
	String numy = f1.liness();
	
	
	ArrayList<file> file = new ArrayList<file>();
	
	gui(String title){
		
		super(title);  // calling/ running the constructor for JFrame (the class this class is inheriting from)
		setSize(600,350);
		 
		f1.columns();
		setLayout(new GridBagLayout());//Layout Gridbag
		setBackground(Color.DARK_GRAY);
		GridBagConstraints c = new GridBagConstraints();
		c.fill = GridBagConstraints.HORIZONTAL;
		field1 = new JTextField("Statistics, No of lines: " + f1.liness());
		field3 = new JTextField("Average Duration: " + f1.avg3());
		field4 = new JTextField("Average Heartrate: " + f1.avg4());
		field5 = new JTextField("Average Calories: " + f1.avg5());
		field6 = new JTextField("Enter new line");
		button1 = new JButton("Save New line");
		button2 = new JButton("Search");
		button2.setBackground(Color.WHITE);
		button3 = new JButton("Delete");
		field2= new JTextField("Enter line to delete");
		
		
		area1 = new JTextArea();
		
		
		   try {
	            String[] lines = f1.nextLine();

	            for (String line : lines) {
	                area1.append(line + "\n");
	            }

	        } catch (IOException e) {
	            area1.setText("Error reading file.");
	        }
		area1.setEditable(false);
		
		area1.setRows(10);
		JScrollPane scroll = new JScrollPane(area1);
		scroll.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
		
		button1.addActionListener(this);
		button2.addActionListener(this);
		button2.addMouseListener(this);
		button3.addActionListener(this);
		field1.addActionListener(this);
		field2.addActionListener(this);
		field3.addActionListener(this);
		field6.addActionListener(this);
		
	
		
		
		panel1  = new JPanel();
		

		 // that "add" method is from the JPanel class , which we know cos it's called against a jpanel object
		
		panel1.add(field2);
		panel1.add(field1);
		
		panel1.add(field3);
		panel1.add(field4);
		panel1.add(field5);
		panel1.setBounds(300,20,500,100);
		panel1.setBackground(Color.RED);
		c.fill = GridBagConstraints.HORIZONTAL; //positioning in GridBagLayout
		c.gridx = 1;
		c.gridy = 0;
		c.weightx = 0.5;
		c.weighty = 0.5;
	
		
	    
		add(panel1, c);  // add the panel to the screen (i.e. the jframe);
		
		add(Box.createVerticalStrut(5));
		
		panel2 = new JPanel();
		
		
		panel2.add(scroll);
		
		
		
		panel2.add(button1); 
		panel2.setBackground(Color.DARK_GRAY);
		
		
		c.fill = GridBagConstraints.HORIZONTAL;
		c.gridx = 1;
		c.gridy = 1;
		c.weightx = 0.5;
		
		c.ipady = 120;
		
		add(panel2, c);
		
		
		panel3 = new JPanel();
	     panel3.add(field6);
	     panel3.add(button1);
	     panel3.add(field2);
	     panel3.add(button3);
	     panel3.setBackground(Color.DARK_GRAY);
	     c.fill = GridBagConstraints.HORIZONTAL;
			c.gridx = 1;
			c.gridy = 2;
			c.weightx = 0.5;
			
			c.ipady = 10;
	     add(panel3, c);
	     
	     
			
			
			panel4 = new JPanel();

			panel4.add(button2);
			panel4.setBackground(Color.DARK_GRAY);
		     c.gridx = 1;
		     c.gridy = 3;
		     c.weightx = 0.5;
		   
		     c.ipady = 10;
		     add(panel4, c);
	     
		     panel5 = new JPanel();
		     panel5.setBackground(Color.BLACK);	
			     c.gridx = 1;
			     c.gridy = 4;
			     c.weightx = 0.5;
			     c.weighty = 30;
			     c.ipady = 100;
			     add(panel5, c);
		     
	     
		getContentPane().setBackground(Color.DARK_GRAY);
		setResizable(false);//can't change display size
	     setVisible(true); //without this, the screen defaults to not visible
	     
	     
	}
	

	public String newl() {
		
		String line = field6.getText();
		return line;
		
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource() == button1) //write new line
		{
			String line = field6.getText();
			if( (!line.equals("Enter new line") ) && (!line.equals(""))) //not allow blanks
			{
			f1.writeFile(line);
			area1.append(line + "\n");
			f1.columns();
			field1.setText("Statistics, No of lines: " + f1.liness());
			field3.setText("Average Duration: " + f1.avg3());
			field4.setText("Average Heartrate: " + f1.avg4());
			field5.setText("Average Calories: " + f1.avg5());
			}
			
			
		}
		if(e.getSource() == button2)
		{
			gui2 g2 = new gui2 ("Search/Filter"); //run second gui
			
			
		}
		if(e.getSource() == button3) //delete line
		{
			int d = Integer.parseInt(field2.getText()); //get line to delete
			if (d!=0) //not allow 0
			{
			f1.del(d);
			area1.setText("");
			f1.columns();
			try {
	            String[] lines = f1.nextLine();

	            for (String line : lines) {
	                area1.append(line + "\n");
	            }

	        } catch (IOException e1) {
	            area1.setText("Error reading file.");
	        }
			field1.setText("Statistics, No of lines: " + f1.liness());
			field3.setText("Average Duration: " + f1.avg3());
			field4.setText("Average Heartrate: " + f1.avg4());
			field5.setText("Average Calories: " + f1.avg5());
			}
			
		}
		
		
		
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mousePressed(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseReleased(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseEntered(MouseEvent e) { //change search button colour when hovered over
		// TODO Auto-generated method stub
		if(e.getSource() == button2)
		{
		button2.setBackground(Color.CYAN);
		
		}
	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		if(e.getSource() == button2)
		{
		button2.setBackground(Color.WHITE);
		button2.setText("Search");
		}
	}



	@Override
	public void mouseClicked(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

}
