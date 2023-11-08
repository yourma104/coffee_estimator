# my_app/ml_utils.py
import pickle
from pathlib import Path

def load_model():
    # Construct a path to the pickle file.
    model_path = Path(__file__).resolve().parent / "coffee_model3.pkl"
    
    # Check if the model exists.
    if not model_path.exists():
        raise FileNotFoundError(f"Could not find model at {model_path}")
    
    # Load the model from the file.
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    
    return model
