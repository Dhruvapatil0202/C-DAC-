#
# balance = int(input("Enter the current balance: "))
#
#
# while True:
#     print(f"\nYour Current Balance is {balance}")
#     resp = input("\nWould you like to withdraw? Y/N: ")
#     if resp != "Y":
#         exi_resp = input("\nWould you like to exit? Y/N: ")
#         if exi_resp == "Y": break
#         else: continue
#
#     else:
#         withdrawal = int(input("Enter the amount you want to Withdraw: "))
#         if withdrawal > balance:
#             print("\nError: Withdrawal amount is greater than current balance!! ")
#             continue
#         elif withdrawal % 10 != 0:
#             print("\nError: withdrawal amount is invalid.")
#             continue
#         else:
#             balance -= withdrawal
#             print(f"\nWithdrawal of {withdrawal} Rs. is successful, current balance is {balance}")


#------------------------------------------------------------------------------------

amt = int(input("Enter your Balance amount: "))

while True:

    choice = input("Do you want to withdraw: ").lower()
    if(choice == "y"):
        withdraw = int(input("Enter the amount to withdraw: "))
        if(amt >= withdraw and withdraw % 10 == 0):
            amt -= withdraw
            print(f"Amount has been withdrawn successfully,\n"
                  f"Your remaining balance is {amt} and your withdrawn amount is {withdraw}")
        else:
            if(amt < withdraw):
                print(f"Not enough balance in your account to withdraw")
            else:
                print("Withdrawal amount must be multiple of 10")
    elif(choice == "n"):
        break


