import pandas as pd
import logging

# Logging setup
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    logging.info("ETL process started")

    # =====================
    # 1. EXTRACT
    # =====================

    data = pd.read_csv("students.csv")
    logging.info("Data extracted successfully")

    # =====================
    # 2. TRANSFORM
    # =====================

    # Remove extra spaces
    data["name"] = data["name"].str.strip()

    # Fill missing values
    data["age"] = data["age"].fillna(data["age"].median())
    data["marks"] = data["marks"].fillna(data["marks"].median())

    # Remove duplicates
    data = data.drop_duplicates()

    logging.info("Data transformed successfully")

    # =====================
    # 3. LOAD
    # =====================

    data.to_csv("students_cleaned.csv", index=False)

    logging.info("Cleaned data saved successfully")

except Exception as e:

    logging.exception("An error occurred")
