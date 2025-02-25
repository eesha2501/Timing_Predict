import pytest
from src.utils import load_synthetic_data
from src.train import load_data, train_model

def test_model_training():
    """Test if model trains without errors."""
    data = load_synthetic_data()
    data.to_csv("data/test_dataset.csv", index=False)
    X, y = load_data("data/test_dataset.csv")
    model = train_model(X, y)
    assert model is not None