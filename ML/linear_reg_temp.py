# ============================================================
# ML Practical: Linear Regression on India Temperatures
# Task: Predict month-wise temperature using Linear Regression
# Requirements: pandas, numpy, scikit-learn, matplotlib
# ============================================================

import os                                   # 1
import sys                                  # 2
import numpy as np                          # 3
import pandas as pd                         # 4
import matplotlib.pyplot as plt             # 5
from sklearn.model_selection import train_test_split   # 6
from sklearn.linear_model import LinearRegression       # 7
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score  # 8

# ---------- 1) Load CSV -------------------------------------------------------

CSV_PATH = "temperatures.csv"               # 9

if not os.path.exists(CSV_PATH):            # 10
    sys.exit(f"[Error] File not found: {CSV_PATH}. Put temperatures.csv next to this script and rerun.")  # 11

df_raw = pd.read_csv(CSV_PATH)              # 12
df = df_raw.copy()                          # 13
df.columns = [c.strip().lower() for c in df.columns]  # 14

# ---------- 2) Locate 'month' and 'temperature' columns ----------------------

# Common candidates seen across public datasets
month_candidates = ["month", "mm", "mon", "mnth", "m"]  # 15
temp_candidates  = ["temperature", "temp", "avgtemperature", "avg_temp", "average_temperature", "mean_temp"]  # 16

def find_column(candidates, cols):          # 17
    for name in candidates:                 # 18
        if name in cols:                    # 19
            return name                     # 20
    return None                             # 21

month_col = find_column(month_candidates, set(df.columns))  # 22
temp_col  = find_column(temp_candidates,  set(df.columns))  # 23

# If month is embedded in a date-like column, try to extract it
if month_col is None:                       # 24
    # Look for a date column
    date_like = None                        # 25
    for c in df.columns:                    # 26
        if "date" in c or "time" in c:      # 27
            date_like = c                   # 28
            break                           # 29
    if date_like is not None:               # 30
        df[date_like] = pd.to_datetime(df[date_like], errors="coerce")  # 31
        df["month"] = df[date_like].dt.month                            # 32
        month_col = "month"                                              # 33

# Final validation
if month_col is None or temp_col is None:   # 34
    sys.exit("[Error] Could not infer 'month' or 'temperature' column. "
             "Rename your columns to include 'month' and 'temperature' (case-insensitive).")  # 35

# ---------- 3) Keep only what we need; clean and aggregate -------------------

work = df[[month_col, temp_col]].dropna().copy()  # 36

# Ensure month is numeric in [1..12]
work[month_col] = pd.to_numeric(work[month_col], errors="coerce")  # 37
work = work[work[month_col].between(1, 12)]                        # 38

# If dataset has multiple rows per month, average to get a single month-wise series
agg = (work
       .groupby(month_col, as_index=False)[temp_col]
       .mean()
       .sort_values(by=month_col))                                  # 39

# Feature (X) and target (y)
X = agg[[month_col]].values                                         # 40
y = agg[temp_col].values                                            # 41

# ---------- 4) Train/Test split (75/25) --------------------------------------

X_train, X_test, y_train, y_test = train_test_split(                 # 42
    X, y, test_size=0.25, random_state=42
)

# ---------- 5) Model training -------------------------------------------------

model = LinearRegression()                                           # 43
model.fit(X_train, y_train)                                          # 44

# ---------- 6) Prediction and evaluation -------------------------------------

y_pred_test = model.predict(X_test)                                  # 45
y_pred_all  = model.predict(X)                                       # 46

mse = mean_squared_error(y_test, y_pred_test)                        # 47
mae = mean_absolute_error(y_test, y_pred_test)                       # 48
r2  = r2_score(y_test, y_pred_test)                                  # 49

print("=== Linear Regression Results ===")                            # 50
print(f"Coefficient (slope): {model.coef_[0]:.4f}")                  # 51
print(f"Intercept:           {model.intercept_:.4f}")                # 52
print(f"MSE:                 {mse:.4f}")                             # 53
print(f"MAE:                 {mae:.4f}")                             # 54
print(f"R²:                  {r2:.4f}")                              # 55

# ---------- 7) Visualization --------------------------------------------------

plt.figure(figsize=(7, 5))                                           # 56
plt.scatter(X, y, label="Actual")                                    # 57
plt.plot(X, y_pred_all, label="Regression Line")                     # 58
plt.xlabel("Month (1-12)")                                           # 59
plt.ylabel("Temperature (°C)")                                       # 60
plt.title("Month-wise Temperature Prediction (Linear Regression)")    # 61
plt.legend()                                                         # 62
plt.tight_layout()                                                   # 63
plt.savefig("regression_month_temperature.png", dpi=200)             # 64
plt.show()                                                           # 65
