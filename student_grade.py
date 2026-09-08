def welcome():
    print("Welcome to Student Grade Manager!")

def greet(name):
    return f"Welcome to the program {name}."

def GetGrade():
    container = []
    
    
    get = int(input("Enter the number of grades you need: "))

    for ex in range(get):
        if get <= 0:
            return None
        else:
            obt = int(input(f"grade {ex + 1}: "))
        container.append(obt)
    return container
       

def grade_average():
    gets = GetGrade()
    
    grade = round(sum(gets) / len(gets), 2)
    return grade
def grade():
    score = grade_average()
    if 100 >= score >= 90:
        return("A")
    elif 89 >= score >= 80:
        return("B")
    elif 79 >= score >= 70:
        return("C")
    elif 69 >= score >= 60:
        return("D")
    elif 59 >= score >= 50:
        return("E")
    elif 50 > score >= 0:
        return("F")
    else :
        return("Invalid Score")
    

welcome()
print(greet("John"))
print(grade())

