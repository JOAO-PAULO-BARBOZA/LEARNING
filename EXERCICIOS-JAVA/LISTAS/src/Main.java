import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

import entities.Employee;

public class Main {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		List<Employee> employees = new ArrayList<>();

		
		System.out.println("HOW MANY EMPLOYEES WILL BE REGISTRED?");
		int nemp = sc.nextInt(); 
		
		
		for (int i = 0; i < nemp; i++) {
			System.out.println("EMPLOYEE'S ID: ");
			int id = sc.nextInt();
			
			System.out.println("EMPLOYEE'S NAME: ");
			sc.nextLine();
			String name = sc.nextLine();
			
			System.out.println("EMPLOYEE'S SALARY: ");
			double salary = sc.nextDouble();
			Employee employee = new Employee(id, name, salary);

			
			employees.add(employee);
			
			
	}
			System.out.println(employees);
		
		System.out.println("ENTER THE EMPLOYEE ID THAT WILL HAVE SALARY INCREASE: ");
		int idsalary = sc.nextInt();
		sc.nextLine();
		Integer pos = cid(employees, idsalary);
		if (pos == null) {
			System.out.println("THIS ID DOES NOT EXIST!");
		}
		else {
			
			
		}
		
		
		
		System.out.println("ENTER THE PERCENTAGE: ");
		int percentage = sc.nextInt();
		

		
		sc.close();

	}

	public static Integer cid(List<Employee> employees, int id) {
		for (int i = 0; i < employees.size(); i++) {
			if (employees.get(i).getId() == id) {
				return i;
			}
		}
		return null;
	
	
	}
	
	
	
	
}
