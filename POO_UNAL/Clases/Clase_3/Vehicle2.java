package POO_UNAL.Clases.Clase_3;

class Vehicle2 {
  protected String brand = "Ford";        // Vehicle attribute
  public void honk() {                    // Vehicle method
    System.out.println("Tuut, tuut!");
  }
}

class Car2 extends Vehicle2 {
    private String modelName = "Mustang"; 
    
       // Car attribute
public static void main(String[] args) {

      // Create a myCar object
    Car2 myCar = new Car2();

      // Call the honk() method (from the Vehicle class) on the myCar object
    myCar.honk();

      // Display the value of the brand attribute (from the Vehicle class) and the value of the modelName from the Car class
    System.out.println(myCar.brand + " " + myCar.modelName);
    }
}
