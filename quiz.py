import csv
import streamlit as st


def load_words(file_name):
    words = []
    with open(file_name, mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  
        for row in csv_reader:
            words.append(row[0])
    return words

words = load_words('order.csv')

st.title("Shuffled Word Game")
st.write(
    """
    This app displays shuffled words. Guess the original word! Below is the code that processes the CSV file.
    """
)

code_snippet = """
import csv


with open('order.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row if it exists

  
    for row in csv_reader:
        word = row[0]
        shuffled = ''.join(sorted(word))  
        print(f"Shuffled: {shuffled}")
"""
st.code(code_snippet, language="python")


if 'current_index' not in st.session_state:
    st.session_state.current_index = 0 

current_word = words[st.session_state.current_index]
shuffled_word = ''.join(sorted(current_word))
st.write(f"Shuffled Word: **{shuffled_word}**")

if st.button("Next Word"):

    st.session_state.current_index = (st.session_state.current_index + 1) % len(words)
