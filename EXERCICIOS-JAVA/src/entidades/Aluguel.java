package entidades;

public class Aluguel {

	private String nome;
	private int nquarto;
	private String email;
	
	public Aluguel() {}
	
	
	public Aluguel(String nome, int nquarto, String email) {
		
		this.nome = nome;
		this.nquarto = nquarto;
		this.email = email;
}
	public String toString() {
		return "NOME: "+nome+ ", E-MAIL: "+email;
		}
	
	public String getNome() {
		return nome;
	}


	public void setNome(String nome) {
		this.nome = nome;
	}


	public int getNquarto() {
		return nquarto;
	}


	public void setNquarto(int nquarto) {
		this.nquarto = nquarto;
	}


	public String getEmail() {
		return email;
	}


	public void setEmail(String email) {
		this.email = email;
	}
	



}