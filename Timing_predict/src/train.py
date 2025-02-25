import pandas as pd
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_absolute_error
import joblib
import argparse

def load_data(data_path):
    """Load dataset with gate_path_count."""
    try:
        data = pd.read_csv(data_path)
        X = data[["fan_in", "fan_out", "gate_path_count", "arithmetic_ops", "conditional_nesting"]]
        y = data["logic_depth"]
        return X, y
    except Exception as e:
        print(f"Data Loading Error: {e}")
        raise

def train_model(X_train, y_train):
    """Train with dynamic cross-validation."""
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [10, 20],
        'min_samples_split': [2, 5]
    }
    n_samples = len(X_train)
    n_folds = min(5, n_samples)
    
    grid_search = GridSearchCV(
        RandomForestRegressor(),
        param_grid,
        cv=n_folds,
        scoring='neg_mean_absolute_error'
    )
    grid_search.fit(X_train, y_train)
    print(f"Best Parameters: {grid_search.best_params_}")
    return grid_search.best_estimator_

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_path", default="data/sample_dataset.csv", help="Path to dataset")
    args = parser.parse_args()

    X, y = load_data(args.data_path)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    model = train_model(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"MAE: {mean_absolute_error(y_test, y_pred):.2f}")
    joblib.dump(model, "model/rf_model.pkl")

if __name__ == "__main__":
    main()