import joblib
import numpy as np

strength_model = joblib.load("models/strength.pkl")
cycle_model = joblib.load("models/cycle.pkl")

def optimize_cycle(input_data):

    best_result = None
    min_cycle = 9999

    for curing_time in range(12, 48, 2):

        test = input_data.copy()
        test[4] = curing_time

        strength = float(
            strength_model.predict([test])[0]
        )

        cycle = float(
            cycle_model.predict([test])[0]
        )

        if strength > 30 and cycle < min_cycle:
            min_cycle = cycle

            best_result = {
                "curing_time": int(curing_time),
                "pred_strength": strength,
                "cycle_time": cycle
            }

    return best_result