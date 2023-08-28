public class Card {
    
    int id;
    String task;

    private static int numCards = 0;

    public Card(String text) {
        this.task = text;
        id = numCards;
        numCards++;
    }

    public String toString() {
        return id + "" + task + "\n";
    }
}
