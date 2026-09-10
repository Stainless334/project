quiz = {
        "Quest": "What is the capital of France?",
         "Option": ("Tokyo", "Abuja", "Paris", "London"), 
        "Ans": "Paris"
}
quiz_2 = {
        "Quest": "What is 5 + 7?",
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
        for display in (question):
            print(display["Quest"])
            for ex in range(len(display["Option"])):
                print(f"{chr(65 + ex)}. {(display["Option"])[ex]}")
            ans = input("Your answer: ").capitalize()
            for check in range(len(question)):
                for cross in 
                if (ord(ans) - 65) == check  and  check == check:

                
                    score += 1
                    print("Correct!!!")
                else:
                    print("Wrong!")
                    print(f"The correct answer is {display["Ans"]}.")
        print(f"{score} / {len(question)}")
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
(RunQuiz())
