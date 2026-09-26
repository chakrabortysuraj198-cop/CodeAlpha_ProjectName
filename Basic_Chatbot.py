print("===================================")
print("       Welcome to My Chatbot")
print("===================================")
print("Type 'bye' to exit the chatbot.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How can I help you?")

    elif "how are you" in user:
        print("Bot: I am fine. Thank you for asking!")

    elif "your name" in user:
        print("Bot: My name is Python Chatbot.")

    elif "who are you" in user:
        print("Bot: I am a simple chatbot created using Python.")

    elif "what can you do" in user:
        print("Bot: I can chat with you and answer some basic questions.")

    elif "thank" in user:
        print("Bot: You're welcome!")

    elif "bye" in user:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")