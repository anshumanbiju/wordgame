import csv
import streamlit as st
import random

# Function to load words/phrases from a CSV file
def load_phrases(file_name):
    phrases = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            phrases.append(row[0])
    return phrases

# Load the phrases from the CSV
phrases = load_phrases('order.csv')

st.title("Shuffled Phrase Game")
st.write(
    """
    This app displays shuffled phrases. Guess the original phrase! Below is the code that processes the CSV file.
    """
)

# Updated code snippet for handling two-word phrases
code_snippet = """
import csv
import random

# Load phrases from a CSV file
with open('order.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if it exists

    # Shuffle letters of each word in the phrase
    for row in csv_reader:
        phrase = row[0]
        words = phrase.split()  # Split into individual words
        shuffled = ' '.join([''.join(random.sample(word, len(word))) for word in words])  # Shuffle each word separately
        print(f"Original: {phrase}, Shuffled: {shuffled}")
"""
st.code(code_snippet, language="python")

# Initialize state
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0  # Start from the first phrase

# Get the current phrase
current_phrase = phrases[st.session_state.current_index]

# Shuffle each word in the current phrase
def shuffle_words(phrase):
    words = phrase.split()  # Split into individual words
    shuffled_words = []
    for word in words:
        shuffled_word = ''.join(random.sample(word, len(word)))  # Shuffle the word
        shuffled_words.append(shuffled_word)
    return ' '.join(shuffled_words)

shuffled_phrase = shuffle_words(current_phrase)

# Display the shuffled phrase
st.write(f"Shuffled Phrase: **{shuffled_phrase}**")

# Button to move to the next phrase
if st.button("Next Phrase"):
    st.session_state.current_index = (st.session_state.current_index + 1) % len(phrases)
