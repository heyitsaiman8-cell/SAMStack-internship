import pandas as pd
import matplotlib.pyplot as plt
data=pd.read_csv(r"C:\Users\Lenovo\Downloads\SAMStack-internship-main\students performance analytics\students1.csv")
print("original data")
print(data)
print("missing values in each column")
print(data.isnull().sum())
print("data after filling missing values")
data["Python"]=data["Python"].fillna(data["Python"].mean())
data["Math"]=data["Math"].fillna(data["Math"].mean())
data["Name"]=data["Name"].str.strip()
data["Attendance"]=data["Attendance"].fillna(data["Attendance"].mean())
data["Name"]=data["Name"].fillna("inha")
data["Total_Marks"]=data["Python"]+data["Math"]
data["Average_Marks"]=data["Total_Marks"]/2
def get_result(average_marks):
    if average_marks >= 90:
        return "Excellent"
    elif average_marks >= 80:
        return "Perfect"
    elif average_marks >= 70:
        return "good"
    elif average_marks >= 60:
        return "not bad"
    elif average_marks >= 50:
        return "average"
    else:
        return "fail and need to work hard"
data["Result"]=data["Average_Marks"].apply(get_result)
departments=data.groupby("Department")[["Python","Math","Total_Marks","Average_Marks","Attendance"]].mean()
print("data according to department")
print(departments)
print("cleaned data")
print(data)
data.to_csv(r"C:\Users\Lenovo\Downloads\SAMStack-internship-main\students performance analytics\cleaned students1.csv",index=False)
print("data saved to cleaned students1.csv")

departments=data.groupby("Department")[["Average_Marks"]].mean()
departments.plot(kind="bar", legend=False,title="Average Marks by Department",figsize=(8, 5))
plt.xlabel("Department")
plt.ylabel("Average Marks")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(r"C:\Users\Lenovo\Downloads\SAMStack-internship-main\students performance analytics\matplotlibgraph.png")
plt.show()
plt.figure(figsize=(8, 5))

plt.scatter(
    data["Attendance"],
    data["Average_Marks"]
)

plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance (%)")
plt.ylabel("Average Marks")
plt.tight_layout()

plt.savefig(r"C:\Users\Lenovo\Downloads\SAMStack-internship-main\students performance analytics\matplotlib.png")

plt.show()

print("\nVisualizations exported successfully!")