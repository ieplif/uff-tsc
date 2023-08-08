import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.Scanner;

class Time {
    String nome;
    int vitorias;
    int pontos;

    public Time(String nome, int vitorias, int pontos) {
        this.nome = nome;
        this.vitorias = vitorias;
        this.pontos = pontos;
    }

    public String getNome() {
        return nome;
    }

    public int getVitorias() {
        return vitorias;
    }

    public int getPontos() {
        return pontos;
    }

    @Override
    public String toString() {
        return nome;
    }
}

public class NBBRanking {
    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter file path: ");  // Exemplo: C:\TempEI4\arquivo.txt
        String arquivo = scanner.nextLine();

        System.out.print("Digite o valor de k: ");
        int k = scanner.nextInt();
        scanner.close();                                               
        List<Time> times = new ArrayList<>();

        try (BufferedReader br = new BufferedReader(new FileReader(arquivo))) {
            String linha;
            while ((linha = br.readLine()) != null) {
                String[] campos = linha.split("/");
                String nomeTime1 = campos[1].trim();
                String nomeTime2 = campos[2].trim();
                int placarTime1 = Integer.parseInt(campos[3].trim());
                int placarTime2 = Integer.parseInt(campos[4].trim());

                // Atualiza as informações dos times
                Time time1 = getTime(times, nomeTime1);
                Time time2 = getTime(times, nomeTime2);
                if (placarTime1 > placarTime2) {
                    time1.vitorias++;
                } else {
                    time2.vitorias++;
                }
                time1.pontos += placarTime1;
                time2.pontos += placarTime2;
            }
        } catch (IOException e) {
            System.out.println("Erro ao ler o arquivo: " + e.getMessage());
            System.exit(1);
        }

        // Ordena os times com base no número de vitórias e pontos
        Collections.sort(times, Comparator.comparing(Time::getVitorias).reversed()
                .thenComparing(Time::getPontos).reversed().thenComparing(Time::getNome));

        // Exibe os primeiros k times
        System.out.println("Os primeiros " + k + " times do NBB são:");
        for (int i = 0; i < k; i++) {
            if (i < times.size()) {
                System.out.println((i + 1) + ". " + times.get(i));
            }
        }
    }

    private static Time getTime(List<Time> times, String nome) {
        for (Time time : times) {
            if (time.getNome().equals(nome)) {
                return time;
            }
        }
        Time novoTime = new Time(nome, 0, 0);
        times.add(novoTime);
        return novoTime;
    }
}
