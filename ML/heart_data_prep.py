import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# ------------------ 1) LOAD DATA -------------------------

df = pd.read_csv("heart.csv")      # keep the file next to this script

# ------------------ 2) BASIC OPERATIONS -------------------

print("\n--- SHAPE OF DATA ---")
print(df.shape)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- COUNT ZERO VALUES IN EACH COLUMN ---")
print((df == 0).sum())

print("\n--- MEAN AGE OF PATIENTS ---")
print(df["age"].mean())

# --------- 3) EXTRACT AGE, SEX, CHESTPAIN, RESTBP, CHOL ---------

selected = df[["age","sex","cp","trestbps","chol"]]

# 75–25 Split
train, test = train_test_split(selected, test_size=0.25, random_state=42)

print("\n--- TRAINING SET SIZE ---")
print(train.shape)

print("\n--- TESTING SET SIZE ---")
print(test.shape)

# ------------------ 4) CONFUSION MATRIX PROBLEM ------------------

# Given:
# Predicted positive: 100
# Actual positive inside predicted: 45
# Actual positives total: 50
# Total samples: 500

TP = 45
FP = 100 - TP
FN = 50 - TP
TN = 500 - (TP + FP + FN)

# Accuracy, Precision, Recall, F1
accuracy = (TP + TN) / 500
precision = TP / (TP + FP)
recall = TP / (TP + FN)
f1 = 2 * (precision * recall) / (precision + recall)

print("\n===== CONFUSION MATRIX =====")
print(f"TP = {TP}")
print(f"FP = {FP}")
print(f"FN = {FN}")
print(f"TN = {TN}")

print("\n===== METRICS =====")
print(f"Accuracy  : {accuracy:.4f}")
print(f"Precision : {precision:.4f}")
print(f"Recall    : {recall:.4f}")
print(f"F1 Score  : {f1:.4f}")
