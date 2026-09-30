package com.project.java;

import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;
import javax.swing.ScrollPaneConstants;

public class gui2 extends JFrame implements ActionListener, MouseListener {

	file f1 = new file("CK.txt");
	JButton button1, button2, button3, button4, button5, button6, button7,button8, button9;
	JPanel panel1, panel2, panel3;
	JLabel label1;
	JTextField field1, fiel;
	JTextArea area1,  field2;
	JScrollPane scroll;
	
	
	
	
	gui2(String title) {
		super(title);
		setSize(600,300);
		setLayout(new FlowLayout());
		field1 = new JTextField("Search");
		fiel = new JTextField("Enter Row");
		button1 = new JButton("Search");
		button2 = new JButton("Id");
		button3 = new JButton("Workout");
		button4 = new JButton("Duration");
		button5 = new JButton("Heart-Rate");
		button6 = new JButton("Calories");
		button7 = new JButton("Intensity");
		button8 = new JButton("Day");
		button9 = new JButton("Search Row");
		area1 = new JTextArea();
		area1.setEditable(false);
		field2 = new JTextArea();
		field2.setEditable(false);
		
		area1.setRows(10);
		area1.setColumns(30);
		JScrollPane scroll = new JScrollPane(area1);
		scroll.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
		field1.addActionListener(this);
		fiel.addActionListener(this);
		button1.addActionListener(this);
		button2.addActionListener(this);
		button3.addActionListener(this);
		button4.addActionListener(this);
		button5.addActionListener(this);
		button6.addActionListener(this);
		button7.addActionListener(this);
		button8.addActionListener(this);
		button9.addActionListener(this);
		panel1  = new JPanel();
		panel1.add(field1);
		//panel1.add(field2);
		panel1.add(scroll);
		panel1.add(button1);
		panel1.setBackground(new Color(13, 27, 33));
		
		
		add(panel1);
		
		panel2 = new JPanel();
		panel2.add(button2);
		panel2.add(button3);
		panel2.add(button4);
		panel2.add(button5);
		panel2.add(button6);
		panel2.add(button7);
		panel2.add(button8);
		panel2.setBackground(new Color(13, 27, 33));
		
		add(panel2);
		
		panel3 = new JPanel();
		panel3.add(fiel);
		panel3.add(button9);
		
		add(panel3);
		
		
		// TODO Auto-generated constructor stub
		getContentPane().setBackground(new Color(13, 27, 33));
		setResizable(false);
		  setVisible(true);
	}
	

	@Override
	public void mouseClicked(MouseEvent e) {
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
	public void mouseEntered(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void mouseExited(MouseEvent e) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		if(e.getSource() == button1)//search for occurencess of word
		{
			
			
			
			panel1.add(field2);
			String res = field1.getText();
			String result =(f1.search(res));
			area1.setText(result);
			String rese =(f1.search1(res));
			area1.append("\n"+ res +" occurs " + rese +" times" );
			field2.setText("");
			field2.append(res +" occurs " + rese +" times");
			panel1.add(field2);
			
			
			
		}
		
		if(e.getSource() == button2) //display column
		{
			f1.columns();
			area1.setText("");
			try {
	            String[] lines = f1.co1();

	            for (String line : lines) {
	                area1.append(line + "\n");
	            }

	        } catch (IOException e1) {
	            area1.setText("Error reading file.");
	        }
		}
		if(e.getSource() == button3)
		{
			f1.columns();
			area1.setText("");
			try {
	            String[] lines = f1.co2();

	            for (String line : lines) {
	                area1.append(line + "\n");
	            }

	        } catch (IOException e1) {
	            area1.setText("Error reading file.");
	        }
		}
		if(e.getSource() == button4)
		{
			f1.columns();
			area1.setText("");
			try {
	            Integer[] lines = f1.co3();

	            for (int line : lines) {
	                area1.append(line + "\n");
	            }

	        } catch (IOException e1) {
	            area1.setText("Error reading file.");
	        }
		}
		if(e.getSource() == button5)
		{
			f1.columns();
			area1.setText("");
			try {
	            Integer[] lines = f1.co4();

	            for (int line : lines) {
	                area1.append(line + "\n");
	            }

	        } catch (IOException e1) {
	            area1.setText("Error reading file.");
	        }
		}
		if(e.getSource() == button6)
		{
			f1.columns();
			area1.setText("");
			try {
	            Integer[] lines = f1.co5();

	            for (int line : lines) {
	                area1.append(line + "\n");
	            }

	        } catch (IOException e1) {
	            area1.setText("Error reading file.");
	        }
		}
		if(e.getSource() == button7)
		{
			f1.columns();
			area1.setText("");
			try {
	            String[] lines = f1.co6();

	            for (String line : lines) {
	                area1.append(line + "\n");
	            }

	        } catch (IOException e1) {
	            area1.setText("Error reading file.");
	        }
		}
		if(e.getSource() == button8)
		{
			f1.columns();
			area1.setText("");
			try {
	            String[] lines = f1.co7();

	            for (String line : lines) {
	                area1.append(line + "\n");
	            }

	        } catch (IOException e1) {
	            area1.setText("Error reading file.");
	        }
		}
		
		if(e.getSource() == button9) //show line searched for
		{
			
			area1.setText("");
			int d = Integer.parseInt(fiel.getText());
			String line =f1.fil(d);
			area1.append(line);
		}

}}
