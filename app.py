import io
import numpy as np
from PIL import Image
from flask import Flask, jsonify, request
from tensorflow.keras.models import load_model
import cv2

# Load the trained model
model = load_model('KCModel')

# Define the Flask app
app = Flask(__name__)

# Define the API route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the image file from the request
    image_file = request.files['image']

    # Read the image file and convert it to a PIL Image object
    image_bytes = io.BytesIO(image_file.read())
    image = Image.open(image_bytes)

    # Convert the PIL Image object to a numpy array
    img_array = np.array(image)

    # Preprocess the image (resize and normalize)
    img_array = cv2.resize(img_array, (224, 224))
    img_array = img_array.astype('float32') / 255.0

    # Add a batch dimension to the image
    img_array = np.expand_dims(img_array, axis=0)

    # Make a prediction using the model
    prediction = model.predict(img_array)

    # Get the predicted label (category)
    predicted_label = np.argmax(prediction, axis=1)[0]

    # Define the class labels
    class_labels = {0: 'Bed', 1: 'Chair', 2: 'Sofa'}

    # Return the predicted label as a JSON object
    response = {'predicted_label': class_labels[predicted_label]}
    return jsonify(response)

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
