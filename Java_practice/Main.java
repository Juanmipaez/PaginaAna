package Java_practice;

public class Main {
    
    public void FullThottle(){
        System.out.println("The car is going at its max speed");
    }
    public void speed(int Maxspeed){
        System.out.println("The car's max speed is "+Maxspeed);
    }

    public static void main(String[] args) {
        Main MyCar = new Main();
        MyCar.FullThottle();
        MyCar.speed(250);
    }
}
