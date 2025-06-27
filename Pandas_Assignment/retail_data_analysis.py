import pandas as pd

# Load the dataset
data = pd.read_csv("retail_sales_sample.csv")

# Display a welcome message
print(" Dataset loaded successfully!\n")

# Display number of rows and columns
print(f" Total Rows: {data.shape[0]}")
print(f" Total Columns: {data.shape[1]}\n")

# Display data types of each column
print(" Column Data Types:")
print(data.dtypes, "\n")

# Check for missing values in the dataset
print(" Missing Values Per Column:")
print(data.isnull().sum(), "\n")
print(data.isnull().count(), "\n")

# Display the first 5 rows using to_string for better formatting
print(" Preview of First 5 Rows:")
print(data.head().to_string(index=False))  # index=False hides row indices


# Step 2: Data Cleaning and Verification
print("\n Starting data cleaning process...\n")

# 1. Handle missing values
total_missing = data.isnull().sum().sum()
if total_missing > 0:
    print(f" Found {total_missing} missing values. Filling missing values...")

    # Fill numeric missing values with 0
    numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
    print(numeric_cols)
    data[numeric_cols] = data[numeric_cols].fillna(0)

    # Fill object (string) missing values with 'Unknown'
    object_cols = data.select_dtypes(include='object').columns
    data[object_cols] = data[object_cols].fillna("Unknown")

    print(" Missing values filled.\n")
else:
    print(" No missing values found.\n")

# 2. Convert 'OrderDate' to datetime
data['OrderDate'] = pd.to_datetime(data['OrderDate'], errors='coerce')
print(" 'OrderDate' column converted to datetime.\n")

# 3. Remove duplicate records
before = len(data)
data.drop_duplicates(inplace=True)
after = len(data)
print(f" Removed {before - after} duplicate record(s).\n")

# 4. Ensure numeric columns are correctly typed
numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns
for col in numeric_columns:
    data[col] = pd.to_numeric(data[col], errors='coerce')

print(" Numeric columns converted to numeric types.\n")

# Step 3: Feature Engineering
print("\n Starting Feature Engineering...\n")

# 1. Create a new column 'TotalPrice'
data['TotalPrice'] = data['Quantity'] * data['UnitPrice'] * (1 - data['Discount'])
print(" 'TotalPrice' column created successfully.")

# 2. Extract 'OrderMonth' and 'OrderYear' from 'OrderDate'
data['OrderMonth'] = data['OrderDate'].dt.month
data['OrderYear'] = data['OrderDate'].dt.year
print(" 'OrderMonth' and 'OrderYear' columns extracted from 'OrderDate'.")

# 3. Show a few rows to confirm new columns are added
print("\n Preview of new columns (first 5 rows):\n")
print(data[['Quantity', 'UnitPrice', 'Discount', 'TotalPrice', 'OrderDate', 'OrderMonth', 'OrderYear']].head().to_string(index=False))

# 4. Show updated column list to confirm
print("\n Current columns in dataset:")
print(data.columns.tolist())


# Step 4: Full Analysis (No Menu Required)
print("\n Step 4: Retail Sales Data Analysis\n")

# a. View Total Sales & Profit by Country
print(" a. Total Sales & Profit by Country (Sorted by Sales):\n")
country_summary = data.groupby("Country")[["TotalPrice", "Profit"]].sum().sort_values(by="TotalPrice", ascending=False)
print(country_summary.round(2).to_string())

# b. Top 10 Products by Revenue
print("\n b. Top 10 Products by Revenue (TotalPrice):\n")
top_products = data.groupby("ProductName")["TotalPrice"].sum().sort_values(ascending=False).head(10)
print(top_products.round(2).to_string())

# c. Monthly Sales Trend (across all years)
print("\n c. Monthly Sales Trend (All Years Combined):\n")
monthly_sales = data.groupby("OrderMonth")["TotalPrice"].sum().sort_index()
print(monthly_sales.round(2).to_string())

# d. Category Performance (Revenue and Profit)
print("\n d. Category Performance (Total Revenue and Profit):\n")
category_performance = data.groupby("Category")[["TotalPrice", "Profit"]].sum().sort_values(by="TotalPrice", ascending=False)
print(category_performance.round(2).to_string())

# e. All countries Transactions
data['Country'] = data['Country'].str.strip()
unique_countries = data['Country'].unique()

for country in unique_countries:
    print(f"\n First 10 Transactions for Country: {country}")
    country_data = data[data['Country'] == country]
    print(country_data.head(10).to_string(index=False))


# Step 5: Bonus Features
print("\n Bonus Features Processing...\n")

# 1. Calculate ProfitMargin
data['ProfitMargin'] = data['Profit'] / (data['Quantity'] * data['UnitPrice'])
print(" 'ProfitMargin' column added successfully.")

# Preview
print("\n Preview of ProfitMargin (first 5 rows):\n")
print(data[['Quantity', 'UnitPrice', 'Profit', 'ProfitMargin']].head().to_string(index=False))

# 2. Top 10 customers by number of orders
print("\n Top 10 Customers by Number of Orders:\n")
customer_orders = data['CustomerName'].value_counts().head(10)
print(customer_orders.to_string())
