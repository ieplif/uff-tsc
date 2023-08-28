public class Phase {
    
    Card tasks[];
    private int numTasks = 0;

    public Phase() {
        tasks = new Card [100];
    }

    public void add(Card c) {
        tasks[numTasks] = c;
        numTasks++;
    }

    public void remove(Card c) {
        boolean find = false;
        for (int i=0; i<numTasks; i++) {
            if ((find) || (tasks[i] == c)) {
                tasks[i] = tasks[i+1];
                find = true;
            }
        }
        if (find) {
            numTasks--;
        }
    }

    public String toString() {

        String out = "";
        for (int i=0; i<numTasks; i++) {
            out += tasks[i].toString();
        }
        return out;
    }
}
