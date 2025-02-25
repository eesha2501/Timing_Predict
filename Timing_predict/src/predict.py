import joblib
import pandas as pd
import argparse

def predict_logic_depth(model_path, features_path):
    model = joblib.load(model_path)
    features = pd.read_csv(features_path)
    return model.predict(features)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="model/rf_model.pkl", help="Path to model")
    parser.add_argument("--features", default="data/features.csv", help="Path to features")
    args = parser.parse_args()

    predictions = predict_logic_depth(args.model, args.features)
    print(f"Predicted Logic Depth: {predictions}")

if __name__ == "__main__":
    main()