print("Welcome to CodeAlpha Chatbot!")
while True:
    user = input("You: ").lower()
    if user == "hello":
        print("Bot: Hi! How can I help you?")
    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")
    elif user == "your name":
        print("Bot: I am a Python Chatbot.")
    elif user == "help":
        print("Bot: You can ask me about my name or how I am.")
    elif user == "good morning":
        print("Bot: Good morning! Have a great day!")
    elif user == "thank you":
        print("Bot: You're welcome!")
    elif user == "what can you do":
        print("Bot: I can answer simple questions and have a basic conversation.")
    elif user == "bye":
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")