

public class Board {
    static int BACKLOG = 0;
    static int TODO = 1;
    static int DOING = 2;
    static int DONE = 3;
    String labels[] = {"BACKLOG", "TODO", "DOING", "DONE"};
    Phase phase[]= new Phase[4];

    public Board() {

        for (int i=0; i<4; i++) {
            phase[i] = new Phase();
        }
    }

    public void add(Card c) {
        phase[BACKLOG].add(c);
    }

    public void prepare(Card c) {
        phase[BACKLOG].remove(c);
        phase[TODO].add(c);
    }

    public void start(Card c) {
        phase[TODO].remove(c);
        phase[DOING].add(c);
    }

    public void finish(Card c) {
        phase[DOING].remove(c);
        phase[DONE].add(c);
    }

    public String toString() {
        String out = "";
        for (int i=0; i<4; i++) {
            out += labels[i] + "\n" + phase[i].toString() + "\n";
        }
        return out;
    }
}

