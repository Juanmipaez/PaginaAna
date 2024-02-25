package Java_practice;

public class Hello{

    public int addNumbers(int a, int b){
        return a+b;
    }

    public static void main(String[] args){
        int myAge = 19;
        int drinkingAge = 18;
        String name = "18.7";
        float name2 = Float.parseFloat(name);
        System.out.println(name2+1);

        int result = (myAge>=drinkingAge) ? drinkingAge+1 : drinkingAge-1 ;
        System.out.println(result);

        Hello obj = new Hello();
        int result2 = obj.addNumbers(myAge, drinkingAge);
        System.out.println(result2);


        String[][] cars = {{"Volvo","Honda","Jaguar","Mercedes"},{"Lamborgihni","Porsche"}};
        // for (String i:cars){
        //     System.out.println(i);
        // }
        for (int i=0; i<cars.length;i++){
            for (int j=0; j<cars[i].length;j++){
                System.out.println(cars[i][j]);
            }
        }
    }

}
