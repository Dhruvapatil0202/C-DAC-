# Online food ordering system

class FoodItem:

    def __init__(self, name, price,category):
        self.name = name
        self.price = price
        self.category = category

    def display_info(self):
        print(f"Food Item: {self.name}      Price: {self.price}       Food Item Category: {self.category}")

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.order_history = []
        self.order_no = 0

    def place_order(self, food_item, quantity):
        self.order_no += 1
        self.order_history.append((self.order_no, self.name, food_item, quantity))

    def view_order_history(self):
        for order in self.order_history:
            print(f"{order[0]}\t\tCustomer Name: {order[1]}\t\tFood Ordered: {order[2].name}\t\tFood Item: {order[3]}\t\tQuantity: {order[4]}")


class RegularCustomer(Customer):

    def __init__(self, name, customer_id):
        super().__init__(name,customer_id)
        self.discount = 0.5

    def place_order(self, food_item, quantity):
        self.order_no += 1
        self.bill = (food_item.price * quantity) - (food_item.price * quantity) * self.discount
        self.order_history.append((self.order_no, self.name, food_item, quantity, self.discount, self.bill))

class PremiumCustomer(Customer):


    def __init__(self, name, customer_id):
        super().__init__(name,customer_id)
        self.discount = 1.5
        self.priority_delivery = None

    def place_order(self, food_item, quantity):
        self.order_no += 1
        self.priority_delivery = True
        self.bill = (food_item.price*quantity)-(food_item.price*quantity)*self.discount
        self.order_history.append((self.order_no, self.name, food_item, quantity, self.discount, self.bill))

class Restaurant:

    def __init__(self):
        self.menu = []
        self.customers = []

    def add_food_item(self, food_item):
        self.menu.append(food_item)

    def add_customer(self,customer):
        self.customers.append(customer)

    def display_menu(self):
        for dish in self.menu:
            print(f"Dish: {dish.name}\t\tDish Category: {dish.category}\t\tDish Price: {dish.price}")

    def display_customers(self):
        for customer in self.customers:
            print(f"Customer Name: {customer.name}\t\tCustomer Id: {customer.customer_id}\t\tTotal Orders: {customer.order_no}")


sandwich = FoodItem("Sandwich",120.00,"Snacks")
pizza = FoodItem("Pizza",560.00,"Snacks")
paneer = FoodItem("Paneer Tikka",320.00,"Main Course")


customer1 = RegularCustomer("customer1",123)
customer2 = PremiumCustomer("customer2",124)
customer3 = RegularCustomer("customer3",125)
customer4 = PremiumCustomer("customer4",126)

restaurant = Restaurant()

restaurant.add_food_item(sandwich)
restaurant.add_food_item(pizza)
restaurant.add_food_item(paneer)

restaurant.add_customer(customer1)
restaurant.add_customer(customer2)
restaurant.add_customer(customer3)
restaurant.add_customer(customer4)

customer1.place_order(pizza,3)
customer1.place_order(paneer,1)
customer1.place_order(sandwich,4)

customer2.place_order(paneer,2)

customer3.place_order(sandwich,4)
customer3.place_order(paneer,2)
customer3.place_order(pizza,4)

restaurant.display_customers()
print()
restaurant.display_menu()

print()
print()
customer1.view_order_history()
customer2.view_order_history()
customer3.view_order_history()
customer4.view_order_history()


