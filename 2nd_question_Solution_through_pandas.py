
'''Author: Himanshu Gupta
Date : 11/04/2024
'''
import pandas as pd



'''2. extract the total quantities of each item bought per customer aged 18-35.
- For each customer, get the sum of each item
- Items with no purchase (total quantity=0) should be omitted from the final
list
- No decimal points allowed (The company doesn’t sell half of an item ;) )
Challenge: Provide 2 solutions using Pandas'''


# Sample data for customers, sales, orders, and items
customers_data = {
    "customer_id": [1, 2, 3, 4, 5],
    "age": [20, 25, 30, 22, 35]
}

sales_data = {
    "sales_id": [101, 102, 103, 104, 105],
    "customer_id": [1, 2, 3, 4, 5]
}

orders_data = {
    "order_id": [1001, 1002, 1003, 1004, 1005],
    "sales_id": [101, 102, 103, 104, 105],
    "item_id": [101, 102, 103, 101, 104],
    "quantity": [2, 1, 3, 2, 1]
}

items_data = {
    "item_id": [101, 102, 103, 104],
    "item_name": ["Item A", "Item B", "Item C", "Item D"]
}

# Create DataFrame from sample data
customers_df = pd.DataFrame(customers_data)
sales_df = pd.DataFrame(sales_data)
orders_df = pd.DataFrame(orders_data)
items_df = pd.DataFrame(items_data)

# Merge/join DataFrames
merged_df = customers_df.merge(sales_df, on="customer_id").merge(orders_df, on="sales_id").merge(items_df, on="item_id")

# Filter rows based on age condition
filtered_df = merged_df[(merged_df["age"] >= 18) & (merged_df["age"] <= 35)]

# Group by and aggregate to get total_quantity
result_df = filtered_df.groupby(["customer_id", "item_id", "item_name"]).agg(total_quantity=("quantity", "sum")).reset_index()

# Filter rows with total_quantity > 0
result_df = result_df[result_df["total_quantity"] > 0]

# Sort the result DataFrame
result_df = result_df.sort_values(by=["customer_id", "item_id"])

print(result_df)
