🚀 End-to-End Sign Language Detection with YOLOv5 and Flask
✨ Introduction
This project presents an end-to-end solution for real-time sign language detection. It leverages the powerful YOLOv5 (You Only Look Once, version 5) object detection model for accurate identification of hand gestures, integrated with a Flask web application to provide a user-friendly interface. Users can upload images for prediction or utilize a live webcam feed for continuous, dynamic detection.

The goal is to offer an accessible and efficient tool for interpreting sign language gestures, paving the way for improved communication and accessibility.

🌟 Features
Image-based Prediction: Upload an image containing a sign language gesture and receive bounding box detections.

Live Webcam Detection: Utilize your webcam for real-time sign language gesture recognition.

Flask Web Interface: A simple and intuitive web application for easy interaction.

YOLOv5 Integration: Powered by a pre-trained or custom-trained YOLOv5 model for robust detection.

Modular Design: Organized project structure for clarity and maintainability.

🎥 Demo
## Demo Video

[![Sign Language Detection Demo](https://drive.google.com/file/d/1jS3phNoqFMT2QoiqX-lX_PUZ2155heCi/view?usp=sharing)

*Click the image above to watch the demo!*

---

📂 Project Structure
.
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies for the project
├── .gitignore                  # Specifies intentionally untracked files to ignore
├── README.md                   # This file!
├── signLanguage/               # Core project logic
│   ├── __init__.py             # Makes 'signLanguage' a Python package
│   ├── pipeline/               # Training pipeline (if implemented)
│   │   ├── __init__.py
│   │   └── training_pipeline.py
│   └── utils/                  # Utility functions (e.g., image encoding/decoding)
│       ├── __init__.py
│       └── main_utils.py
├── data/                       # Contains input images (e.g., inputImage.jpg)
│   └── inputImage.jpg
├── yolov5/                     # Cloned YOLOv5 repository (or relevant parts)
│   ├── detect.py               # YOLOv5 detection script
│   ├── models/                 # YOLOv5 model definitions
│   │   └── common.py
│   │   └── experimental.py
│   └── runs/                   # YOLOv5 output directory (will be created)
│       └── detect_output/      # Custom output folder for web app predictions
│           └── current_run/    # Fixed name for the latest detection
│               └── inputImage.jpg
└── my_model.pt                 # Your trained YOLOv5 model weights (or link to download)

⚙️ Prerequisites
Before you begin, ensure you have the following installed:

Python 3.9: It's highly recommended to use Python 3.9 for compatibility with all dependencies.

Conda (Anaconda or Miniconda): For managing virtual environments and packages.

Download Miniconda

🚀 Installation
Follow these steps to set up the project locally:

Clone the repository:

git clone https://github.com/VASIREDDYSRINIKETH/Sign-Language-Detection-YOLOv5.git
cd Sign-Language-Detection-YOLOv5

Create and activate a Conda environment:

conda create -n sign-dec python=3.9 -y
conda activate sign-dec

Configure Pip for Proxy (if applicable):
If you are behind a corporate or institutional proxy, you might need to configure pip to use it.

Set environment variables (for current session):

$env:HTTP_PROXY="http://127.0.0.1:51769" # Replace with your actual proxy address and port
$env:HTTPS_PROXY="http://127.0.0.1:51769" # Replace with your actual proxy address and port

Or, configure pip.ini for persistent proxy settings:
Create a file C:\Users\YOUR_USERNAME\pip\pip.ini (replace YOUR_USERNAME) and add:

[global]
proxy = http://127.0.0.1:51769 # Replace with your actual proxy address and port
trusted-host = pypi.org
               files.pythonhosted.org

Install project dependencies:
First, install Flask and Flask-Cors, which are used by app.py but not explicitly in requirements.txt:

pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org Flask Flask-Cors

Then, install all other dependencies from requirements.txt:

pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org -r requirements.txt

Download the YOLOv5 Model Weights:

If my_model.pt is not in the repository (due to size limits), you will need to download it separately and place it in your project's root directory.

Download my_model.pt from: [YOUR_YOLOV5_MODEL_DOWNLOAD_LINK_HERE]

Place the downloaded my_model.pt file in the End-to-end-Sign-Language-Detection folder.

🏃 Usage
Running the Flask Application
Ensure your sign-dec Conda environment is active.

Start the Flask server:

python app.py

The server will start and typically run on http://127.0.0.1:5000/ (or the port defined in signLanguage/constant/application.py). You will see output similar to:

 * Serving Flask app 'app'
 * Debug mode: off

The terminal will remain active as the server is running.

Accessing the Web Interface
Open your web browser and navigate to http://127.0.0.1:5000/ (or the appropriate host and port).

For Image Prediction: Use the provided interface to upload an image. The processed image with detections will be displayed.

For Live Webcam Detection: Click the "Live" button (or navigate to /live if implemented) to start the webcam feed. A new window showing the live detection will appear.

API Endpoints
/ (GET): Renders the index.html page.

/predict (POST):

Method: POST

Content-Type: application/json

Body: {"image": "base64_encoded_image_string"}

Returns: JSON object {"image": "base64_encoded_output_image_string"}

/live (GET): Triggers the live webcam detection. Returns a simple message.

/train (GET): Triggers the model training pipeline. Returns a success message or error.

🤝 Contributing
Contributions are welcome! If you have suggestions for improvements, bug fixes, or new features, please feel free to:

Fork the repository.

Create a new branch (git checkout -b feature/your-feature-name).

Make your changes.

Commit your changes (git commit -m 'Add new feature').

Push to your branch (git push origin feature/your-feature-name).

Open a Pull Request.

📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

🙏 Acknowledgements
YOLOv5: The core object detection framework by Ultralytics.

Flask: The micro web framework used for the application.

Original Project Source (if forked/adapted): If this project is an adaptation or fork, consider linking to the original source here (e.g., "Inspired by [Original Author/Project Name](Link to original repo)").