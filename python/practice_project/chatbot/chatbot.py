# Project 8
# Multi-Intent AI Assistant

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


# Knowledge Base

questions = [
    "hello",
    "hi",
    "how are you",
    "what is python",
    "what is ai",
    "what is machine learning",
    "what is data science",
    "how to get a software job",
    "help me",
    "bye"
]

responses = [
    "Hello! Nice to meet you.",
    "Hi! How can I help you?",
    "I am doing well.",
    "Python is a popular programming language.",
    "AI means Artificial Intelligence.",
    "Machine Learning helps computers learn from data.",
    "Data Science extracts insights from data.",
    "Build projects, learn DSA, and practice coding interviews.",
    "I am here to help you.",
    "Goodbye!"
]


# Vectorization

vectorizer = TfidfVectorizer()

question_vectors = vectorizer.fit_transform(questions)

print("🤖 AI Assistant Started")
print("Type 'bye' to exit.\n")


while True:

    user_input = input("You: ")

    user_vector = vectorizer.transform([user_input])

    similarity = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match = np.argmax(similarity)

    best_score = similarity[0][best_match]

    if best_score > 0.3:

        print("Bot:", responses[best_match])

        if questions[best_match] == "bye":
            break

    else:
        print("Bot: Sorry, I don't understand that yet.")