import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# ==========================================
# DAY 21 - EXPLORATORY DATA ANALYSIS
# ==========================================

# 1. Load Dataset
df = pd.read_csv("student_performance.csv")

print("========== EDA REPORT ==========")

# 2. Basic Structure
print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Column Names ---")
print(df.columns.tolist())

# 3. Dataset Information
print("\n--- Dataset Information ---")
df.info()

# 4. Missing Values
print("\n--- Missing Values ---")
print(df.isnull().sum())

# 5. Statistical Summary
print("\n--- Statistical Summary ---")
print(df.describe())

# 6. Skewness
print("\n--- Skewness ---")
print(df.skew(numeric_only=True))

# 7. Distribution
plt.figure(figsize=(8, 5))

df["Exam_Score"].hist()

plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.show()

# 8. Boxplot
plt.figure(figsize=(8, 5))

sns.boxplot(x=df["Exam_Score"])

plt.title("Exam Score Outliers")
plt.xlabel("Exam Score")
plt.show()

# 9. Z-Score
df["Exam_ZScore"] = zscore(df["Exam_Score"])

print("\n--- Exam Scores with Z-Scores ---")
print(df[["Exam_Score", "Exam_ZScore"]])

# Identify Outliers
outliers = df[abs(df["Exam_ZScore"]) > 3]

print("\n--- Potential Outliers ---")
print(outliers)

# 10. Correlation Matrix
correlation = df.corr(numeric_only=True)

print("\n--- Correlation Matrix ---")
print(correlation)

# 11. Correlation Heatmap
plt.figure(figsize=(9, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix Heatmap")
plt.show()

print("\n========== EDA COMPLETED ==========")