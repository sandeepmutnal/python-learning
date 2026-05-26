# Project 8
# Basic AI Chatbot

print("🤖 AI Chatbot Started")
print("Type 'bye' to stop the chatbot\n")


while True:

    user_input = input("You: ").lower()


    # Greetings

    if user_input == "hello":
        print("Bot: Hello! Welcome!")

    elif user_input == "how are you":
        print("Bot: I am fine. Thank you!")

    elif user_input == "what is your name":
        print("Bot: I am an AI chatbot.")

    elif user_input == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I do not understand.")