import streamlit as st
from wbc_helper import WBC_Helper
from PIL import Image

# Create an instance of WBC_Helper
helper = WBC_Helper()

# Load the models
detector = WBC_Helper.load_model("MKnaepen/WBC_detector", "main", 'best_detector.pt','yolo')
identifier = WBC_Helper.load_model("MKnaepen/WBC_identifier", "main", 'wbc_classifier1.pkl','fastai')
st.markdown("""If you don't have a peripheral blood smear image, you can drag and drop one from [these search results](https://www.google.com/search?q=peripheral+blood+smear+white+blood+cell&sca_esv=f42f57a008774f06&sca_upv=1&rlz=1C1GCEA_enBE1092BE1092&udm=2&biw=1280&bih=656&sxsrf=ADLYWILw3mCT1g46EPAlkzmTxXvpfFqwEw%3A1715355769874&ei=eUA-ZvT3NIiG9u8PlPaW0Ak&ved=0ahUKEwi0mM6atoOGAxUIg_0HHRS7BZoQ4dUDCBA&uact=5&oq=peripheral+blood+smear+white+blood+cell&gs_lp=Egxnd3Mtd2l6LXNlcnAiJ3BlcmlwaGVyYWwgYmxvb2Qgc21lYXIgd2hpdGUgYmxvb2QgY2VsbDIGEAAYCBgeSNQhULwIWIsgcAF4AJABAJgBZaABgAuqAQQxNi4xuAEDyAEA-AEBmAISoAKVC8ICBBAjGCfCAgUQABiABMICChAAGIAEGEMYigXCAgcQABiABBgYmAMAiAYBkgcEMTcuMaAH8iI&sclient=gws-wiz-serp).""")
st.markdown(""" or try this image!""")
st.image('streamlit/images/test.png', caption='Test Image')
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image')

if st.button('Detect'):
    if uploaded_file is None:
        st.error('Please upload an image before detection.')
    else:
        detected_image, results = helper.detect(image, detector)
        st.image(detected_image, caption='Detected Image')

        # Crop the detected cells
        cropped_images = helper.crop_boxes(image, results)

        # Display each cropped image along with its inference
        helper.display_box_and_inference(cropped_images, identifier)