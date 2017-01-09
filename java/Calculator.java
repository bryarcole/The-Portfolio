/*
Made by: Bryar Hamilton David Cole
For: Demostration
*/


class Calculator {
  public Calculator(){
    
  }
  
  //Add two ints
  public int add(int a, int b){
     return a + b;
  }
  
  //subtract two ints
  public int subtract (int a, int b){
    return b - a;
  }
  
  //multiply two ints
  public int multiply(int a, int b){
    return a * b;
  }

  //divide two ints but check if zero first
  public int divide(int a, int b){
    if( b == 0){
      System.out.println("Cannot divide by zero");
      return 0;
    }else {
      return a / b;
    }
  }

  //grab modulo but check if zero first
  public int modulo(int a, int b){
    if(b == 0){
      System.out.println("Cannot divide by zero");
      return 0;
    }else {
      return a % b;
    }
  }
  
  public static void main(String [] args){
    Calculator myCalculator = new Calculator();
    System.out.println(myCalculator.add(5, 7));
    System.out.println(myCalculator.subtract(12, 34));
    
  }
  
}