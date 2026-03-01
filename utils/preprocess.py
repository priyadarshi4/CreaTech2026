import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path):
    df = pd.read_csv(path)

    X = df.drop(["strength","cycle_time","cost"], axis=1)
    y_strength = df["strength"]
    y_cycle = df["cycle_time"]

    return train_test_split(
        X, y_strength, y_cycle,
        test_size=0.2,
        random_state=42
    )