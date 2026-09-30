package com.project.java;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class file  {
	private File myFile;
	String o;
	String[] array;
	List<String> col1 = new ArrayList<>(); //column arrays
	List<String> col2 = new ArrayList<>();
	List<Integer> col3 = new ArrayList<>();
	List<Integer> col4 = new ArrayList<>();
	List<Integer> col5 = new ArrayList<>();
	List<String> col6 = new ArrayList<>();
	List<String> col7 = new ArrayList<>();
	List<String> out = new ArrayList<>();
	
	file(String title)
	{
	 myFile = new File("CK.txt"); 
	}
	
	
	public String readFile() {
		
	
	try (Scanner myScanner = new Scanner(myFile)) {
		
		while (myScanner.hasNextLine())
		{
			
			String text = myScanner.nextLine();
			o = text;
			
		}
		
	} catch (FileNotFoundException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
		
	}
	return o;
	}
	
	
	
	public String[] nextLine() throws IOException//read file to array
	{
	
		List<String> listoflines = new ArrayList<String>();
		listoflines = Files.readAllLines(Paths.get("CK.txt"));
		String[] array = listoflines.toArray(new String[0]);
		

	return array;
	}
	
	public String[] co1() throws IOException //return column1 as array
	{
	
		
		
		String[] array = col1.toArray(new String[0]);
		

	return array;
	}
	
	public String[] co2() throws IOException
	{
	
		
		
		String[] array = col2.toArray(new String[0]);
		

	return array;
	}
	
	public Integer[] co3() throws IOException //return column 3 as integer array
	{
	
		
		Integer[] array = col3.toArray(new Integer[0]);
		

	return array;
	}
	
	public Integer[] co4() throws IOException
	{
	
		
		Integer[] array = col4.toArray(new Integer[0]);
		

	return array;
	}
	
	
	public Integer[] co5() throws IOException
	{
	
		
		Integer[] array = col5.toArray(new Integer[0]);
		

	return array;
	}
	
	
	public String[] co6() throws IOException
	{
	
		
		String[] array = col6.toArray(new String[0]);
		

	return array;
	}
	
	public String[] co7() throws IOException
	{
	
		
		String[] array = col7.toArray(new String[0]);
		

	return array;
	}
	
	
	public void writeFile(String line)
	{
	try (PrintWriter myOutFile = new PrintWriter(new FileWriter("CK.txt", true)))
	{
		
		
		myOutFile.println(line);
		myOutFile.close();
		
	} catch (FileNotFoundException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
		System.out.println("Error");
	} catch (IOException e1) {
		// TODO Auto-generated catch block
		e1.printStackTrace();
	}
	
	}
		
	
	

	public int lines()
	{ int i = 0;
	try(Scanner myScanner = new Scanner(myFile)) {
		while (myScanner.hasNextLine())
		{
			i++;
		}
		
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
	}
	return i;
	}
	
	public void columns() //split rows into column arrays
	{ 
		col1.clear(); //clear columns in case file is edited
	    col2.clear();
	    col3.clear();
	    col4.clear();
	    col5.clear();
	    col6.clear(); 
	    col7.clear();
	try(Scanner myScanner = new Scanner(myFile)) {
		
		while (myScanner.hasNextLine())
		{
			String text = myScanner.nextLine();
			
			myScanner.useDelimiter("\\s+"); // seperate using spaces
			
			
			while (myScanner.hasNext()) {
				
			    col1.add(myScanner.next());
			    col2.add(myScanner.next());
			    col3.add(myScanner.nextInt());
			    col4.add(myScanner.nextInt());
			    col5.add(myScanner.nextInt());
			    col6.add(myScanner.next()); 
			    col7.add(myScanner.next());
			    
			}
			    
			 
			myScanner.nextLine();
			
		}
		
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
		
	}
	
	
	}
	
	
	public String fil(int inp) //filter to one line
	{
	    int i = inp;
	    int j = 1;

	    String line = null;

	    // Read the line you want
	    try (Scanner scanner = new Scanner(myFile)) {

	        while (scanner.hasNextLine()) {
	            

	            if (j == i) {
	            	line = scanner.nextLine();
	            }
	            else {
	            	scanner.nextLine();
	            }
	            
	            j++;
	        
	            
	        }

	    } catch (FileNotFoundException e) {
	        e.printStackTrace();
	        
	    }
		return line;
	}
	
	public String search1(String term)
	{
		
        int j = 0;
     
      //search for number of occurences of term
       
        
		try (Scanner myScanner = new Scanner(myFile)) {
            
            

            while ((myScanner.hasNext())) {
            	String line = myScanner.next();
                if (line.contains(term)) {
                	
                   
                 
                    j++;
                }
                
                 
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
		return String.valueOf(j);
    }
	
	public String search(String term)
	{
		int i = 1;
        
        List<String> out = new ArrayList<>();
       // Search for lines search occurs on;
       
        
		try (Scanner myScanner = new Scanner(myFile)) {
            
            

            while ((myScanner.hasNextLine())) {
            	String line = myScanner.nextLine();
                if (line.contains(term)) {
                	
                  // System.out.println("Found at line " + i + ": " + line);
                    out.add("Found at line " + i + ": " + line);
                  
                   
                }
                
                i++;  
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
		return String.join("\n", out);
    }
		
		
	
	
	public int avg3() //calculate average for column 3
	{ 
	int j = 0;
		
	for(int num : col3)
	{
		j  += num;
	}
	j = j/ col3.size();
	//System.out.print(j);
	return j;
	}
	
	
	public int avg4()
	{ 
	int j = 0;
		
	for(int num : col4)
	{
		j  += num;
	}
	j = j/ col4.size();
	
	return j;
	}
	
	public int avg5()
	{ 
	int j = 0;
		
	for(int num : col5)
	{
		j  += num;
	}
	j = j/ col5.size();
	
	return j;
	}
	
	public String liness() //return no of lines value as string
	{ int i = 0;
	try(Scanner myScanner = new Scanner(myFile)) {
		while (myScanner.hasNextLine())
		{
			i++;
			myScanner.nextLine();
			
		}
		
	} catch (IOException e) {
		// TODO Auto-generated catch block
		e.printStackTrace();
		return String.valueOf(i);
	}
	return String.valueOf(i);
	}
	
	
	public void del(int inp) //choose line to delete and rewrite file without that line
	{
	    int i = inp;
	    int j = 1;

	    List<String> newLines = new ArrayList<>();

	    // Read all lines except the one to delete
	    try (Scanner scanner = new Scanner(myFile)) {

	        while (scanner.hasNextLine()) {
	            String line = scanner.nextLine();

	            if (j != i) {
	                newLines.add(line);
	            }

	            j++;
	        }

	    } catch (FileNotFoundException e) {
	        e.printStackTrace();
	        return;
	    }

	    // Rewrite the file
	    try (PrintWriter writer = new PrintWriter(new FileWriter("CK.txt", false))) {

	        for (String line : newLines) {
	            writer.println(line);
	        }

	    } catch (IOException e) {
	        e.printStackTrace();
	    }
	}
	
	
	}


