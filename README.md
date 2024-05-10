# CellScope

CellScope is a project aimed at facilitating the identification and analysis of white blood cells in peripheral blood smear images using machine learning techniques. The project offers a streamlined interface for users to upload images, detect white blood cells, and classify them into different types.

## Features

- **White Blood Cell Detection**: Utilizes object detection models (such as YOLO) to detect white blood cells in uploaded images.
  
- **White Blood Cell Identification**: Employs classification models (such as fastai) to identify different types of white blood cells, including basophils, eosinophils, lymphocytes, monocytes, and neutrophils.

- **Model Evaluation**: Provides comprehensive evaluation metrics, including confusion matrices, precision-recall curves, F1 curves, and training details, to assess the performance of both detection and classification models.

## Getting Started

To get started with CellScope, follow these steps:

1. **Clone the Repository**: Clone the CellScope repository to your local machine:
   ```
   git clone https://github.com/your-username/CellScope.git
   ```

2. **Install Dependencies**: Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**: Launch the Streamlit application by running:
   ```
   streamlit run app.py
   ```

4. **Upload Images**: Upload peripheral blood smear images to the application using the provided interface.

5. **Detection and Identification**: Click the "Detect" button to initiate the white blood cell detection process. Once the detection is complete, the detected cells will be displayed along with their classifications.

6. **Evaluate Models**: Explore the evaluation metrics provided in the application to assess the performance of the detection and classification models.

## Model Repositories

- Detection Model: [Hugging Face Model Hub](https://huggingface.co/models)
  
- Identification Model: [Hugging Face Model Hub](https://huggingface.co/models)

## Contributing

Contributions to CellScope are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
