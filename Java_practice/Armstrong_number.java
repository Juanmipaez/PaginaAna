package Java_practice;

public class Armstrong_number {
    public static void main(String[] args){
        int numero = 153;
        int num_length = (String.valueOf(numero).length()); //Cantidad de cifras del numero
        int suma=0;

        for(int i=0;i<num_length;i++){
            int numero_acortado = (int) Math.floor(numero/(Math.pow(10,i)));
            int ultimo_digito = numero_acortado%10;
            suma+= Math.pow(ultimo_digito, num_length);
        }
        if  (suma==numero){
            System.out.println("It is");
        }
        else{
            System.out.println("It's not");
        }
    }
}
