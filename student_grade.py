def welcome():
    print("Welcome to Student Grade Manager!")

def greet(name):
    return f"Welcome to the program {name}."

def GetGrade():
    get = int(input("Enter the number of grades you need: "))
    for ex in range(get):
        print(f"grade {ex + 1}")

def grade_average(grade):
    grade = round(sum(grade) / len(grade), 2)
    return grade
def grade():
    score = grade_average([31, 27, 62, 56, 60, 41, 11, 34])
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
GetGrade()


