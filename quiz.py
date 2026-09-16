import time
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
quiz_16 = {
    "Quest": "When a brick is taken from the earth's surface to the moon, its mass will",
    "Option": ("Increase", "Decrease", "Remain constant", "become zero"),
    "Ans": "Remain constant",
    "Difficulty": "Medium"
}
quiz_17 = {
    "Quest": "A simple machine with an efficiency of 75% lifts a load of 5000 N when a force of 500 N is applied to it. Calculate the velocity ratio of the machine.",
    "Option": ("13.3", "17.5", "25.0", "10.0"),
    "Ans": "13.3",
    "Difficulty": "Hard"
}
quiz_18 = {
    "Quest": "What is the fastest land animal in the world?",
    "Option": ("Cheetah", "Lion", "Horse", "Tiger"),
    "Ans": "Cheetah",
    "Difficulty": "Easy"
}
quiz_19 = {
    "Quest": "Which gas is most abundant in the Earth's atmosphere?",
    "Option": ("Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"),
    "Ans": "Nitrogen",
    "Difficulty": "Easy"
}
quiz_20 = {
    "Quest": "What is the largest ocean on Earth?",
    "Option": ("Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"),
    "Ans": "Pacific Ocean",
    "Difficulty": "Easy"
}
quiz_21 = {
    "Quest": "If a sound wave goes from a cold-air region to a hot-air region, its wavelength",
    "Option": ("Increases", "Decreases", "Remains constant", "Decreases then increases"),
    "Ans": "Increases",
    "Difficulty": "Medium"
}
quiz_22 = {
    "Quest": "The vibration of an air column produces the sound in the",
    "Option": ("piano", "guitar", "flute", "school hand bell"),
    "Ans": "flute",
    "Difficulty": "Medium"
}
quiz_23 = {
    "Quest": "Echo CANNOT be used for",
    "Option": ("medical ultrasound", "operations of fibre optic cables", "oil prospecting", "detecting flaws in metal casting"),
    "Ans": "operations of fibre optic cables",
    "Difficulty": "Hard"
}
quiz_24 = {
    "Quest": "In which of the following material media would sound travel faster?",
    "Option": ("Metal", "Water", "Oil", "Gas"),
    "Ans": "Metal",
    "Difficulty": "Medium"
}
quiz_25 = {
    "Quest": "The velocity of sound in air will be doubled if its absolute temperature is",
    "Option": ("doubled", "halved", "quadrupled", "constant"),
    "Ans": "quadrupled",
    "Difficulty": "Hard"
}
quiz_26 = {
    "Quest": "The most suitable substance for putting out petrol fire is",
    "Option": ("Water", "Sand", "Fire blanket", "Carbon(IV)oxide"),
    "Ans": "Carbon(IV)oxide",
    "Difficulty": "Medium"
}
quiz_27 = {
    "Quest": "Diamond does not conduct electricity because it",
    "Option": ("has no free valence electrons", "is a giant molecule", "contains no bonded electrons", "is a solid at room temperature"),
    "Ans": "has no free valence electrons",
    "Difficulty": "Hard"
}
quiz_28 = {
    "Quest": "Methanol is obtained from wood by",
    "Option": ("combustion", "esterification", "destructive distillation", "bacterial decomposition"),
    "Ans": "destructive distillation",
    "Difficulty": "Hard"
}
quiz_29 = {
    "Quest": "The alloy used for metal work and plumbing contains",
    "Option": ("lead and tin", "copper and tin", "aluminium and copper", "iron and carbon"),
    "Ans": "lead and tin",
    "Difficulty": "Hard"
}
quiz_30 = {
    "Quest": "Which of the following halogens is solid at room temperature?",
    "Option": ("Chlorine", "Bromine", "Iodine", "Fluorine"),
    "Ans": "Iodine",
    "Difficulty": "Medium"
}
question = [quiz, quiz_2, quiz_3, quiz_4, quiz_5, quiz_6, quiz_7, quiz_8, quiz_9, quiz_10, quiz_11, quiz_12, quiz_13, quiz_14, quiz_15, quiz_16, quiz_17, quiz_18, quiz_19, quiz_20, quiz_21, quiz_22, quiz_23, quiz_24, quiz_25, quiz_26, quiz_27, quiz_28, quiz_29, quiz_30]
rep = "Yes"
while rep == "Yes":
    

    def RunQuiz():




            global filter_question
            filter_question = FilterQuiz()
            random.shuffle(filter_question)
            score = SolveQuestion(filter_question)

            percent = CalcPercentage(score)
            message = Performance(percent)

            FinalResult(score, len(filter_question), percent, message)

    def FilterQuiz():
        difficulty = input("Choose a difficulty level (Easy, Medium, Hard): ").strip().capitalize()
        while difficulty != "Easy" and difficulty != "Medium" and difficulty != "Hard":
            print("Invalid input!")
            print("Please choose either 'Easy', 'Medium' or 'Hard'.")
            difficulty = input("Try again: ").strip().capitalize()
        filter_question = [q for q in question if q["Difficulty"] == difficulty]
        while len(filter_question) == 0:
            print(f"No questions available for {difficulty} difficulty.")
            difficulty = input("Choose a different difficulty level (Easy, Medium, Hard): ").strip().capitalize()
            while difficulty != "Easy" and difficulty != "Medium" and difficulty != "Hard":
                print("Invalid input!")
                print("Please choose either 'Easy', 'Medium' or 'Hard'.")
                difficulty = input("Try again: ").strip().capitalize()
            filter_question = [q for q in question if q["Difficulty"] == difficulty]
        return filter_question
            
    def AskQuestion(i, display):
        start_time = time.time()
        print(f"Question: {i + 1}/{len(filter_question)}")
        print(f"{display["Quest"]}")
        options = list(display["Option"])
        random.shuffle(options)
        for ex, opt in enumerate(options):
            print(f"{chr(65 + ex)}. {opt}")

        ans = input("Your answer: ").strip().capitalize()
        while ans != "A" and ans != "B" and ans != "C" and ans != "D":

            print("Invalid Input!!")
            print("Please choose options from 'A to D'.")
            ans = input("Try again: ").strip().capitalize()
        end_time = time.time()
        time_taken = end_time - start_time
        if ans == "A":
            ans = 0
        elif ans == "B":
            ans = 1
        elif ans == "C":
            ans = 2
        elif ans == "D":
            ans = 3
        print(f"Time taken: {time_taken:.2f} seconds")
        selected = (options)[ans]
        if selected == (display["Ans"]):

            print("Correct!!!")
            return True
        else:
            print("Wrong!!")
            print(f"The correct answer is {(display["Ans"])}.")
            return False


    def SolveQuestion(filter_question):
        score = 0
        for i, display in enumerate(filter_question):
            result = AskQuestion(i, display)
            if result == True:
                score += 1
        return score


    def CalcPercentage(score):
        percent = round((score / len(filter_question)) * 100, 2)
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
    replay = input("Would you like to replay the quiz?: ").strip().capitalize()


    while replay != "Yes" and replay != "No":
        print("Invalid input!")
        print("Please enter either 'Yes' or 'No'")
        replay = input("Try again: ").strip().capitalize()

    if rep == replay:
        print("Alright!")
        continue
    elif replay == "No":
        print("Thank you for playing!!")
        break
                
    

    

#RunQuiz()     


