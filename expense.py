import json

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
    #if ans != int:   print("Please write only numbers")

    ans = int(input("Write a number here: "))
    
    if ans == 6:
        print("See you next time!")
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
        if expenses == []:
            print("No Expenses added yet.")
        print("Total Expenses: ")
        total_amount = sum(total["Amount"] for total in expenses)
        print(total_amount)
    elif ans == 4:
        search = (input("Search Category: "))
        for see in expenses:
            if search == see["Category"]:
                print(f"Expense Found!: {see["Name"], see["Amount"], see["Category"]}")
    elif ans == 5:
        print("Choose a number from the following ")
        
        for crop in range(len(expenses)):
            print(f"{crop + 1}. {expenses[crop]["Name"]}")
        rem = int(input(">>> "))
        if rem > len(expenses):
            print("Invalid Option!")
            continue
        rem = rem - 1
        expenses.pop(rem)
        print("Deleted!")
        print("Check the ('View expence') option for the updeted Expenses")
    else:
        print("Invalid option!")
        print("Please choose between 1 and 6.")
        
