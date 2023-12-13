import java.util.Calendar;

public class Jogador {
    private String nome;
    private String posicao;
    private Calendar nascimento;
    private String nacionalidade;
    private int altura;
    private int peso;

    public Jogador(String nome, String posicao, Calendar nascimento, String nacionalidade, int altura, int peso) {
        this.nome = nome;
        this.posicao = posicao;
        this.nascimento = nascimento;
        this.nacionalidade = nacionalidade;
        this.altura = altura;
        this.peso = peso;
    }

    public String getNome() {
        return nome;
    }

    public String getPosicao() {
        return posicao;
    }

    public Calendar getNascimento() {
        return nascimento;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }

    public int getAltura() {
        return altura;
    }

    public int getPeso() {
        return peso;
    }

    public void setNome(String v) {
        nome = v;
    }

    public void setPosicao(String v) {
        posicao = v;
    }

    public void setNascimento(Calendar v) {
        nascimento = v;
    }

    public String setNacionalidade() {
        return nacionalidade;
    }

    public void setAltura(int v) {
        altura = v;
    }

    public void setPeso(int v) {
        peso = v;
    }

    public void imprimir() {
        System.out.println("Nome: " + nome + ", Posição: " + posicao + ", Datade Nascimento: " + nascimento + ", Nacionalidade: " + nacionalidade + ", Altura: " + altura + ", Peso: " + peso);
        }

    public int getIdade() {
        // Existem várias formas de cálculo, com ou sem o uso da API.
        Calendar today = Calendar.getInstance();
        return today.get(Calendar.YEAR) - nascimento.get(Calendar.YEAR);
    }

    public int getTempoParaAposentar() {
        switch (posicao.toLowerCase()) {
            case "defesa":
                return 40 - getIdade();
            case "meio-campo":
                return 38 - getIdade();
            case "ataque":
                return 35 - getIdade();
            default:
                throw new RuntimeException();
            // Na prova, não precisava levantar uma exceçã.
        }
    }
}