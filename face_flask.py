from flask import Flask, request, jsonify
from flask_cors import CORS
import base64
import cv2
import numpy as np
from PIL import Image
from io import BytesIO
import tensorflow as tf

try:
    active_model = tf.keras.models.load_model('/content/drive/MyDrive/path/to/your/active_model.h5')
    passive_model = tf.keras.models.load_model('/content/drive/MyDrive/path/to/your/passive_model.h5')
    print("Models loaded successfully.")
except Exception as e:
    print(f"Error loading models: {e}")

app = Flask(__name__)
CORS(app)

def preprocess_image(image_data):
    image_data = base64.b64decode(image_data.split(',')[1])
    img = Image.open(BytesIO(image_data))
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img

def prepare_input_for_passive(frame):
    frame_resized = cv2.resize(frame, (224, 224))
    frame_normalized = frame_resized / 255.0
    return np.expand_dims(frame_normalized, axis=0)

def prepare_input_for_active(sequence_of_frames):
    sequence_flattened = [frame.flatten() / 255.0 for frame in sequence_of_frames]
    return np.expand_dims(sequence_flattened, axis=0)

@app.route('/process-frame', methods=['POST'])
def process_frame():
    data = request.get_json()
    image_data = data['image']
    frame = preprocess_image(image_data)
    sequence_of_frames = [frame] * 16

    passive_input = prepare_input_for_passive(frame)
    active_input = prepare_input_for_active(sequence_of_frames)

    try:
        passive_result = passive_model.predict(passive_input)
        active_result = active_model.predict(active_input)

        passive_liveness = "Live" if passive_result[0][0] > 0.5 else "Spoof"
        active_liveness = "Live" if active_result[0][0] > 0.5 else "Spoof"

        if passive_liveness == "Live" and active_liveness == "Live":
            liveness_result = "Live"
        else:
            liveness_result = "Spoof"

    except Exception as e:
        return jsonify({"error": str(e)})

    return jsonify({"result": liveness_result})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
