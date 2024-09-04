
from tabulate import tabulate

CHOICE_STR = """

1. Add new item
2. Update the Item
3. Display inventory
4. exit
Enter index of your choice: """


def display_inventory(dict):
    headers = ['Item', 'Quantity', 'Price']
    data = [[item, dict[item]['quantity'], dict[item]['price']] for item in dict]
    print(tabulate(data, headers, tablefmt = 'grid'))
    # print(f"{'_' * 50}\nItem\t\tQuantity\t\tPrice\n")
    # for item, val in dict.items():
    #     print(f"{item}\t\t{val['quantity']}\t\t{val['price']}")

    total_value = sum(dict[i]["price"] * dict[i]["quantity"] for i in dict)

    print(f"\nTotal price of the inventory is {total_value}.")
    print(f"{'-' * 50}")

def add_new_item(dict):

    item = input("Enter Item name: ")
    if item in dict:
        print("Item already exists in Inventory! ")
        return dict

    quantity = int(input(f"Enter quantity of {item}: "))
    price = float(input(f"Enter price of {item}: "))



    dict[item] = {"quantity" : quantity,
                    "price" : price}
    return dict

def update_item(dict):

    item = input("Enter Item name: ")
    if item not in dict:
        print("Item not present in inventory!")
        return dict
    else:
        print(f"\n item: {item} price: {dict[item]['price']} quantity: {dict[item]['quantity']}")

    price = float(input(f"Enter New price of {item}: "))
    quantity = int(input(f"Enter New quantity of {item}"))
    dict[item]["price"] = price
    dict[item]["quantity"] = quantity

    return dict

    pass

item_num = int(input("Enter number of items: "))
print("")

items = {}
while item_num > 0:

    item = input("Enter Item name: ")
    quantity = int(input(f"Enter quantity of {item}: "))
    price = float(input(f"Enter price of {item}: "))

    if item in items:
        print("Item already exists. ")
        continue
    else: item_num -= 1

    print("")

    items[item] = {"quantity" : quantity,
                   "price" : price}


while True:
    resp = input(CHOICE_STR)

    match resp:
        case "1": items = add_new_item(items)
        case "2": items = update_item(items)
        case "3": display_inventory(items)
        case "4": break
        case _ : print("\nInvalid input!")



# _______________________________________________________________

# inventory = {}
#
# def addItems(inventory):
#     item_name = input("Enter Item Name : ")
#     if item_name in inventory:
#         print("Item already exists!")
#         return
#     quantity = int(input("Enter Item Quantity: "))
#     price = int(input("Enter Item Price: "))
#
#     inventory.update({item_name: [quantity, price]})
#
#     return inventory
#
# def updateQuantity(inventory):
#     item = input("Enter the item to update: ")
#     new_quantity = int(input("Enter the new quantity value for the current item: "))
#
#     inventory[item][0] = new_quantity
#     return inventory
#
#
# def updatePrice(inventory):
#     item = input("Enter the item to update: ")
#     new_price = int(input("Enter the new price value for the current item: "))
#
#     inventory[item][1] = new_price
#     return inventory
#
# def sumInventory(inventory):
#     sum = 0
#     for item in inventory:
#         sum += (inventory[item][0] * inventory[item][1])
#
#     return sum
#
# def displayInventory(inventory):
#     print(f"Items\t\tQuantity\t\tPrice")
#
#     for item in inventory:
#         print(f"{item}\t\t{inventory[item][0]}\t\t{inventory[item][1]}")
#
#     print(f"Total value of the inventory is {sumInventory(inventory)}")
#
# options = """
# 1. Add Items to your Inventory
# 2. Update Quantity for the item
# 3. Update Price of the Item
# 4. Get Total Value of the Inventory
# 5. Display your Inventory
# 6. Exit
# """
#
# while True:
#
#     choice = int(input(f"Enter your choice: \n{options}\n"))
#
#     match choice:
#         case 1:
#             inventory = addItems(inventory)
#         case 2:
#             inventory = updateQuantity(inventory)
#         case 3:
#             inventory = updatePrice(inventory)
#         case 4:
#             print(f"Total value of the inventory is : {sumInventory(inventory)}")
#         case 5:
#             displayInventory(inventory)
#         case 6:
#             break

