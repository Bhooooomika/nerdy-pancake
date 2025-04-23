import streamlit as st
from PIL import Image

def show_visuals():
    st.header("Visuals: A Glimpse into the Unknown")
    image = Image.open("assets/haunted_radio.jpg")  # Add an image of a haunted radio later
    st.image(image, caption="A flickering, haunted radio station")
