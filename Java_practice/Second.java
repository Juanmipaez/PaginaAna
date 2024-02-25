package Java_practice;

public class Second {

    String nombre, NumeroCuenta;
    double Saldo;

    public void Suma(int x, int y){
        System.out.println("Suma= "+(x+y));
    }

    public void AccountName(String name){
        System.out.println("The account's holder name is: "+name);
    }
    public static void main(String[] args) {
        Second Cuenta1 = new Second();
        Cuenta1.nombre="Juan";
        Cuenta1.NumeroCuenta = "101039902";
        Cuenta1.Saldo = 1200000;
        Cuenta1.AccountName("Daniel");
        System.out.println("The account's holder name is "+Cuenta1.nombre);
        Main obj = new Main();
        obj.speed(200);
        Cuenta1.Suma(4,5);
    }
}
