public class Teclado extends ItemDeCompra {
    public Teclado(String descricao, double preco) {
    super(descricao, preco);
    }

    @Override
    public double getPrice() {
    return getPreco(); // o preço do teclado é o seu preço próprio
    }
}

