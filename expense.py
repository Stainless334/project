import json
import os


ans = 0
if os.path.exists("expense.json"):
    with open("expense.json", "r") as file:
        file = json.load(file)
        expenses = file
else:
    expenses = []

    
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
    ans = (input("Write a number here: ")).capitalize()
    try:
        ans = int(ans)
    except ValueError:
        print("")
    if ans == 6:
        print("See you next time!")
        break
    elif ans == 1:
        print("Please fill the following info before you proceed")
        name = input("Enter expense name: ").capitalize()
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ").capitalize()
        Expense_3 = {
            "Name": name,
            "Amount": amount,
            "Category": category
        }
        expenses.append(Expense_3)
        print("Expense Added!")
        with open("expense.json", "w") as save_file:
            save_file = json.dump(expenses, save_file)
    elif ans == 2:
        if expenses == []:
            print("You have an empty list.")
        else:
            print("Your expenses:")
            for exp in expenses:
                print(exp["Name"], exp["Amount"], exp["Category"])
    elif ans == 3:
        if expenses == []:
            print("No Expenses added yet.")
        else:
            print("Total Expenses: ")
            total_amount = sum(total["Amount"] for total in expenses)
            print(f"${total_amount} only.")
    elif ans == 4:
        search = (input("Search Category: ")).capitalize()
        for see in expenses:
            if search == see["Category"]:
                print(f"Expense Found!: {see["Name"], see["Amount"], see["Category"]}")
            else:
                print(f"{search} was not found in your expenses.")
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
        print("Check the ('View expence') option for the updated Expenses")
        with open("expense.json", "w") as save_file:
            save_file = json.dump(expenses, save_file)

    else:
        print("Invalid option!")
        print("Please choose between 1 and 6.")
    
