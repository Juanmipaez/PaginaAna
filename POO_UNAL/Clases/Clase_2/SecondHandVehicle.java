package POO_UNAL.Clases.Clase_2;

public class SecondHandVehicle extends Vehicle {
    int numberOfOwners;

    public SecondHandVehicle(String regNo, String make, int yearOfManufacture, double value, int numberOfOwners){
        super(regNo, make, yearOfManufacture, value);
        this.regNo = regNo;
        this.make = make;
        this.yearOfManufacture = yearOfManufacture;
        this.value = value;
        this.numberOfOwners = numberOfOwners;
    }
}

