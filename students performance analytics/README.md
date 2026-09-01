# Student Performance Analytics

 Overview

This project is a simple end-to-end data analytics project developed as part of the SAMStack Python Internship.

The project analyzes student performance data by extracting data from a CSV file, cleaning missing values, creating new performance metrics, analyzing department-wise trends, and generating visualizations.

 Project Workflow

CSV Data
↓
Data Extraction
↓
Missing Value Detection
↓
Data Cleaning
↓
Metric Transformation
↓
Department-wise Analysis
↓
Data Visualization
↓
Export Results

 Features

* Extract student data from a CSV file
* Detect missing values
* Handle missing numerical values using column averages
* Calculate total marks
* Calculate average marks
* Categorize student performance
* Analyze department-wise performance
* Compare attendance with average marks
* Export processed data
* Export visualizations as PNG files

Technologies Used

* Python
* Pandas
* Matplotlib
* CSV

 Data Processing

Missing values in the Math, Python, and Attendance columns are handled using the mean value of their respective columns.

The project then creates:

* Total Marks
* Average Marks
* Performance Category

Performance categories are based on average marks:

* 85 or above → Excellent
* 70–84 → Good
* 50–69 → Average
* Below 50 → Needs Improvement

Analysis

The project performs department-wise analysis using Pandas groupby() and calculates average values for:

* Math
* Python
* Average Marks
* Attendance

Visualizations

Two visualizations are generated:

1. Department-wise Average Marks
2. Attendance vs Average Marks

The charts are automatically exported to the output folder as PNG files.

 How to Run

Make sure Python, Pandas, and Matplotlib are installed.

Run the following command from the project folder:

python main.py

The processed data and visualizations will be generated automatically.

 Learning Outcomes

This project demonstrates basic data analytics concepts including:

* CSV data handling
* Pandas DataFrames
* Missing value handling
* Data transformation
* Conditional logic
* Grouping and aggregation
* Data visualization
* File export
