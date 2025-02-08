import pandas as pd
import os

try:
    # Load the CSV file into a pandas DataFrame
    input_file = 'datasets/sales/sample_sales_data.csv'
    df = pd.read_csv(input_file)
    print(f"Successfully read input file: {input_file}")

    # Calculate the cost using the provided unit cost of 20
    df['Cost'] = df['Quantity'] * 20
    print("Successfully calculated 'Cost' column")

    # Save the updated DataFrame to a new CSV file
    output_file = 'datasets/sales/sample_sales_data_with_cost.csv'
    print(f"Attempting to save to: {os.path.abspath(output_file)}")  # Print the absolute path
    df.to_csv(output_file, index=False)

    print(f"Added 'Cost' column to {output_file}")

except FileNotFoundError:
    print(f"Error: Input file not found.")
except pd.errors.EmptyDataError:
    print(f"Error: Input CSV file is empty.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
