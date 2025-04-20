from flask import Blueprint, request, jsonify
import pickle
import numpy as np
from .database import db

predict_bp = Blueprint('predict', __name__)

# Load the model once
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@predict_bp.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    try:
        # Extract and format features (assuming 14 features)
        features = [
            float(data[f'feature{i+1}']) for i in range(14)  # Ensure you're passing the correct number of features
        ]
        input_data = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_data)[0]  # Directly using the model to predict

        # Interpret result
        result = "High possibility of heart disease" if prediction <= 0.5 else "Low possibility of heart disease"

        return jsonify({
            'prediction_score': float(prediction),
            'result': result
        }), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400
