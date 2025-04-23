import streamlit as st
from narrative import display_intro
from puzzles import show_puzzle
from visuals import show_visuals

def main():
    st.title("Frequency 333: The Ossuary of Echoes")
    display_intro()
    show_puzzle()
    show_visuals()

if __name__ == "__main__":
    main()
