"""

Expense_1 = {
    "Name": "School fees",
    "Amount": 35000,
    "Category": "Children"
}
Expense_2 = {
    "Name": "Lunch",
    "Amount": 2500,
    "Category": "Food"
}


the_list = [Expense_1, Expense_2]


        # ADD EXPENSE
print("Enter name of expense.")
name = input()

print("What is the amount?")
amount = input()

print("Enter expense category.")
cat = input()

Expense_n = {
    "Name": name,
    "Amount": float(amount),
    "Category": cat
}
the_list.append(Expense_n)

for view in (the_list):
    print(*view.values())
  
  # VIEW TOTAL
total_amount = 0
for total in the_list:
    total_amount += total["Amount"]

print(total_amount)
"""
Expense_1 = {
    "Name": "School fees",
    "Amount": 35000,
    "Category": "Children"
}
Expense_2 = {
    "Name": "Lunch",
    "Amount": 2500,
    "Category": "Food"
}
expenses = []
expenses.append(Expense_1)
expenses.append(Expense_2)
ans = 0
while ans != 6:
    print("Enter a number representing the following options")
    print("""
    1. Add expense
    2. View expenses
    3. View total
    4. Search expenses
    5. Delete expense
    6. Exit
    """)
    ans = int(input("Write a number here: "))
    if ans == 6:
        print("See you next time.")
        break
    elif ans == 1:
        print("Please fill the following info before you proceed")
        name = input("Enter expense name: ")
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")
        Expense_3 = {
            "Name": name,
            "Amount": amount,
            "Category": category
        }
        expenses.append(Expense_3)
        print("Expense Added!")
    elif ans == 2:
        print("Your expenses:")
        for exp in expenses:
            print(exp["Name"], exp["Amount"], exp["Category"])
    elif ans == 3:
        #total_amount = 0
        #for total in expenses:
            print("Total Expenses: ")
            total_amount = sum(total["Amount"] for total in expenses)
            print(total_amount)
    elif ans == 4:
        search = (input("Search Category: "))
        for see in expenses:
            if search == see["Category"]:
                print(see)
    elif ans == 5:
        print("Choose an Expense name")
        



        
    