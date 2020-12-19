package principal;

import java.util.Scanner;

import entidades.Aluguel;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		Aluguel[] reserva = new Aluguel[10];
		System.out.println("INFORME QUANTOS QUARTOS SERÃO ALUGADOS ; ");
		int q = sc.nextInt();
		sc.nextLine();
		
		for (int i = 0; i < q; i++) {
			System.out.println("INFORME O NOME DO CLIENTE : ");
			String nome = sc.nextLine();
			System.out.println("INFORME O NÚMERO DO QUARTO : ");
			int nquarto = sc.nextInt();
			sc.nextLine();
			System.out.println("INFORME O SEU E-MAIL : ");
			String email = sc.nextLine();
			
			reserva[nquarto] = new Aluguel(nome, nquarto, email);

		}		
		
		for (int i = 0; i < 10; i++) {
			if (reserva[i] != null) {
				System.out.println("QUARTO: "+ i +", "+ reserva[i]);
				
			}
		
		
		
		
		}
	}
}
		
		
 		
		
	


