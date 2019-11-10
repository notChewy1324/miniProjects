public class PersonDatabase
{
	public static void main(String[] args) {
	    
	    //Values
	int age = 15;
	String person = "Ecoli";
	String passions = "Track & Field";
	String school = ("High School");
	String gradelevel = ("9");
	String lover = "None";
	
	//Reader Values
	String helpername = ("Name: ");
	String helperage = ("Age: ");
	String helperpassions = ("Passions: ");
	String helperschool = ("School: ");
	String helpergradelevel = ("Grade: ");
	String helperlover = ("GF: ");
	
	//Total Output Vaules
	String finalname = (helpername + person);
	String finalage = (helperage + age);
	String finalpassions = (helperpassions + passions);
	String finalschool = (helperschool + school);
	String finalgradelevel = (helpergradelevel + gradelevel);
	String finallover = (helperlover + lover);
	
	//Output
	System.out.println("Person Database Information");
	System.out.println("___________________________");
	System.out.println(finalname);
	System.out.println(finalage);
	System.out.println(finalpassions);
	System.out.println(finalschool);
	System.out.println(finalgradelevel);
	System.out.println(finallover);
	System.out.println("___________________________");
	}
	
}