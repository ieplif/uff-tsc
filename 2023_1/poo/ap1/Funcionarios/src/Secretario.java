public class Secretario extends Empregado {
    
    public Secretario(String nome, double salario, int anoDeContratacao) { 
        super(nome, salario, anoDeContratacao); 
    } 
 
    @Override 
    public void imprimirPaper() { // Polimorfismo 
        System.out.println("Eu sou secretário(a)."); 
    } 
} 
 
