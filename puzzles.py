import streamlit as st

def show_puzzle():
    st.header("Puzzle 1: The Static Code")
    st.write("You encounter a distorted radio broadcast. The static seems to contain a hidden message. Can you decode it?")
    st.text_input("Enter the decoded message:")
