import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


print(" ==============================")
print(" DATA")
print(" ==============================")

months = ["January", "February", "March", "April", "May", "June"]
sales = [120, 150, 180, 170, 220, 250]

students = ["Ali", "Sara", "Ahmed", "Eiman", "Hina"]
marks = [75, 88, 67, 92, 81]

study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
study_marks = [45, 50, 55, 62, 68, 75, 82, 90]


print(" ==============================")
print(" 1. LINE CHART")
print(" ==============================")

plt.figure(figsize=(10, 6))

plt.plot(
    months,
    sales,
    marker="o",
    label="Monthly Sales"
)

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Trend")
plt.legend()

plt.savefig(
    "line_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


print(" ==============================")
print(" 2. BAR PLOT")
print(" ==============================")

plt.figure(figsize=(10, 6))

plt.bar(
    students,
    marks,
    label="Student Marks"
)

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Comparison")
plt.legend()

plt.savefig(
    "bar_plot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("============================== ")
print("3. HISTOGRAM")
print("==============================")

plt.figure(figsize=(10, 6))

plt.hist(
    marks,
    bins=5,
    label="Marks Distribution"
)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Student Marks")
plt.legend()

plt.savefig(
    "histogram.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


print(" ==============================")
print(" 4. SCATTER PLOT")
print(" ==============================")

plt.figure(figsize=(10, 6))

plt.scatter(
    study_hours,
    study_marks,
    label="Students"
)

plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.legend()

plt.savefig(
    "scatter_plot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


print(" ==============================")
print(" DATAFRAME FOR SEABORN")
print(" ==============================")

data = {
    "Study Hours": [2, 4, 6, 8, 10],
    "Attendance": [60, 70, 75, 85, 95],
    "Assignments": [50, 60, 70, 80, 90],
    "Final Marks": [55, 65, 72, 84, 95]
}

df = pd.DataFrame(data)


print(" ==============================")
print(". SEABORN BOX PLOT")
print(" ==============================")

plt.figure(figsize=(10, 6))

sns.boxplot(data=df)

plt.title("Box Plot of Student Performance")
plt.xlabel("Subjects/Factors")
plt.ylabel("Values")

plt.savefig(
    "box_plot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


print("========================")
print(" 6. SEABORN HEATMAP")
print("=========================")

correlation = df.corr()

plt.figure(figsize=(10, 6))

sns.heatmap(
    correlation,
    annot=True
)

plt.title("Correlation Heatmap")

plt.savefig(
    "heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


print("All charts have been created and saved successfully!")