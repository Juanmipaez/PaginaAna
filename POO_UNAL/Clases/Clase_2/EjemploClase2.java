package POO_UNAL.Clases.Clase_2;

public class EjemploClase2 {

    
    public static void main(String[] args) {
        Vehicle vehiculo1 = new Vehicle("kahqwgad","colombia",2022,65);
        vehiculo1.getRegNo();
        vehiculo1.getMake();
        SecondHandVehicle vehiculo2 = new SecondHandVehicle("alhakjsda","usa",2022,65,18);
        vehiculo2.getMake();
    }

}
