/*
Made by: Bryar Hamilton David Cole
For: Demostration
*/

import java.util.ArrayList;
//Showing use of ArrayList object in Java
class GradeAnalyzer {
  public GradeAnalyzer(){
    //empty constructor
  }
  public int getAverage (ArrayList<Integer> grades){
      //Check to see if grades array is empty
    if (grades.size() < 1){
      System.out.println("The list is empty! Fill it up.");
      return 0;
    }else {
        //Sum of grades
      int sum = 0;
      for(Integer grade : grades){
        sum = grade + sum;
      }
      //Average of grades
      int average = sum / grades.size();
      System.out.println(average);
      return average;
    }
  }
  
  public static void main(String[] arg){
      //Create ArrayList object 
    ArrayList<Integer> myClassRoom = new ArrayList<Integer>();
    //Add grades
    myClassRoom.add(98);
    myClassRoom.add(92);
    myClassRoom.add(88);
    myClassRoom.add(75);
    myClassRoom.add(61);
    myClassRoom.add(89);
    myClassRoom.add(95);
    
    //Create GradeAnalyzer object
    GradeAnalyzer myAnalyzer = new GradeAnalyzer();
    
    //Pass the myClassRoom array into the getAverage method from the GradeAnalyzer class, via an object named myAnalyzer.
    myAnalyzer.getAverage(myClassRoom);
  }
}