package POO_UNAL.Taller_1;

public class Ejercicio_resuelto_5 {
    public static void main(String[] args) {
        double suma=0; double x,y;
        x=20;
        y=40;
        suma+=x;
        x+=Math.pow(y,2);
        suma+=(x/y);
        System.out.println("El valor de la suma es: "+suma);
    }
}
