package Java_practice;
import java.util.Scanner;


public class Main2 {
    public static void suma(double x, double y){
        System.out.println(x+y);
    }
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("Ingrese numero 1: ");
        double numero1 = entrada.nextDouble();
        System.out.print("Ingrese numero 2: ");
        double numero2 = entrada.nextDouble();

        suma(numero1,numero2);
    }
}