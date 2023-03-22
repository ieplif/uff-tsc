
public abstract class ItemDeCompra {
    private String descricao;
    private double preco;
    
    
    public ItemDeCompra(String descricao, double preco) {
        this.descricao = descricao;
        this.preco = preco;
    }
    
    public String getDescricao() {
        return descricao;
    }
    
    public double getPreco() {
        return preco;
    }
    
    public abstract double getPrice(); // método abstrato para calcular o preço total do item
    
}

