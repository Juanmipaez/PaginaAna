package POO_UNAL.Taller_1;

public class Ejercicio_prop_12 {
    public static void main(String[] args) {
        double Horas,CostoPorHora,PorcentajeRetencion,SalarioBruto,SalarioNeto;
        Horas = 40;
        CostoPorHora = 5000;
        SalarioBruto = Horas*CostoPorHora;
        PorcentajeRetencion = (0.125*SalarioBruto);
        SalarioNeto = SalarioBruto-PorcentajeRetencion;
        System.out.println("Salario bruto: "+SalarioBruto);
        System.out.println("Retencion en la fuente: "+PorcentajeRetencion);
        System.out.println("Salario neto: "+SalarioNeto );
    }
}
