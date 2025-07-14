import sys
import os
from signLanguage.pipeline.training_pipeline import TrainPipeline
from signLanguage.exception import SignException
from signLanguage.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template, Response
from flask_cors import CORS, cross_origin
from signLanguage.constant.application import APP_HOST, APP_PORT

# Instantiate ClientApp globally so it's available for routes
class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"

clApp = ClientApp() # Instantiate ClientApp here

app = Flask(__name__)
CORS(app)

@app.route("/train")
def trainRoute():
    """
    Route to trigger the training pipeline.
    Initializes and runs the TrainPipeline.
    """
    try:
        obj = TrainPipeline()
        obj.run_pipeline()
        return "Training Successful!!"
    except Exception as e:
        print(f"Error during training: {e}")
        return Response(f"Training failed: {e}", status=500)

@app.route("/")
def home():
    """
    Home route that renders the index.html template.
    """
    return render_template("index.html")

@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    """
    Prediction route that takes an image, performs sign language detection,
    and returns the processed image.
    """
    try:
        # Get image from JSON request and decode it
        image = request.json['image']
        decodeImage(image, clApp.filename)

        # Run YOLOv5 detection
        # IMPORTANT: We specify a fixed output directory using --project and --name
        # and use --exist-ok to overwrite previous runs in that folder.
        # This ensures the output image is always in a predictable location.
        os.system(f"cd yolov5/ && python detect.py --weights my_model.pt --img 416 --conf 0.5 --source ../data/{clApp.filename} --project runs/detect_output --name current_run --exist-ok")

        # Encode the processed image from the fixed output location
        # The path must match the --project and --name flags used above
        output_image_path = f"yolov5/runs/detect_output/current_run/{clApp.filename}"
        opencodedbase64 = encodeImageIntoBase64(output_image_path)

        # Return the encoded image as JSON
        result = {"image": opencodedbase64.decode('utf-8')}

        # Optional: Clean up the specific output folder if desired,
        # but ensure it's done AFTER the image is encoded and sent.
        # For now, commented out to ensure the file exists for debugging.
        # os.system("rm -rf yolov5/runs/detect_output")

    except ValueError as val:
        print(f"ValueError in predictRoute: {val}")
        return Response("Value not found inside json data", status=400)
    except KeyError as ke:
        print(f"KeyError in predictRoute: {ke}")
        return Response("Key value error: incorrect key passed", status=400)
    except Exception as e:
        print(f"An unexpected error occurred in predictRoute: {e}")
        # Log the full traceback for better debugging in a real application
        # import traceback
        # traceback.print_exc()
        return Response(f"An error occurred during prediction: {e}", status=500)

    return jsonify(result)

@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    """
    Route to start live webcam detection.
    Note: This will open a new window for the webcam feed.
    """
    try:
        # Source 0 typically means webcam.
        # The output of this is usually a live window, not a saved file.
        os.system("cd yolov5/ && python detect.py --weights my_model.pt --img 416 --conf 0.5 --source 0")
        # No need to remove 'runs' here as live feed doesn't necessarily save to it
        # os.system("rm -rf yolov5/runs")
        return "Camera starting!!"
    except ValueError as val:
        print(f"ValueError in predictLive: {val}")
        return Response("Value not found inside json data", status=400)
    except Exception as e:
        print(f"An unexpected error occurred in predictLive: {e}")
        return Response(f"An error occurred during live prediction: {e}", status=500)

if __name__ == "__main__":
    # Ensure APP_HOST and APP_PORT are correctly defined in signLanguage.constant.application
    # For local testing, you can hardcode them if needed:
    # APP_HOST = '0.0.0.0'
    # APP_PORT = 5000
    app.run(host=APP_HOST, port=APP_PORT)

