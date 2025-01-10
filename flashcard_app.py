import streamlit as st
import pandas as pd
import random

# Load the flashcard data
@st.cache_data
def load_data():
    return pd.read_csv('Swedish_German_Flashcards.csv')

data = load_data()

# Initialize session state for tracking progress
if 'current_index' not in st.session_state:
    st.session_state.current_index = 0
if 'show_translation' not in st.session_state:
    st.session_state.show_translation = False
if 'category_filter' not in st.session_state:
    st.session_state.category_filter = 'All'
if 'shuffled_data' not in st.session_state:
    st.session_state['shuffled_data'] = data

# Sidebar for filtering
st.sidebar.header("Filter by Category")
categories = ['All'] + sorted(data['Category'].unique())
st.session_state.category_filter = st.sidebar.selectbox("Choose a category", categories)

# Filter data by selected category
filtered_data = data if st.session_state.category_filter == 'All' else data[data['Category'] == st.session_state.category_filter]
st.session_state['shuffled_data'] = filtered_data

# Get the current flashcard
def get_flashcard():
    index = st.session_state.current_index
    shuffled_data = st.session_state.get('shuffled_data', filtered_data)
    if index >= len(shuffled_data):
        st.session_state.current_index = 0
        index = 0
    return shuffled_data.iloc[index]

flashcard = get_flashcard()

# Display the flashcard
st.title("Swedish-German Flashcards")
st.write(f"**Category:** {flashcard['Category']}")
st.subheader(flashcard['Swedish'])

if st.session_state.show_translation:
    st.write(f"**Translation:** {flashcard['German']}")

# Buttons for interaction
col1, col2 = st.columns(2)

if col1.button("Show Translation"):
    st.session_state.show_translation = True

if col2.button("Next Flashcard"):
    st.session_state.current_index += 1
    st.session_state.show_translation = False

# Progress tracking
st.sidebar.write(f"Progress: {st.session_state.current_index + 1}/{len(filtered_data)}")

# Shuffle option
if st.sidebar.button("Shuffle Flashcards"):
    st.session_state.current_index = 0
    st.session_state['shuffled_data'] = filtered_data.sample(frac=1).reset_index(drop=True)
