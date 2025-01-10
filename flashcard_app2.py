import streamlit as st
import pandas as pd
import random

# Load the flashcard data
@st.cache_data
def load_data():
    return pd.read_excel('german-english-swedish.xlsx')

data = load_data()

# Initialize session state for tracking progress
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'show_translation' not in st.session_state:
    st.session_state.show_translation = False
if 'question_language' not in st.session_state:
    st.session_state.question_language = 'German'
if 'answer_language' not in st.session_state:
    st.session_state.answer_language = 'English'
if 'shuffled_data' not in st.session_state:
    st.session_state['shuffled_data'] = data

# Sidebar for language selection
st.sidebar.header("Select Languages")
languages = ['German', 'English', 'Swedish']
st.session_state.question_language = st.sidebar.selectbox("Question Language", languages, index=0)
st.session_state.answer_language = st.sidebar.selectbox("Answer Language", languages, index=1)

# Get the current flashcard
def get_flashcard():
    index = st.session_state.current_index
    shuffled_data = st.session_state.get('shuffled_data', data)
    if index >= len(shuffled_data):
        st.session_state.current_index = 0
        index = 0
    return shuffled_data.iloc[index]

flashcard = get_flashcard()

# Display the flashcard
st.title("Multilingual Flashcards")
question = flashcard[st.session_state.question_language]
answer = flashcard[st.session_state.answer_language]

st.subheader(question)

if st.session_state.show_translation:
    st.write(f"**Translation:** {answer}")

# Buttons for interaction
col1, col2 = st.columns(2)

if col1.button("Show Translation"):
    st.session_state.show_translation = True

if col2.button("Next Flashcard"):
    st.session_state.current_index += 1
    st.session_state.show_translation = False

# Progress tracking
st.sidebar.write(f"Progress: {st.session_state.current_index + 1}/{len(data)}")

# Shuffle option
if st.sidebar.button("Shuffle Flashcards"):
    st.session_state.current_index = 0
    st.session_state['shuffled_data'] = data.sample(frac=1).reset_index(drop=True)
