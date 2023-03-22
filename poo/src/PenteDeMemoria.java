public class PenteDeMemoria extends ItemDeCompra {
    private int capacidadeGb;

    public PenteDeMemoria(String descricao, int capacidadeGb, double preco) {
        super(descricao, preco);
        this.capacidadeGb = capacidadeGb;
    }
    
    public int getCapacidadeGb() {
        return capacidadeGb;
    }
    
    @Override
    public double getPrice() {
        return getPreco(); // o preço do pente de memória é o seu preço próprio
    }
}
    