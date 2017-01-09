/*
Made by: Bryar Hamilton David Cole
For: Demostration
*/

//Create a Droid class with multiple methods
public class Droid {
  int batteryLevel;
  
  public Droid(){
    batteryLevel = 100;
    //On createion the Droid object will have a prop called "batteryLevel" set to 100
  }
  
  //First Method
  public void activate(){
    System.out.println("I'm up, how may I help?");
    //Deduct 5 from batteryLevel
    batteryLevel = batteryLevel - 5;
    System.out.println("Batter level is now: " + batteryLevel + " percent.");
  }

  //Second Method
  public void chargeBattery(int hours) {
     System.out.println("Droid charging...");
     //Use hours as the number that will be used to determine how much to recharge the batteryLevel
     batteryLevel = batteryLevel + hours;
     //If the batter level is over 100 just set it to 100
     if(batteryLevel < 100){
       batteryLevel = 100;
       System.out.println("Battery level is " + batteryLevel +"%");
     }else {
         //If the battery level is less that 100, it will be set to whatever number in batteryLevel
       System.out.println("Batter level is " + batteryLevel + "%");
     }
   }
  

  //Third method - print out Battery level (return an INT)
  public int checkBatteryLevel(){
    System.out.println("Battery level is " + batteryLevel + "%");
    return batteryLevel;	
  }
  
  //Forth Method 
  public void hover(int feet){
      //check to see if number passed into is greater than 2
    if(feet > 2){
      System.out.println("Error, cannot hover above 2 feet");
    }else{
        //Deduct batter life, show hovering
      System.out.println("Hovering....");
      batteryLevel = batteryLevel - 20;
      System.out.println("Batter level is " + batteryLevel + "%");
    }
  }
  
  //Main 
  public static void main(String [] args){
    Droid botty = new Droid();
    botty.activate();
    botty.chargeBattery(5);
    botty.hover(2);
  }
}