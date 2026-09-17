import pandas as pd

data = {
    "Name": ["Ravi", "Sita", "Arjun", "Priya", "Kiran", "Anjali", "Rahul", "Sneha", "Vijay", "Meena"],
    "Age": [24, 27, 29, 31, 26, 30, 28, 35, 25, 29],
    "Department": ["IT", "HR", "Finance", "IT", "HR", "Finance", "IT", "Sales", "IT", "Finance"],
    "City": ["Hyderabad", "Mumbai", "Delhi", "Hyderabad", "Chennai", "Mumbai", "Pune", "Hyderabad", "Mumbai", "Delhi"],
    "Salary": [45000, 60000, 75000, 85000, 52000, 68000, 72000, 48000, 55000, 80000],
    "Experience": [2, 4, 6, 8, 3, 5, 7, 10, 2, 6]
}

df = pd.DataFrame(data)

# print(df)

result = df[
    df["Department"].isin(["IT", "Finance"]) &
    (df["Experience"] >= 5) &
    df["Age"].between(25, 35) &
    df["Salary"].between(55000, 90000)
]

result = result[[ "Name", "Department", "Experience", "Salary"]]

print(result)
