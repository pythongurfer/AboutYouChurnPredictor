# tests/test_predict.py
import pytest
import numpy as np

# Let's assume you have a function to test in app/predict.py.
# If not, you can create a simple one like this for the test to pass.
# from app.predict import make_prediction 

# For this example, we'll define a dummy function to test against.
def dummy_prediction_logic(data):
    """A dummy function that returns 1 if a value is high, else 0."""
    if data['monthly_charge'] > 100:
        return np.array([1])
    return np.array([0])

def test_high_charge_returns_churn():
    """Tests if a high monthly charge correctly predicts churn (1)."""
    sample_data = {'monthly_charge': 120}
    prediction = dummy_prediction_logic(sample_data)
    assert prediction[0] == 1

def test_low_charge_returns_no_churn():
    """Tests if a low monthly charge correctly predicts no churn (0)."""
    sample_data = {'monthly_charge': 50}
    prediction = dummy_prediction_logic(sample_data)
    assert prediction[0] == 0

def test_prediction_output_is_numpy_array():
    """Tests if the output type is a numpy array."""
    sample_data = {'monthly_charge': 50}
    prediction = dummy_prediction_logic(sample_data)
    assert isinstance(prediction, np.ndarray)