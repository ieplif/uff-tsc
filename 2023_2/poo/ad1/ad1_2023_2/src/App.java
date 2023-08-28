public class App {
    public static void main(String[] args) throws Exception {

        Board semestre2023_2 = new Board();
        Card fazerAD1 = new Card("Fazer a AD1");
        semestre2023_2.add(fazerAD1);
        Card fazerAD2 = new Card("Fazer a AD2");
        semestre2023_2.add(fazerAD2);
        System.out.println(semestre2023_2);
        semestre2023_2.prepare(fazerAD1);
        System.out.println(semestre2023_2);
        semestre2023_2.start(fazerAD1);
        System.out.println(semestre2023_2);
        semestre2023_2.finish(fazerAD1);
        System.out.println(semestre2023_2);
        
    }
}
