

class FoodItem:

    def __init__(self, name, price, category):
        self.name = name
        self.price = price
        self.category = category

    def display_info(self):
        print(f"Food Item: {self.name}")
        print(f"Food Item Price: {self.price}")
        print(f"Food Item Category: {self.category}")


class Customer:

    def __init__(self, name, cust_id):
        self.name = name
        self.customer_id = cust_id
        self.order_history = []
        # self.restaurant = restaurant

    def place_order(self, food_item, quantity, price, discount_percent):

        total = price * quantity
        discounted_total = total - ((total * discount_percent)/100)
        self.order_history.append((food_item, quantity, discounted_total))

        # print(f"Order got placed by trial1")

    def view_order_history(self):

        print(f"Order history of {self.name}: \n")
        for food_item, quantity, cost in self.order_history:
            print(f"{food_item}: {quantity} - {cost}")
        print("")


class RegularCustomer(Customer):

    def __init__(self, name, cust_id):
        super().__init__(name, cust_id)
        self.discount = 5


class PremiumCustomer(Customer):

    def __init__(self, name, cust_id):
        super().__init__(name, cust_id)
        self.discount = 15


class Restaurant:

    def __init__(self):
        self.menu = []
        self.customers = []

    def add_food_item(self, food_item):
        self.menu.append(food_item)

    def add_customer(self, new_customer):
        self.customers.append(new_customer)

    def display_menu(self):
        for food_item in self.menu:
            food_item.display_info()
            print("")

    def display_customers(self):
        for customer in self.customers:
            print(f"{customer.name}: {customer.order_history}")



if __name__ == '__main__':
    # Creating objects
    one_restaurant = Restaurant()

    food_item_one = FoodItem('Vengeful Chicken', 100, 'Main Course')
    food_item_two = FoodItem('Screaming Cream', 80, 'Dessert')
    food_item_three = FoodItem('Walling Lamb', 150, 'Main Course')
    food_item_four = FoodItem('Dragon Scales', 50, 'Starter')

    reg_cust_one = RegularCustomer(name = 'name1', cust_id= 100)
    reg_cust_two = RegularCustomer(name = 'name2', cust_id = 101)

    pre_cust_one = PremiumCustomer(name = 'pre_cust1', cust_id = 201)
    pre_cust_two = PremiumCustomer(name = 'pre_cust2', cust_id = 202)

    one_restaurant.menu.extend([food_item_one, food_item_four, food_item_two, food_item_three])
    one_restaurant.customers.extend([reg_cust_one, reg_cust_two, pre_cust_two, pre_cust_one])

    # Placing orders

    reg_cust_one.place_order(food_item_one.name, 3, food_item_one.price, reg_cust_one.discount)
    reg_cust_one.place_order(food_item_two.name, 10, food_item_two.price, reg_cust_one.discount)

    pre_cust_one.place_order(food_item_one.name, 3, food_item_one.price, pre_cust_one.discount)
    pre_cust_one.place_order(food_item_two.name, 10, food_item_two.price, pre_cust_one.discount)

    # Viewing order history
    reg_cust_one.view_order_history()
    pre_cust_one.view_order_history()


    # print(reg_cust_two)