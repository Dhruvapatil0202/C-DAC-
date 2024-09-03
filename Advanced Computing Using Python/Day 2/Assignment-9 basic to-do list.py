
CHOICE_STR = """
1. Add task in the list
2. Mark task completed
3. See currently pending tasks
4. Exit
(type 1, 2, 3, 4 as choices): """

def print_to_do_list(item_list):
    if len(item_list) == 0:
        print("\nThere are No more tasks remaining!!!")
    else:
        print("\nCurrent tasks are as following: ")
        for ind in range(len(item_list)):
            print(f"{ind + 1}. {item_list[ind]}")
        print("")

def print_options():
    return input(CHOICE_STR)


to_do_list = []

while True:

    resp = print_options()

    if resp == "1":
        new_task = input("Enter new task: ")
        to_do_list.append(new_task)
        print("New task has been inserted successfully. \n")

    elif resp == "2":
        if len(to_do_list) == 0:
            print("No tasks are currently pending.")
            continue
        print("\n")
        print_to_do_list(to_do_list)
        comp_task_ind = int(input("Select the index of completed task. "))
        to_do_list.pop(comp_task_ind - 1)

    elif resp == "3":
        print_to_do_list(to_do_list)

    elif resp == "4":
        break

    else:
        print("Invalid input, Try again.")

 #----------------------------------------------------------------------------------------

 # to_do = []
 #
 # def add
