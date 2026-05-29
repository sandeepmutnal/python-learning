# Project 8
# TF-IDF Intelligent Chatbot

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# Training Questions

questions = [
    "hello",
    "how are you",
    "what is python",
    "what is ai",
    "help me",
    "bye"
]


# Bot Responses

responses = [
    "Hello! Nice to meet you!",
    "I am fine. Thank you!",
    "Python is a programming language.",
    "AI means Artificial Intelligence.",
    "I am here to help you.",
    "Goodbye!"
]


# TF-IDF Vectorizer

vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(questions)


print("🤖 Intelligent AI Chatbot Started\n")


while True:

    # User Input

    user_input = input("You: ")


    # Convert User Input into Numbers

    user_vector = vectorizer.transform([user_input])


    # Similarity Calculation

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )


    # Best Match

    best_match = np.argmax(similarity)


    # Get Similarity Score

    best_score = similarity[0][best_match]


    # Response Logic

    if best_score > 0.3:

        print("Bot:", responses[best_match])

        if questions[best_match] == "bye":
            break

    else:
        print("Bot: Sorry, I do not understand.")