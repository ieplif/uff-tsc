import java.util.List;

public class Gabinete {
    private Processador processador;
    private List<PenteDeMemoria> pentesDeMemoria;

    public Gabinete(Processador processador, List<PenteDeMemoria> pentesDeMemoria) {
        this.processador = processador;
        this.pentesDeMemoria = pentesDeMemoria;
    }
    
    public Gabinete(String string) {
    }

    public Processador getProcessador() {
        return processador;
    }
    
    public List<PenteDeMemoria> getPentesDeMemoria() {
        return pentesDeMemoria;
    }
    
    public double getPrice() {
        double price = processador.getPreco();
        for (PenteDeMemoria pente : pentesDeMemoria) {
            price += pente.getPreco();
        }
        return price;
    }

    public void inclui(PenteDeMemoria mem1) {
    }

    public void inclui(Processador cpu1) {
    }
}
