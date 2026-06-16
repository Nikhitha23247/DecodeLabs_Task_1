print("🤖 AI Chatbot Started (type 'bye' to exit)")

while True:
    user = input("You: ").lower()

    if user in ["hello", "hi", "hey"]:
        print("Bot: Hello! How can I help you?")
    elif user in ["how are you"]:
        print("Bot: I am doing great!")
    elif user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye!")
        break
    else:
        print("Bot: Sorry, I don't understand.")
