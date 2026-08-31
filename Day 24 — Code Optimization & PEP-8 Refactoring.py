
"""
Day 24 - Code Optimization & PEP-8 Refactoring
"""

import pandas as pd


def process_data(file_name: str) -> pd.DataFrame:
    """
    Load, clean, and process student data.

    Args:
        file_name: CSV file name.

    Returns:
        Processed student DataFrame.
    """
    data = pd.read_csv(file_name)

    data["name"] = data["name"].str.strip()
    data["age"] = data["age"].fillna(data["age"].mean())
    data["marks"] = data["marks"].fillna(data["marks"].mean())

    data["result"] = data["marks"].apply(
        lambda marks: "Pass" if marks >= 50 else "Fail"
    )

    return data


def main() -> None:
    """Run the data processing program."""
    data = process_data("abc.csv")

    print("Processed Data:")
    print(data)

    print("\nMemory Usage:")
    print(data.memory_usage(deep=True))


if __name__ == "__main__":
    main()

