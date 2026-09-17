result = df[
    df["Department"].isin(["IT", "Finance"]) &
    (df["Experience"] >= 5) &
    df["Age"].between(25, 35) &
    df["Salary"].between(55000, 90000)
]

result = result[[ "Name", "Department", "Experience", "Salary"]]

print(result)
