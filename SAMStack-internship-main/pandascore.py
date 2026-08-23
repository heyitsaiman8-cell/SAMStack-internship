import pandas as pd
marks = [80, 90, 75, 88]
s = pd.Series(marks)
print(s)

print("==================================")
print("=====dictionaries to series=====")
print("==================================")
import pandas as pd
marks ={
  "Ali":80,
   "inha" : 90,
   "soha": 45,
   "yunha": 88
}
s = pd.Series(marks)
print(s)

#dataframe
print("==================================")
print("=====dictionaries to dataframe=====")
print("==================================")
import pandas as pd
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Ayesha"],
    "Age": [20, 21, 19, 22],
    "Marks": [85, 92, 78, 88]
}
display = pd.DataFrame(data)
print(display)

print("==================================")
print("=======list to dataframe=====")
print("==================================")
import pandas as pd

data = [
    ["Ali", 20, 85],
    ["Sara", 21, 92],
    ["Ahmed", 19, 78]
]

df = pd.DataFrame(data, columns=["Name", "Age", "Marks"])

print(df)

print("==================================")
print("=======.loc,.iloc=====")
print("==================================")

import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [20, 21, 19],
    "Marks": [85, 92, 78]
}
df = pd.DataFrame(data, index=["student1", "student2", "student3"])
print(df)
print(df.loc["student2","Age"])
print(df.iloc[1, 2,])

#Conditional Row Filtering
print("==================================")
print("=====Conditional Row Filtering======")
print("============multiple conditions========")
print("========.info,.describe===========")
print("==================================")
import pandas as pd

data = {
    "Name": ["Ali", "Sara", "Ahmed"],
    "Age": [20, 21, 19],
    "Marks": [85, 92, 78]
}
pp=pd.DataFrame(data)
result=pp[pp["Marks"]>70]
print(result)
result = df[(df["Marks"] > 80) & (df["Age"] > 20)]

print(result)
print(pp.info())
print(pp.describe())
