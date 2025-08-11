import pandas as pd
import matplotlib.pyplot as plt

# Step 1: CSV ka path set karo
file_path = r"C:\Users\av713\OneDrive\Desktop\Elevate Labs Tasks\Analysis task\sales_data.csv"

# Step 2: Data load karo
df = pd.read_csv(file_path)

# Step 3: Data ka preview
print("First 5 rows:")
print(df.head())

# Step 4: Summary stats
print("\nSummary Statistics:")
print(df.describe())

# Step 5: Total sales by Product
sales_by_product = df.groupby("Product")["Sales"].sum().reset_index()
print("\nTotal Sales by Product:")
print(sales_by_product)

# Step 6: Bar chart - Sales by Product
plt.figure(figsize=(8,5))
plt.bar(sales_by_product["Product"], sales_by_product["Sales"], color='skyblue')
plt.title("Total Sales by Product")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.show()

# Step 7: Total sales by Month
sales_by_month = df.groupby("Month")["Sales"].sum().reset_index()

# Step 8: Line chart - Sales by Month
plt.figure(figsize=(8,5))
plt.plot(sales_by_month["Month"], sales_by_month["Sales"], marker='o', color='green')
plt.title("Total Sales by Month")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)
plt.show()
