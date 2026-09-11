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
       #rem = int(input("Choose the number you want to delete: "))
       # rem = rem - 1
      #  for ex in range(len(expenses)):
          #  if rem == ex:
           #total_amount = 0
        #for total in expenses:
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
"""

#expenses = []
#expenses.append(Expense_1)
#expenses.append(Expense_2)


"""if ans == "A":
                
                    a == 0
            elif ans == "B":
                for b in range(len(display["Option"])):
                    b == 1
            elif ans == "C":
                for c in range(len(display["Option"])):
                    c == 2
            elif ans == "D":
                for d in range(len(display["Option"])):
                    d == 3
                    
"""