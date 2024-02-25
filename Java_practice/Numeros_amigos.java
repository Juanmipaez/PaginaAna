package Java_practice;
import java.util.Scanner;
public class Numeros_amigos {
    public static void main(String[] args){
        try (Scanner Entrada = new Scanner(System.in)) {
            System.out.print("Ingrese primer numero: ");
            int Numero1 = Entrada.nextInt();
            System.out.print("Ingrese segundo numero: ");
            int Numero2 = Entrada.nextInt();
            int Suma_digitos_num1 = 0;
            int Suma_digitos_num2 = 0;


            for (int i=1;i<=(Numero1/2);i++){
                if ( (Numero1%i) == 0 ){
                    Suma_digitos_num1+=i;
                }
            }

            for (int i=1;i<=(Numero2/2);i++){
                if ( (Numero2%i) == 0 ){
                    Suma_digitos_num2+=i;
                }
            }

            if (Suma_digitos_num1==Numero2 & Suma_digitos_num2==Numero1){
                System.out.println("They're friends");
            }
            else{
                System.out.println("They're not");
            }
        }
    }
}
