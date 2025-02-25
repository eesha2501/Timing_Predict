import pandas as pd

def load_synthetic_data():
    """Generate synthetic dataset for testing."""
    data = {
        "fan_in": [2, 4, 3, 5],
        "fan_out": [1, 2, 1, 3],
        "num_gates": [5, 10, 8, 15],
        "arithmetic_ops": [0, 1, 0, 2],
        "conditional_nesting": [1, 3, 2, 4],
        "logic_depth": [3, 7, 5, 10]
    }
    return pd.DataFrame(data)