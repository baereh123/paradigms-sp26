package paradigms;
import paradigms.classes.Student;

public class StudentMain{
	public static void main(String[] args){
		String name = "John Doe";
		String [] grades = new String[]{"A", "A-", "B+", "C"};
		Student student = new Student(grades, name);
		System.out.println(student.computeGPA()); // null?
		// System.out.println(student.getGrades());
	}
}