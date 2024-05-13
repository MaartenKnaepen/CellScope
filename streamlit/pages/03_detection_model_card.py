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

st.title("Detection Model Evaluation")

st.header("Introduction")
st.markdown("""
This model is designed to detect white blood cells in images. It has been trained using a dataset available at [Roboflow Universe](https://universe.roboflow.com/trst1/wbcc-ezrfu), which contains annotated images of white blood cells. 

The architecture is the YOLOV8 model that has been trained on the dataset mentioned earlier. The model is trained for 100 epochs. It performs well across different white blood cell types, with some misclassifications across cell types as background. The model's performance is consistent across different metrics, indicating that the model is not overfitting to the training data.

While the model performs very well on validation data, its real-world performance may vary. The model may struggle with images that are not well-lit, have poor contrast, or are taken at an angle. The model may also struggle with images that contain other objects that are similar in shape to white blood cells such as lymphoblasts or myeloblasts.
The model is hosted on [Hugging Face](https://huggingface.co/MKnaepen/WBC_detector/tree/main).
            """)

st.header("Confusion Matrix")
st.image('streamlit\images\confusion_matrix_normalized.png')
st.markdown("""
This confusion matrix highlights the model's strong performance in classifying basophils (14/15), neutrophils (105/108), eosinophils (74/80), lymphocytes (40/45), and monocytes (40/46). 
Some misclassifications across cell types as background still occur. 
            While excelling at most white blood cell types, further reducing these background misclassifications could enhance overall accuracy.
""")

st.header("Precision-Recall Curve")
st.image('streamlit\images\PR_curve.png')
st.markdown("""
The precision-recall curve shows the trade-off between precision and recall for the model. The model performs well, with an average precision of 0.95. 
The curve is close to the top right corner, indicating high precision and recall across the classes.
""")

st.header("F1-Curve")
st.image('streamlit\images\F1_curve.png')
st.markdown("""
The F1 curve shows the F1 score for the model across different confidence points. 
            The model performs well with an F1-score  of approximately 90% for confidence values from 0.1 to 0.9. 
            The F1 score is a good metric for evaluating the model's performance across different confidence thresholds.
""")

st.header("Loss functions")
st.image("streamlit\images/results.png")
st.markdown("""
This graph shows that validation losses for multiple metrics converge after approximately 50 epochs. 
            The model's performance is consistent across different metrics, indicating that the model is not overfitting to the training data.
""")

st.header("Labels and boxes")
st.image("streamlit\images\labels.jpg")
st.markdown("""
The top left graph shows the distribution between different labels. 
The top right graph shows the size and shape of the detected bounding boxes. 
The bottom left graph shows the center of each bounding box, confirming that for most training data the white blood cell is in the center of the image. 
The bottom right graph shows the correlation between the width and height of the bounding boxes.
""")

st.header('Training details')
st.text('The training notebook can be accessed [here](https://colab.research.google.com/drive/1CcoAmnvPGAGVo1iLJCXdU6SahAA-NbzU?usp=sharing).')

st.header("Architecture")
st.markdown('This is a visual representation of the model architecture.')
st.image('streamlit/images/architecture.png')