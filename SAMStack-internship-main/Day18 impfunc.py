import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha", "Hamza"],
    "Age": [20, 21, None, 22, 20],
    "Marks": [85, None, 78, 90, None],
    "City": ["Lahore", "lahore ", "Islamabad", None, "LAHORE"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

print("\nMissing Values:")
print(df.isnull().sum())

# Mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Median
df["Marks"] = df["Marks"].fillna(df["Marks"].median())

# Clean City FIRST
df["City"] = df["City"].str.strip().str.lower()

# Mode
df["City"] = df["City"].fillna(df["City"].mode()[0])

# Convert Age to integer
df["Age"] = df["Age"].astype(int)

print("\nCleaned Data:")
print(df)

print("\nData Types:")
print(df.dtypes)