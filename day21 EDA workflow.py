import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

print(" ==========================================")
print("DAY 21 - EXPLORATORY DATA ANALYSIS")
print(" ==========================================")
df = pd.read_csv("student_performance.csv")
print("========== EDA REPORT ==========")
print("\n--- Dataset Shape ---")
print(df.shape)

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Dataset Information ---")
df.info()

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Statistical Summary ---")
print(df.describe())

print("\n--- Skewness ---")
print(df.skew(numeric_only=True))

print("Distribution")
plt.figure(figsize=(8, 5))

df["Exam_Score"].hist()

plt.title("Distribution of Exam Scores")
plt.xlabel("Exam Score")
plt.ylabel("Frequency")
plt.show()

print(" Boxplot")
plt.figure(figsize=(8, 5))

sns.boxplot(x=df["Exam_Score"])

plt.title("Exam Score Outliers")
plt.xlabel("Exam Score")
plt.show()

print(" Z-Score")
df["Exam_ZScore"] = zscore(df["Exam_Score"])

print("\n--- Exam Scores with Z-Scores ---")
print(df[["Exam_Score", "Exam_ZScore"]])

print(" Identify Outliers")
outliers = df[abs(df["Exam_ZScore"]) > 3]

print("\n--- Potential Outliers ---")
print(outliers)

print(" Correlation Matrix")
correlation = df.corr(numeric_only=True)

print("\n--- Correlation Matrix ---")
print(correlation)

print(" Correlation Heatmap")
plt.figure(figsize=(9, 6))

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Matrix Heatmap")
plt.show()

print("\n========== EDA COMPLETED ==========")