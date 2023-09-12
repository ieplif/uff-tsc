public class Tecnico extends Empregado { // Uso de herança ao estender a classe "Empregado" e não cometer o erro de redeclarar os atributos herdados. 
    
public Tecnico(String nome, double salario, int anoDeContratacao) { 
        super(nome, salario, anoDeContratacao); 
    } 
 
    @Override 
    public void imprimirPaper() { // Polimorfismo 
        System.out.println("Eu sou técnico(a)."); 
    } 
}
    

