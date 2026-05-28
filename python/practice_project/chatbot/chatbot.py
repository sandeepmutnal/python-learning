# Project 8
# Intent Recognition Chatbot

import string


print("🤖 AI Chatbot Started")
print("Type 'bye' to stop the chatbot\n")


while True:

    # User Input

    user_input = input("You: ")


    # NLP Preprocessing

    user_input = user_input.lower()

    user_input = user_input.translate(
        str.maketrans('', '', string.punctuation)
    )


    # Greeting Intent

    greetings = [
        "hello",
        "hi",
        "hey"
    ]


    # Help Intent

    help_words = [
        "help",
        "support",
        "assist"
    ]


    # Python Intent

    python_words = [
        "python",
        "programming",
        "coding"
    ]


    # Intent Recognition Logic

    if any(word in user_input for word in greetings):
        print("Bot: Hello! Nice to meet you!")

    elif any(word in user_input for word in help_words):
        print("Bot: I am here to help you!")

    elif any(word in user_input for word in python_words):
        print("Bot: Python is great for AI and software development.")

    elif "ai" in user_input:
        print("Bot: AI means Artificial Intelligence.")

    elif user_input == "bye":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: Sorry, I do not understand.")