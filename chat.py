

ans = ""
while ans != "Exit":

    ans = input("You: ").strip().capitalize()
    def get_response(ans):

        
        if ans == "Hello":
            ans = ("Bot: Hello! How can I assist you today?")
        elif ans == "What is python?":
            ans = ("Bot: Python is a high-level, interpreted programming language known for its readability and versatility.")
        elif ans == "What is a function?":
            ans = ("Bot: A function is a block of organized, reusable code that performs a single action or task.")
        else:
            ans = (f"Bot: I am not sure how to respond to that")
        return ans
    print(get_response(ans))
else:
    print("Bot: Goodbye! Have a great day!")

