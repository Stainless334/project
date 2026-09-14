import random
quiz = {
        "Quest": "What is the capital of France?",
         "Option": ("Tokyo", "Abuja", "Paris", "London"), 
        "Ans": "Paris"
}
quiz_2 = {
        "Quest": " 5 + 7 = ?",
        "Option": ("35", "12", "2", "13"),
        "Ans": "12"
}
quiz_3 = {
        "Quest": "Which language are we using to build this quiz",
        "Option": ("Python", "Golang", "Java", "Javascript"),
        "Ans": "Python"
}

question = [quiz, quiz_2, quiz_3]

def RunQuiz():
    rep = "Yes"
    while rep == "Yes":
        score = 0

        random.shuffle(question)
        for i, display in enumerate(question):
            result = AskQuestion(i, display)
            if result == True:
                score += 1
        print(f" Final score: {score} / {len(question)} ({round((score / len(question)) * 100, 2)}%)")
        replay = input("Would you like to replay the quiz?: ").capitalize()
        if rep == replay:
            print("Alright!")
            continue
        elif replay == "No":
            print("Thank you for playing!!")
            break
        else:
            print("Invalid Option")
            break
            


def AskQuestion(i, display):
    print(f"Question: {i + 1}/{len(question)}")
    print(f"{display["Quest"]}")
    for ex in range(len(display["Option"])):
       print(f"{chr(65 + ex)}. {(display["Option"])[ex]}")

    ans = input("Your answer: ").capitalize()
    while ans != "A" and ans != "B" and ans != "C" and ans != "D":

        print("Invalid Input!!")
        print("Please choose options from 'A to D'.")
        ans = input("Try again: ").capitalize()
                


    if ans == "A":
        ans = 0
    elif ans == "B":
        ans = 1
    elif ans == "C":
        ans = 2
    elif ans == "D":
        ans = 3
            
                
    selected = (display["Option"])[ans]
    if selected == (display["Ans"]):
        #score += 1
        print("Correct!!!")
        return True
    else:
        print("Wrong!!")
        print(f"The correct answer is {(display["Ans"])}.")
        return False
        
        
        
RunQuiz()
