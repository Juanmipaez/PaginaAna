package Java_practice;
import java.util.ArrayList;
public class Perfect_number {
    public static void main(String[] args){
        ArrayList<Integer> Numlist = new ArrayList<>();
        int Numero_original = 535;
        int Suma_digitos = 0;

        for (int i=1;i<(Numero_original/2)+1;i++){
            if ( (Numero_original%i) == 0 ){
                Suma_digitos+=i;
                Numlist.add(i);
            }
        }
        if (Suma_digitos==Numero_original){
            System.out.println("It is");
        }
        else{
            System.out.println("It's not");
        }
        for (int i:Numlist){
            System.out.println(i);
        }
        System.out.println(Numlist);
    }
}
