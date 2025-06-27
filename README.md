
#  Retail Sales Analysis Project

This project analyzes a sample retail sales dataset using Python and pandas. It covers data loading, cleaning, feature engineering, and multiple insights generation — including country-level, product-level, and customer-level summaries.


##  Dataset

- File: `retail_sales_sample.csv`
- Expected Columns:
  - `OrderDate`, `Country`, `Category`, `ProductName`, `CustomerName`, `Quantity`, `UnitPrice`, `Discount`, `ShippingCost`, `Profit`


##  Project Steps

### 1. Dataset Loading
- Reads the CSV file using pandas.
- Displays:
  - Number of rows and columns
  - Data types
  - Missing values per column
  - First 5 sample rows

---

### 2. Data Cleaning
- **Missing Values**: 
  - Numeric columns → filled with `0`
  - Object (string) columns → filled with `"Unknown"`
- **Date Conversion**: 
  - Converts `OrderDate` to datetime format.
- **Duplicates**: 
  - Removes duplicate records.
- **Type Enforcement**: 
  - Ensures `Quantity`, `UnitPrice`, `Discount`, `ShippingCost`, and `Profit` are numeric.

---

### 3. Feature Engineering
- `TotalPrice` = `Quantity × UnitPrice × (1 - Discount)`
- Extracts:
  - `OrderMonth` from `OrderDate`
  - `OrderYear` from `OrderDate`


##  Step 4: Full Data Analysis 

### a. Total Sales & Profit by Country
- Grouped by `Country`
- Displays total `TotalPrice` and `Profit`, sorted by sales

### b. Top 10 Products by Revenue
- Based on sum of `TotalPrice` grouped by `ProductName`

### c. Monthly Sales Trend
- Total monthly sales grouped by `OrderMonth`

### d. Category Performance
- Total Revenue (`TotalPrice`) and `Profit` grouped by `Category`

### e. Raw Transactions by Country
- Displays first 10 transactions for **each unique country**


##  Step 5: Bonus Features

### 1. Profit Margin Calculation
- Formula: `Profit / (Quantity × UnitPrice)`
- Adds a new column `ProfitMargin`

### 2. Customers with Most Orders
- Lists top 10 customers by number of orders 


##  Requirements

- pandas

Install using:

```bash
pip install pandas
```


##  How to Run

1. Place `retail_sales_sample.csv` in the same folder.
2. Run the Python script (`.py`) using any Python IDE or terminal:

```bash
python retail_sales_analysis.py
```


##  Insights You Can Gain

- Which countries bring in the most revenue?
- What products are top sellers?
- Are there trends in sales across months?
- Which customers order the most?
- Which categories are most profitable?
