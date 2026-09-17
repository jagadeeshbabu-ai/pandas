employees = pd.DataFrame({
    "EmpID": ["E101", "E102", "E103", "E104",
              "E105", "E106", "E107", "E108"],
    "Name": ["Rahul", "Priya", "Arun", "Meena",
             "Kiran", "Sneha", "Vikram", "Anjali"],
    "Department": [
        "IT", "HR", "IT", "Sales",
        "Finance", "IT", "HR", "Finance"
    ],
    "City": [
        "Hyderabad", "Mumbai", "Hyderabad", "Chennai",
        "Delhi", "Hyderabad", "Mumbai", "Bangalore"
    ],
    "Age": [25, 29, 24, 32, 35, 31, 27, 30],
    "Salary": [45000, 55000, 48000, 70000,
               85000, 75000, 62000, 68000],
    "Experience": [2, 5, 1, 8, 10, 7, 4, 6]
})
print(employees)
# IT or HR
s=employees[employees["Department"].isin(["IT", "HR"])]

# Age 25–30
d=employees[employees["Age"].between(25, 30)]

# Salary ₹50,000–₹80,000
f=employees[employees["Salary"].between(50000, 80000)]

# Hyderabad + salary > ₹50,000
h=employees[
    (employees["City"] == "Hyderabad") &
    (employees["Salary"] > 50000)
]
print(s)
print("==================================================================================")
print(d)
print("==================================================================================")
print(f)
print("==================================================================================")
print(h)
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

print(df)
s=df[df["Department"].isin(["IT","HR"])]
print(s)
d=df[df["Age"].between(23,29,
inclusive="neither")]
print(d)
f=df[df["City"].isin(["Hyderabad","Mumbai"])]
print(f)

# v=df[
#     ~df["Department"] .isin(["IT"])
# ]
# print(v)
k=df[(df["Department"] == "IT") & (df["Experience"] > 5)]
print(k)
print("*******************************")
mask=df['Salary'] >50000
print(df.loc[mask,["Name", "Department", "City", "Salary"]])