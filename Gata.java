import java.util.Scanner;

public class Gata {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Choose Gate (AND, OR, NOT, XOR, NOR, NAND):");
        String gate = sc.next().toUpperCase();
        int a = 0,b=0;
        if (!gate.equals("NOT")) {
            System.out.println("Enter first input (0 or 1):");
            a = sc.nextInt();
            System.out.println("Enter second input (0 or 1):");
            b = sc.nextInt();
            a = (a == 0) ? 0 : 1;
            b = (b == 0) ? 0 : 1;
        }
        else{
            System.out.println("Enter input (0 or 1):");
            a = sc.nextInt();
            a = (a == 0) ? 0 : 1;
        }
        int result = 0;
        switch (gate) {
            case "AND":
                result = a&b;
                break;
            
            case "OR":
                result = a|b;
                break;
            
            case "NOT":
                result = (a==0)?1:0;
                break;
            
            case "XOR":
                result = a^b;
                break;
            
            case "NOR":
                
                result = 1 - (a | b);
                break;

            case "NAND":
                result = 1 - (a & b);
                break;
            
            default:
                System.out.println("Galat hei");
                break;
        }
        System.out.println("Output: "+result);
    }
    
}
