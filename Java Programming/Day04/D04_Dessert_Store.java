package Day04;
/*
Create an application for Desssert Store
the Store sells candies (per kg) cookies (per dozen) and ice creams (per peice)

develop hierarchy of desserts with calculatePrice mothod

a cart class should have addToCart() method that will update the cart value when user selects a perticular dessert
develop Store class as menu driver application what will take input from user.

1. Type of dessert
2. Quantity

Hierarchy:


 */
import Day04.Des;
import java.util.Scanner;

public class D04_Dessert_Store {
    private Shopping_Cart cart;
    private static Scanner sc = new Scanner(System.in);

    public D04_Dessert_Store(){
        this.cart = new Shopping_Cart();
    }

    public int select_Choice_Main_Interf(){

        System.out.print("--------------------------------------------------------------------------------------------");
        System.out.println("\nWelcome to Dessert Shop, please provide your choice.");
        System.out.println("1. Shop \n2. Generate Bill\n3. Exit");
        System.out.println("--------------------------------------------------------------------------------------------");
        System.out.println("Enter Your Choice: ");
        return sc.nextInt();
    }

    public void select_Desserts_Interf(){

        while( true){
            System.out.print("--------------------------------------------------------------------------------------------");
            System.out.println("Select Your Desserts: ");
            System.out.println("A. Candies: \n\t1. Coconut candy\n\t2. Strawberry candy\n\t3. Mango candy");
            System.out.println("B. Cookies: \n\t4. Chocolate cookies\n\t5. Resin cookies\n\t6. Coconut cookies");
            System.out.println("C. Ice Cream: \n\t7. Vanilla \n\t8. Butter Skotch \n\t9. Chocolate");
            System.out.println("--------------------------------------------------------------------------------------------");
            System.out.println("10. To Proceed your order.");
            System.out.println("Enter Your Choice: ");

            int choice = sc.nextInt();
            double qty;
            int qty2;

            switch(choice){
                case(1):
                    System.out.println("Enter the Quantity(in gms): ");
                    qty = sc.nextDouble();
                    Candy coco_cand = new Candy(Des.COCONUT_CANDY.getName(),
                            Des.COCONUT_CANDY.getPrice(),
                            qty);
                    this.cart.add_Item(coco_cand);
                    break;
                case(2):
                    System.out.println("Enter the Quantity(in gms): ");
                    qty = sc.nextDouble();
                    Candy straw_cand = new Candy("Strawberry candy", 120, qty);
                    this.cart.add_Item(straw_cand);
                    break;
                case(3):
                    System.out.println("Enter the Quantity(in gms): ");
                    qty = sc.nextDouble();
                    Candy mango_cand = new Candy("Mango candy", 125, qty);
                    this.cart.add_Item(mango_cand);
                    break;
                case(4):
                    System.out.println("Enter the Quantity(in num): ");
                    qty2 = sc.nextInt();
                    Cookies choco_cook = new Cookies("Choco Cookie", 115, qty2);
                    this.cart.add_Item(choco_cook);
                    break;
                case(5):
                    System.out.println("Enter the Quantity(in num): ");
                    qty2 = sc.nextInt();
                    Cookies resin_cook = new Cookies("Resin Cookie", 90, qty2);
                    this.cart.add_Item(resin_cook);
                    break;
                case(6):
                    System.out.println("Enter the Quantity(in num): ");
                    qty2 = sc.nextInt();
                    Cookies coco_cook = new Cookies("Coconut Cookie", 150, qty2);
                    this.cart.add_Item(coco_cook);
                    break;
                case(7):
                    System.out.println("Enter the Quantity(in no.): ");
                    qty2 = sc.nextInt();
                    Ice_Cream vanilla = new Ice_Cream("Vanilla", 100, qty2);
                    this.cart.add_Item(vanilla);
                    break;
                case(8):
                    System.out.println("Enter the Quantity(in no.): ");
                    qty2 = sc.nextInt();
                    Ice_Cream butter_k = new Ice_Cream("Butter Skotch", 120, qty2);
                    this.cart.add_Item(butter_k);
                    break;
                case(9):
                    System.out.println("Enter the Quantity(in no.): ");
                    qty2 = sc.nextInt();
                    Ice_Cream choco = new Ice_Cream("Chocolate", 120, qty2);
                    this.cart.add_Item(choco);
                    break;
                case(10):
                    return ;
                default:
                    System.out.println("Invalid Choice");
                    break;
            }
        }
    }

    public void generate_Bill(){

        System.out.println("\nTotal Bill: ");

        for(Dessert item : this.cart.items){
            System.out.println(item.get_stat());
        }

        System.out.println("Total bill\t\t" + this.cart.calculate_Current_Bill());
    }

    public static void main(String[] args) {

        D04_Dessert_Store store = new D04_Dessert_Store();

        while(true) {

            switch (store.select_Choice_Main_Interf()) {
                case (1):
                    store.select_Desserts_Interf();
                    break;
                case (2):
                    store.generate_Bill();
                    break;
                case (3):
                    return;

            }
        }
    }
}
