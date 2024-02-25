package Java_practice.People;


public class PersonTester {
    public static void main(String[] args) {
        Student estudiante1 = new Student("Juan", "12/02/2003", 4.54, 12);
        System.out.println("Student's name: "+estudiante1.getname());
        System.out.println("Student's grade: "+estudiante1.getgrade());
    
    }
}
