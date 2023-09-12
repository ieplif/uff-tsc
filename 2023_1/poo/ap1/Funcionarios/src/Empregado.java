    public abstract class Empregado { // Abstração
    private String nome;    // Uso de encapsulamento ao declarar o atributos como privado e
    private double salario; // mantê-los apenas por métodos desta classe.
    private int anoDeContratacao;
    public Empregado(String nome, double salario, int anoDeContratacao) {
        this.nome = nome;
        this.salario = salario;
        this.anoDeContratacao = anoDeContratacao;
}
    public String getNome() {
        return this.nome;
}
    public double getSalario() {
        return this.salario;
}
    public int getAnoDeContratacao() {
        return this.anoDeContratacao;
}
    public void aumentarSalario(double percentual) {
        this.salario += this.salario * percentual / 100;
}
    public abstract void imprimirPaper(); // Abstração
}
 