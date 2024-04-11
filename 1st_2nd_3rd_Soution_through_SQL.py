'''Author: Himanshu Gupta
Date : 11/04/2024
'''
import sqlite3
import pandas as pd

#Question 1. connect to the SQLite3 database provided
def connect_to_database(db_file):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    print("Connected to SQLite database successfully!")
    return conn

def perform_database_operations(connection):
    if connection:
        # Perform database operations here
        cursor = connection.cursor()
        
        #Question 2. extract the total quantities of each item bought per customer aged 18-35.
        #- For each customer, get the sum of each item
        #- Items with no purchase (total quantity=0) should be omitted from the final list
        #- No decimal points allowed (The company doesn’t sell half of an item ;) )
        #Challenge: Provide 2 solutions, one using purely SQL.
        
        sql_query = """
            SELECT c.customer_id, i.item_id, i.item_name, SUM(o.quantity) AS total_quantity
            FROM customers c
            JOIN sales s ON c.customer_id = s.customer_id
            JOIN orders o ON s.sales_id = o.sales_id
            JOIN items i ON o.item_id = i.item_id
            WHERE c.age BETWEEN 18 AND 35
            GROUP BY c.customer_id, i.item_id, i.item_name
            HAVING total_quantity > 0
            ORDER BY c.customer_id, i.item_id;
            """
        cursor.execute(sql_query)
        result_rows = cursor.fetchall()
        if result_rows is not None:
            result_df = pd.DataFrame(result_rows, columns=['Customer', 'Age', 'Item', 'Quantity'])
            # Save the DataFrame to a CSV file with semicolon delimiter

            # 3. store the query to a CSV file, delimiter should be the semicolon character (';')
            
            #please change the path before runing other wise i will show error in your laptop
            result_df.to_csv('C:/Users/hgupt178/Documents/ETL_assignment_solution/output_file.csv', sep=';', index=False)
            print("Data saved to CSV file successfully!")
        else:
            print(" Error while - Data saved to CSV file")
    else:
        print("Failed to connect to the SQLite database.")

# Usage example
if __name__ == "__main__":
    db_file_path = 'C:/Users/hgupt178/Documents/ETL_assignment_solution/S30_Assignment.db'
    connection = connect_to_database(db_file_path)
    perform_database_operations(connection)
