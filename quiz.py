def RunQuiz():

    quiz = {
        "Quest": "What is the capital of France?",
        "Ans": "Paris"
    }
    quiz_2 = {
        "Quest": "What is 5 + 7?",
        "Ans": "12"
    }
    quiz_3 = {
        "Quest": "Which language are we using to build this quiz",
        "Ans": "Python"
    }
    question = [quiz, quiz_2, quiz_3]
    score = 0
    for display in (question):
        print(display["Quest"])
        ans = input("Your answer: ").capitalize()
        if ans == display["Ans"]:
            score += 1
            print("Correct!!!")
        else:
            print("Wrong!")
            print(f"The correct answer is {display["Ans"]}.")
    print(f"{score} / {len(question)}")
RunQuiz()