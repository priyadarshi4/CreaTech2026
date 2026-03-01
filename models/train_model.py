import joblib
from xgboost import XGBRegressor
from utils.preprocess import load_data

X_train, X_test, y_s_train, y_s_test, y_c_train, y_c_test = \
    load_data("data/precast_data.csv")

# Strength Prediction Model
strength_model = XGBRegressor()
strength_model.fit(X_train, y_s_train)

# Cycle Time Prediction Model
cycle_model = XGBRegressor()
cycle_model.fit(X_train, y_c_train)

joblib.dump(strength_model, "models/strength.pkl")
joblib.dump(cycle_model, "models/cycle.pkl")

print("✅ Models Trained Successfully")