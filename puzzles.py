import streamlit as st

def show_puzzle():
    st.header("Puzzle 1: The Static Code")
    st.write("You encounter a distorted radio broadcast. The static seems to contain a hidden message. Can you decode it?")
    
    correct_answer = "echoes"
    user_input = st.text_input("Enter the decoded message:")

    if user_input.lower() == correct_answer:
        st.success("Correct! You've decoded the message.")
    elif user_input:
        st.error("Incorrect. Try again.")
