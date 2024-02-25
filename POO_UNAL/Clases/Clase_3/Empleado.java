package POO_UNAL.Clases.Clase_3;

public class Empleado extends Estudiante {
    double sueldo;
    String empresa;

    public Empleado (int ID, String nombre, String apellido, String direccion, Double sueldo, String empresa){
        super(ID, nombre, apellido, direccion);
        this.ID = ID;
        this.nombre = nombre;
        this.apellido = apellido;
        this.direccion = direccion;
    }

    


}
