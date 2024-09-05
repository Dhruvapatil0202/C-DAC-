monthly_income = float(input("Enter monthly Income: "))
rent = float(input("Enter Rent amount: "))
groceries = float(input("Enter groceries expenses: "))
util = float(input("Enter utilities expenses: "))
other = float(input("Enter other expenses: "))

monthly_expenses = rent + groceries + util + other

savings = monthly_income - monthly_expenses
percent_savings = round((savings/monthly_income)*100, 2)

print(f"")
print(f"Total Savings: {savings}")
print(f"Percentage Savings: {percent_savings}")
print(f"Percentage Spent: {100 - percent_savings}")
