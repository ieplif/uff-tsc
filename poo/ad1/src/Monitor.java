public class Monitor extends ItemDeCompra {
    private double resolucaoPolegadas;
    
    public Monitor(String descricao, double resolucaoPolegadas, double preco) {
        super(descricao, preco);
        this.resolucaoPolegadas = resolucaoPolegadas;
    }
    
    public double getResolucaoPolegadas() {
        return resolucaoPolegadas;
    }
    
    @Override
    public double getPrice() {
        return getPreco(); // o preço do monitor é o seu preço próprio
    }
}        