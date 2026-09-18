import pandas as  pd
df = pd.read_csv(
    r"C:\Users\boddu\OneDrive\Desktop\Pandas_Day_4\Pandas_Day_4_Real_World_Sales_Data.csv"
)

# print(df)
# print(type(df))
# print(df.head())
# print(df.tail())
# print(df.sample(5))

# print(df.info())
# print(df["Order_ID"])
# print(df)
# print(df["Order_Date"].map(type).value_counts())
# df["Order_ID"] = df["Order_ID"].astype("string")
# df["Customer_ID"] = df["Customer_ID"].astype("string")
# df["Quantity"] = df["Quantity"].astype("int64")
# df["Price"] = df["Price"].astype("float64")

# print(df.dtypes)

# values = pd.Series(["100", "200", "300"])

# numbers = pd.to_numeric(values)

# print(numbers)
# print(numbers.dtype)

# values = pd.Series([
#     "100", "200", "unknown", "400"
# ])

# numbers = pd.to_numeric(
#     values,
#     errors="coerce"
# )

# print(numbers)


# 12. pd.to_datetime()
# Use pd.to_datetime() when a column represents dates or timestamps.
# df["Order_Date"] = pd.to_datetime(
#     df["Order_Date"]
# )

# print(df["Order_Date"].dtype)

# dates= pd.Series([
#     "2023-02-01",
#     "2023-02-01",
#     "2023-02-01",
#     "invalid date",
#     "2023-02-01"

# ])

# converted = pd.to_datetime(
#     dates,
#     errors="coerce"
# )
# print(converted)


# df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# df["Order_Year"] = df["Order_Date"].dt.year
# df["Order_Month"] = df["Order_Date"].dt.month
# df["Order_Day"] = df["Order_Date"].dt.day
# df["Order_Quarter"] = df["Order_Date"].dt.quarter
# print(df[["Order_Date", "Order_Year", "Order_Month", "Order_Day", "Order_Quarter"]])


"""Boolean Data Type
A condition naturally produces True/False values. This is useful for business flags."""

# df["Revenue"] = df["Quantity"] * df["Price"]

# df["High_Value"] =( df["Revenue"] > 50000 )
# print(df[["Revenue", "High_Value"]].head())
# print(df["High_Value"].dtype)

# print(df)


# category Data Type
# category is useful when a column contains a relatively small repeated set of labels.
# df["Category"] = df["Category"].astype("category")
# df["City"] = df["City"].astype("category")

# print(df.dtypes)
# Categorical data can reduce memory usage and communicate that a column represents a finite set of categories

# inspect Categorical Data

# print(df["Category"].cat.categories)
# print(df["Category"].cat.codes)


# print(df.memory_usage(deep=True))
# print(df.memory_usage(deep=True).sum())


# print(df.info())
# print(df.head())
# print(df.dtypes)

# print(df)
# df["Order_Date"] = pd.to_datetime(df["Order_Date"])
# print(df["Order_Date"].dtype)

print(df["Quantity"].dtypes)

df["Quantity"] = pd.to_numeric(df["Quantity"], errors="coerce")
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print(df[["Quantity", "Price"]].dtypes)