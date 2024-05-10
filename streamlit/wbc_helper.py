from huggingface_hub import snapshot_download
import streamlit as st
from ultralytics import YOLO
from PIL import Image
from fastai.vision.all import *
import os
import cv2
import numpy as np

class WBC_Helper:
    @staticmethod
    @st.cache_data()
    def load_model(repo_id, revision, name, model_type):
        model_path = snapshot_download(repo_id, revision=revision)
        model_file = os.path.join(model_path, name)
        
        if model_type.lower() == 'yolo':
            model = YOLO(model_file)
        elif model_type.lower() == 'fastai':
            model = load_learner(model_file)
        else:
            raise ValueError("Invalid model_type. Expected 'yolo' or 'fastai'")
        
        return model

    

    def detect(self, image, model):
        results = model.predict(source=image, hide_labels=True, hide_conf=True, conf=0.4, show=True)
        return results[0].plot(),results
        

    def crop_boxes(self, image, results):
        # Convert PIL Image to OpenCV format
        image = np.array(image)
        
        # Process each result
        cropped_images = []
        for result in results:
            obb = result.obb  # Oriented boxes object for OBB outputs
            point = result.obb.xywhr.tolist()

            for ob in point:
                xc, yc, w, h, angle = ob  # Unpack the OBB

                # Get rotation matrix for the given angle
                center = (int(xc), int(yc))
                M = cv2.getRotationMatrix2D(center, angle, 1.0)

                # Apply affine transformation - rotating the image
                rotated = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]), flags=cv2.INTER_LINEAR)

                # Create a rectangle enclosing the rotated license plate
                rect = ((xc, yc), (h, w), angle)  # swapping w and h
                box = cv2.boxPoints(rect)
                box = box.astype(np.int32)

                # Get the rotated bounding box coordinates
                x1, y1 = np.min(box, axis=0)
                x2, y2 = np.max(box, axis=0)

                # Crop the rotated image
                crop = rotated[y1:y2, x1:x2]
                cropped_images.append(crop)
        
        return cropped_images

    def display_prediction(self, prediction):
        # Define the class names
        class_names = ['basophil','eosinophil','lymphocyte','monocyte','neutrophil']

        # Convert the probabilities tensor to a list
        probabilities = prediction[2].tolist()

        # Convert the probabilities to percentages
        probabilities = [p * 100 for p in probabilities]

        # Create a DataFrame
        df = pd.DataFrame({
            'Class Name': class_names,
            'Probability (%)': probabilities
        })
        # Sort the DataFrame by probability in descending order
        df = df.sort_values('Probability (%)', ascending=False).reset_index(drop=True)
        # Return the DataFrame
        return f'Prediction for image: {prediction[0]}',df

    def display_box_and_inference(self, cropped_images, identifier):
        for i, crop in enumerate(cropped_images):
            # Skip if the crop is empty
            if crop.size == 0:
                continue

            try:
                # Convert OpenCV image to PIL format for display
                pil_image = Image.fromarray(crop)
                st.image(pil_image, caption=f'Cropped Image {i+1}')

                # Run inference on the cropped image
                prediction = identifier.predict(crop)
                df = self.display_prediction(prediction)

                # Display the DataFrame
                st.write(f'Prediction for Image {i+1}')
                st.table(df[1])
            except Exception as e:
                st.error(f'Error processing Image {i+1}: {str(e)}')