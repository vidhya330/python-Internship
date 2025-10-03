# Task 8: Rule-Based Chatbot using if-else

print(" Chatbot: Hello! I am your simple chatbot. Type 'bye' to exit.")

while True:
    user_input = input("You: ").lower()  

    if user_input in ["hi", "hello", "hey"]:
        print(" Chatbot: Hello! How can I help you today?")
    
    elif "name" in user_input:
        print(" Chatbot: My name is PyBot. I am here to chat with you!")
    
    elif "how are you" in user_input:
        print(" Chatbot: I'm doing great, thank you! How are you?")
    
    elif "time" in user_input:
        from datetime import datetime
        now = datetime.now()
        print(" Chatbot: The current time is", now.strftime("%H:%M:%S"))
    
    elif "date" in user_input:
        from datetime import datetime
        today = datetime.today()
        print(" Chatbot: Today's date is", today.strftime("%Y-%m-%d"))
    
    elif "bye" in user_input or "exit" in user_input or "quit" in user_input:
        print(" Chatbot: Goodbye! Have a great day ")
        break
    
    else:
        print(" Chatbot: Sorry, I don’t understand that. Can you rephrase?")
