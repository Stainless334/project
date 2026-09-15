import random
quiz = {
        "Quest": "What is the capital of France?",
        "Option": ("Tokyo", "Abuja", "Paris", "London"), 
        "Ans": "Paris",
        "Difficulty": "Easy"
}
quiz_2 = {
        "Quest": " 5 + 7 = ?",
        "Option": ("35", "12", "2", "13"),
        "Ans": "12",
        "Difficulty": "Easy"
}
quiz_3 = {
        "Quest": "Which language are we using to build this quiz",
        "Option": ("Python", "Golang", "Java", "Javascript"),
        "Ans": "Python",
        "Difficulty": "Easy"
}
quiz_4 = {
        "Quest": "What is the largest planet in our solar system?",
        "Option": ("Mars", "Jupiter", "Saturn", "Neptune"),
        "Ans": "Jupiter",
        "Difficulty": "Easy"
}
quiz_5 = {
        "Quest": "What is the chemical symbol for gold?",
        "Option": ("Au", "Ag", "Fe", "Hg"),
        "Ans": "Au",
        "Difficulty": "Medium"
}
quiz_6 = {
    "Quest": "Which of the following is not self luminous?",
    "Option": ("Moon", "Lighted candle", "Incandescent electric bulb", "Incandescent fluorescent tube"),
    "Ans": "Moon",
    "Difficulty": "Medium"
}
quiz_7 = {
    "Quest": "Which of the following is not a programming language?",
    "Option": ("Python", "Java", "HTML", "C++"),
    "Ans": "HTML",
    "Difficulty": "Medium"
}
quiz_8 = {
    "Quest": "What is the capital of Japan?",
    "Option": ("Beijing", "Seoul", "Tokyo", "Bangkok"),
    "Ans": "Tokyo",
    "Difficulty": "Easy"
}
quiz_9 = {
    "Quest": "The implication x => y is equivalent to",
    "Option": ("~ y => ~ x", "y => ~x", "~ x => ~y", "y => x"),
    "Ans": "~ y => ~ x",
    "Difficulty": "Hard"
}
quiz_10 = {
    "Quest": "Alums are classified as",
    "Option": ("simple salts", "double salts", "anhydrous salts", "acid salts"),
    "Ans": "double salts",
    "Difficulty": "Hard"
}
quiz_11 = {
    "Quest": "A salt which loses mass when exposed to air is called",
    "Option": ("hygroscopic", "efflorescent", "deliquescent", "flourescent"),
    "Ans": "efflorescent",
    "Difficulty": "Hard"
}
quiz_12 = {
    "Quest": "The mangrove swamp in Nigeria is restricted to the",
    "Option": ("Sahel savanna", "Sudan savanna", "Guinea savanna", "Tropical rainforest"),
    "Ans": "Tropical rainforest",
    "Difficulty": "Medium"
}
quiz_13 = {
    "Quest": "When a virus is placed in a non-living medium it",
    "Option": ("Becomes dehydrated", "Forms flagella", "Becomes crystallized", "Forms spores"),
    "Ans": "Becomes crystallized",
    "Difficulty": "Hard"
}
quiz_14 = {
    "Quest": "Which country is famous for the pyramids of Giza?",
    "Option": ("Egypt", "Greece", "Turkey", "Iraq"),
    "Ans": "Egypt",
    "Difficulty": "Easy"
}
quiz_15 = {
    "Quest": "Which animal is the largest mammal in the world?",
    "Option": ("Elephant", "Blue Whale", "Giraffe", "Hippopotamus"),
    "Ans": "Blue Whale",
    "Difficulty": "Easy"
}

question = [quiz, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10, quiz_11, quiz_12, quiz_13, quiz_14, quiz_15]

def RunQuiz():
    rep = "Yes"
    while rep == "Yes":
        

        random.shuffle(question)
        score = SolveQuestion(question)
        
        percent = CalcPercentage(score)
        message = Performance(percent)

        FinalResult(score, len(question), percent, message)
        
                
            
        
            
        replay = input("Would you like to replay the quiz?: ").capitalize().strip()
        while replay != "Yes" and replay != "No":
            print("Invalid input!")
            print("Please enter either 'Yes' or 'No'")
            replay = input("Try again: ").capitalize().strip()

        if rep == replay:
            print("Alright!")
            continue
        elif replay == "No":
            print("Thank you for playing!!")
            break
       
            
def AskQuestion(i, display):
    print(f"Question: {i + 1}/{len(question)}")
    print(f"{display["Quest"]}")
    options = list(display["Option"])
    random.shuffle(options)
    for ex, opt in enumerate(options):
        print(f"{chr(65 + ex)}. {opt}")

    ans = input("Your answer: ").capitalize().strip()
    while ans != "A" and ans != "B" and ans != "C" and ans != "D":

        print("Invalid Input!!")
        print("Please choose options from 'A to D'.")
        ans = input("Try again: ").capitalize().strip()
                
    if ans == "A":
        ans = 0
    elif ans == "B":
        ans = 1
    elif ans == "C":
        ans = 2
    elif ans == "D":
        ans = 3
               
    selected = (options)[ans]
    if selected == (display["Ans"]):
        
        print("Correct!!!")
        return True
    else:
        print("Wrong!!")
        print(f"The correct answer is {(display["Ans"])}.")
        return False


def SolveQuestion(question):
    score = 0
    for i, display in enumerate(question):
        result = AskQuestion(i, display)
        if result == True:
            score += 1
    return score
    

def CalcPercentage(score):
    percent = round((score / len(question)) * 100, 2)
    return percent


def Performance(percent):
    if 100 >= percent >= 90:
        percent = "Excellent!"
    elif 90 > percent >= 70:
        percent = "Great work!"
    elif 70 > percent >= 50:
        percent = "Good effort!"
    elif percent < 50:
        percent = "Keep practicing!"
    return percent


def FinalResult(score, total, percentage, message,):
    print(f"Final Score: {score}/{total}")
    print(percentage)
    print(message)
    
    

RunQuiz()     


