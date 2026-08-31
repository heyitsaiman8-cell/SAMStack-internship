import pandas as pd
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    logging.info("ETL process started")
    data = pd.read_csv("students.csv")
    logging.info("Data extracted successfully")
  
    data["name"] = data["name"].str.strip()

   
    data["age"] = data["age"].fillna(data["age"].median())
    data["marks"] = data["marks"].fillna(data["marks"].median())
    data = data.drop_duplicates()

    logging.info("Data transformed successfully")
    data.to_csv("students_cleaned.csv", index=False)

    logging.info("Cleaned data saved successfully")

except Exception as e:

    logging.exception("An error occurred")
