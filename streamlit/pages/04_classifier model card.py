import streamlit as st
from PIL import Image

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

st.title("Classification Model Evaluation")

st.header("Introduction")
st.markdown("""
This model is designed to identify medical conditions using the Raabin Health Database. It was trained using transfer learning from ResNet-34 with the fastai library. The training data is sourced from the [Raabin Health Database](https://raabindata.com/raabin-health-database/), which provides a comprehensive collection of medical images for research and development purposes. The dataset used for training can be accessed from the [Raabin Health Database Free Data](https://raabindata.com/free-data/) section.

The model architecture leverages transfer learning to adapt a pre-trained ResNet-34 backbone for medical image classification tasks. This approach enables the model to achieve high accuracy and generalization on medical image datasets.

While the model demonstrates strong performance during training and validation, its real-world efficacy may vary depending on factors such as image quality, lighting conditions, and the diversity of medical conditions present in the dataset.
The model is hosted on [Hugging Face](https://huggingface.co/MKnaepen/WBC_Identifier/tree/main)
            """)

st.header("Confusion Matrix")
st.image('streamlit/images/output.png')
st.markdown("""
The classification matrix shows that the model is very accurate on all ttypes of white blood cells. There is a minor underperformance on monocytes, where 15 out of 107 are mistakenly identified as lymphocytes.""")

st.header('Training details')
st.markdown(""" The Notebook used to train the model can be accessed [here](https://colab.research.google.com/drive/1m6lK-ZluFWjJTObO40so-A9BoW4J7ixR?usp=sharing)""")

st.header("Conclusion")
st.markdown("""
In conclusion, the identification model trained on the Raabin Health Database demonstrates promising performance in medical condition classification tasks. Leveraging transfer learning from ResNet-34 and utilizing the fastai library, the model achieves high accuracy and generalization on diverse medical image datasets. However, continuous evaluation and refinement are essential to enhance the model's robustness and applicability in real-world healthcare settings.
""")

