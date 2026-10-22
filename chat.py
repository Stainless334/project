
def get_response(ans):

   
    
    return response.output_text


ans = ""
while ans != "Exit":
    
    ans = input("You: ").strip().capitalize()
    response = get_response(ans)

    print(response)
    
else:
    print("Bot: Goodbye! Have a great day!")




"""if ans == ("Hello"):
        ans = "Bot: How far G"
    elif ans == "How far":
        ans = "Bot: All good"
    else:
        ans = "Bot: I don't know how to respond to that."""