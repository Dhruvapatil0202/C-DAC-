package Day04;
import java.util.ArrayList;
public class Shopping_Cart {

    protected ArrayList<Dessert> items = new ArrayList<>();
    protected int item_Count = 0;

    public void add_Item(Dessert item){
        this.items.add(item);
        this.item_Count += 1;
    }

    public double calculate_Current_Bill(){
        double curr_Bill = 0;
        for(Dessert des: items){
            curr_Bill += des.calculate_Price();
        }
        return curr_Bill;
    }

}
