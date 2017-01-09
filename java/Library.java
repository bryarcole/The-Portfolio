/*
Made by: Bryar Hamilton David Cole
For: Demostration
*/

import java.util.HashMap;
/*
Showing use of the HashMap object in Java
*/
public class Library {
  public Library(){
    //Empty constructor 
  }
  
  //Retrive books that have a 'true' value
  public void getFinishedBooks(HashMap<String, Boolean> library){
      //check to see if library is empty
    if(library.size() < 1){ 
        
      System.out.println("The library is empty");
    }else{
        //Print out finished books
      for (String book: library.keySet()){
        if (library.get(book) == true){
          System.out.println(book);
        }
      }
    }
  }

	public static void main(String[] arg){
    //Create HashMap object
    HashMap<String, Boolean> myBooks = new HashMap<String, Boolean>();
    
    //Add properties to the library
    myBooks.put("Road Down The Funnel", true);
    myBooks.put("Rat: A biology", false);
    myBooks.put("TimeIn", true);
    myBooks.put("3D Food Printing", false);
    
    //Create Library object from the Library class
    Library library = new Library();
    //Pass the HashMap into the getFinishedBooks method from the Library class
    library.getFinishedBooks(myBooks);
  }
}