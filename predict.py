import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.losses import MeanSquaredError
from joblib import load

# File paths
INPUT_FILE = 'input.csv'
MODEL_FILE = 'model.h5'
SCALER_X_FILE = 'scaler_X.joblib'
SCALER_Y_FILE = 'scaler_y.joblib'
OUTPUT_FILE = 'output.csv'

try:
    # Load the data
    print("Loading input data...")
    data = pd.read_csv(INPUT_FILE)

    # Extract input features (first 8 columns)
    X = data.iloc[:, :8]

    # Load the saved scalers
    print("Loading scalers...")
    scaler_X = load(SCALER_X_FILE)
    scaler_y = load(SCALER_Y_FILE)

    # Normalize the input data
    print("Normalizing input data...")
    X_normalized = scaler_X.transform(X)

    # Load the trained neural network model
    print("Loading model...")
    model = load_model(MODEL_FILE, custom_objects={'mse': MeanSquaredError()})

    # Make predictions using the model
    print("Making predictions...")
    y_pred_normalized = model.predict(X_normalized)
    y_pred_unnormalized = scaler_y.inverse_transform(y_pred_normalized)

    # Combine predictions and input values into a DataFrame
    predicted_df = pd.DataFrame(
        np.hstack((X, y_pred_unnormalized)),
        columns=list(X.columns) + ['a_predicted', 'b_predicted']
    )

    # Convert first 8 columns to integers (if applicable)
    for col in predicted_df.columns[:8]:
        predicted_df[col] = predicted_df[col].astype(int)

    # Save predicted values to CSV
    print(f"Saving predictions to {OUTPUT_FILE}...")
    predicted_df.to_csv(OUTPUT_FILE, index=False)

    print("Prediction process completed successfully!")

except FileNotFoundError as e:
    print(f"Error: {e}. Please check that all required files exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")


