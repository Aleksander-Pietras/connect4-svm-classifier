from pathlib import Path

import pandas as pd
import numpy as np

import csv


def load_dataset(filename: str) -> pd.DataFrame:
    # Build absolute path starting from this script's folder
    current_script = Path(__file__).resolve()
    project_root = current_script.parent.parent
    file_path = project_root / "dataset_connect4" / filename
    
    if not file_path.exists():
        raise FileNotFoundError(f"Could not find dataset at: {file_path}")
    
    df = pd.read_csv(file_path)
    return df

# Main execution block
if __name__ == "__main__":
    # Load dataset
    data = load_dataset("connect-4_training.csv")
    
    # Inspect the structure
    print("--- First 5 Rows ---")
    print(data.head())
    
    print("\n--- Data Summary ---")
    print(data.info())