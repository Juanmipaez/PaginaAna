package Java_practice.People;

public class Student extends Person {
    double gpa;
    int grade;

    public Student(String name,String birthday, double gpa, int grade){
        super(name, birthday);
        this.name = name;
        this.birthday = birthday;
        this.gpa = gpa;
        this.grade = grade;
    }

    public int getgrade(){
        return grade;
    }

    public double getgpa(){
        return gpa;
    }
}
