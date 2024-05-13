import streamlit as st
from PIL import Image
from pathlib import Path

# Load the image for the page icon
page_icon_image = Image.open('streamlit/images/logo.jpg')

# Configure Streamlit page settings
st.set_page_config(
    page_title="Hello!",
    page_icon=page_icon_image,
)

# Hide default Streamlit format for cleaner UI
hide_default_format = """
       <style>
       #MainMenu {visibility: hidden; }
       footer {visibility: hidden;}
       </style>
       """
st.markdown(hide_default_format, unsafe_allow_html=True)

# Display header text
st.write("# Welcome to CellScope:")
st.write("# AI-Powered Blood Cell Identification")


# Display introduction text
st.markdown(
    """
Welcome to our platform for analyzing peripheral blood smears! 
Our tool employs cutting-edge machine learning to swiftly detect and identify white blood cells in uploaded images. 
Say goodbye to manual analysis and hello to efficient, accurate results. 
Whether you're a healthcare professional or a researcher, our user-friendly interface offers a seamless solution for blood cell analysis.

Each model comes with its own dedicated model card, providing detailed insights into its performance and capabilities. 
Simply upload your image, select a model, and click the detect button to see the output."""
)


