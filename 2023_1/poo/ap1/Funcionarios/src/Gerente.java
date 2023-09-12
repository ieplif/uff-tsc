import java.util.ArrayList;

public class Gerente extends Empregado {
    
    private Secretario secretario; // Uso de encapsulamento ao declarar o atributos como privado e mantê-los apenas por métodos desta classe. 
    private ArrayList<Tecnico> tecnicos = new ArrayList<Tecnico>(); 
 
    public Gerente(String nome, double salario, int anoDeContratacao, Secretario secretario) { 
        super(nome, salario, anoDeContratacao); 
        this.secretario = secretario; 
    } 
 
    public void aumentarSalarioEmpregados(double percentual) { 
        if (secretario != null) { 
            secretario.aumentarSalario(percentual); 
        } 
        for (Tecnico tecnico: tecnicos) { 
            tecnico.aumentarSalario(percentual) 
        } 
 
        public void addTecnico(Tecnico tecnico) { 
            this.tecnicos.add(tecnico); 
        } 
    } 
 
    @Override 
    public void imprimirPaper() { // Polimorfismo 
        System.out.printl("Eu sou gerente e tenho %s como secretário(a) e mais %d técnicos(as) sob meu comando.", this.secretario.getNome(), this.tecnicos.size()); 
    } 
} 

