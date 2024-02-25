package POO_UNAL.Clases.Clase_2;

public class Vehicle {
    String regNo;
    String make;
    int yearOfManufacture;
    double value;

    public Vehicle(String regNo, String make, int yearOfManufacture, double value){
        this.regNo = regNo;
        this.make = make;
        this.yearOfManufacture = yearOfManufacture;
        this.value = value;
    }

    public void getRegNo(){
        System.out.println(regNo);
    }

    public void getMake(){
        System.out.println(make);
    }

}

