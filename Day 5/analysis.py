import pandas as pd
import matplotlib.pyplot as plt

# Load Excel file
df = pd.read_excel("sales.xlsx")

# Show first rows
print("Sample Data:")
print(df.head())

# Add Total column
df["Total"] = df["Quantity"] * df["Price"]

# Group by Product
summary = df.groupby("Product")["Total"].sum().reset_index()
print("\nSales Summary:")
print(summary)

# Plot chart
plt.figure(figsize=(8,5))
plt.bar(summary["Product"], summary["Total"], color="skyblue")
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
