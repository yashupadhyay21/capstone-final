from flask import Blueprint, request, render_template
from flask_login import login_required, current_user
import pickle
import numpy as np
from .database import db, User

predict_bp = Blueprint('predict', __name__)

# Load the model once
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Route for the prediction page (accessible only after login)
@predict_bp.route('/predict', methods=['GET', 'POST'])
@login_required
def predict_page():
    if request.method == 'POST':
        data = request.form
        features = [float(data[f'feature{i+1}']) for i in range(14)]  # Extracting features from the form

        input_data = np.array(features).reshape(1, -1)
        prediction = model.predict(input_data)[0]  # Make prediction
        result = "High possibility of heart disease" if prediction <= 0.5 else "Low possibility of heart disease"

        # ✅ Update current logged-in user's prediction data
        current_user.prediction_score = float(prediction)
        current_user.prediction_result = result
        db.session.commit()

        return render_template('predict.html', prediction_score=prediction, result=result)
    
    return render_template('predict.html')
