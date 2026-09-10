def welcome():
    print("Welcome to Student Grade Manager!")

def greet():
    name = input("What's your name sir?: ").capitalize()
    return f"Welcome to the program Mr/Mrs {name}."

def GetGrade():
    container = []
    
    
    get = (input("Enter the number of grades you need: "))
    try:
        get = int(get)
    except ValueError:
        return []
    else:
        for ex in range(get):
      
            obt = (input(f"grade {ex + 1}: "))
            try:
                obt = int(obt)
            except ValueError:
                return []
            else:    
                container.append(obt)
        return container
       

def grade_average():
    gets = GetGrade()
    if gets == []:
        return "Invalid Input"
    else:
        for res in gets:
            if res > 100 or res < 0:
                return "Invalid Input"
            
        grade = round(sum(gets) / len(gets), 2)
        return grade
def grade():
    score = grade_average()
    if score == "Invalid Input":
        return """Invalid Info!
Please enter a number from 1 to 100."""
    elif 100 >= score >= 90:
        return("A")
    elif 90 > score >= 80:
        return("B")
    elif 80 > score >= 70:
        return("C")
    elif 70 > score >= 60:
        return("D")
    elif 60 > score >= 50:
        return("E")
    elif 50 > score >= 0:
        return("F")
    else :
        return("Invalid Score")
    
welcome()
print(greet())
#print(grade_average())
print(grade())
