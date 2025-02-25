import argparse
import pandas as pd
import os
from pyverilog.vparser.parser import parse

def count_gate_path(ast):
    """Count logic gates in the design (simplified example)."""
    gate_count = 0
    for node in ast.children():
        # Detect basic gates (customize based on your needs)
        if "Add" in str(node) or "And" in str(node) or "Or" in str(node):
            gate_count += 1
    return gate_count

def parse_rtl(rtl_path):
    """Extract features from RTL file."""
    try:
        if not os.path.exists(rtl_path):
            raise FileNotFoundError(f"File {rtl_path} not found!")
        
        ast, _ = parse([rtl_path])
        features = {
            "fan_in": 2,  # Replace with actual parsing
            "fan_out": 1,  
            "gate_path_count": count_gate_path(ast),
            "arithmetic_ops": 1,
            "conditional_nesting": 0
        }
        return pd.DataFrame([features])
    except Exception as e:
        print(f"RTL Parsing Error: {e}")
        raise

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to RTL file")
    parser.add_argument("--output", default="data/features.csv", help="Path to output CSV")
    args = parser.parse_args()

    features_df = parse_rtl(args.input)
    features_df.to_csv(args.output, index=False)
    print(f"Features saved to {args.output}")

if __name__ == "__main__":
    main()