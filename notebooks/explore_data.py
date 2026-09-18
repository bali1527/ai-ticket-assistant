import pandas as pd

df = pd.read_csv("data/support_tickets.csv")

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nData Types:")
print(df.dtypes)

print("\nStatus Distribution:")
print(df["status"].value_counts())

print("\nPriority Distribution:")
print(df["priority"].value_counts())