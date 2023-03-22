public class Processador extends ItemDeCompra {
    public Processador(String descricao, double preco) {
    super(descricao, preco);
    }


    @Override
    public double getPrice() {
    return getPreco(); // o preço do processador é o seu preço próprio
    }
}
