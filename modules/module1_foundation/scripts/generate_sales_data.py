import random

import numpy as np
import pandas as pd


def generate_sales_data(start_date="2023-01-01", periods=365):
    """
    Generate realistic sales data with temporal patterns, seasonality,
    and promotional effects.
    """
    # Set random seed for reproducibility
    np.random.seed(42)

    # Base data parameters
    products = {
        "Laptop": {
            "category": "Electronics",
            "base_price": 999.99,
            "seasonality": "back_to_school",
        },
        "Smartphone": {
            "category": "Electronics",
            "base_price": 699.99,
            "seasonality": "holiday",
        },
        "Headphones": {
            "category": "Electronics",
            "base_price": 159.99,
            "seasonality": "holiday",
        },
        "Coffee Maker": {
            "category": "Appliances",
            "base_price": 79.99,
            "seasonality": "winter",
        },
        "Blender": {
            "category": "Appliances",
            "base_price": 49.99,
            "seasonality": "summer",
        },
        "Office Chair": {
            "category": "Furniture",
            "base_price": 199.99,
            "seasonality": "work_from_home",
        },
        "Desk": {
            "category": "Furniture",
            "base_price": 299.99,
            "seasonality": "work_from_home",
        },
    }

    regions = ["East", "West", "North", "South"]

    # Create date range
    dates = pd.date_range(start=start_date, periods=periods, freq="D")

    # Lists to store data
    records = []

    for date in dates:
        # Add seasonal effects
        month = date.month
        day_of_week = date.dayofweek

        # Seasonal multipliers
        season_mult = 1.0
        if month in [11, 12]:  # Holiday season
            season_mult = 1.5
        elif month in [6, 7, 8]:  # Summer
            season_mult = 1.2
        elif month in [8, 9]:  # Back to school
            season_mult = 1.3

        # Day of week effects (weekends have different patterns)
        dow_mult = 1.0 if day_of_week < 5 else 0.7

        for product, details in products.items():
            for region in regions:
                # Base demand with randomness
                base_demand = np.random.normal(100, 20)

                # Apply multipliers
                demand = base_demand * season_mult * dow_mult

                # Product-specific seasonality
                if details["seasonality"] == "holiday" and month in [11, 12]:
                    demand *= 2.0
                elif details["seasonality"] == "back_to_school" and month in [8, 9]:
                    demand *= 1.8
                elif details["seasonality"] == "summer" and month in [6, 7, 8]:
                    demand *= 1.5
                elif details["seasonality"] == "winter" and month in [12, 1, 2]:
                    demand *= 1.6
                elif details["seasonality"] == "work_from_home":
                    demand *= 1.3  # Constant elevated demand

                # Random promotions
                on_promotion = random.random() < 0.1  # 10% chance of promotion
                price = details["base_price"] * (0.8 if on_promotion else 1.0)

                # Add some noise to price
                price *= np.random.normal(1, 0.02)  # 2% price variation

                # Calculate quantity (rounded to whole numbers)
                quantity = max(0, int(demand * np.random.normal(1, 0.1)))

                # Calculate total sales
                total_sales = quantity * price

                # Create record
                record = {
                    "Date": date,
                    "Product": product,
                    "Category": details["category"],
                    "Region": region,
                    "Quantity": quantity,
                    "Unit_Price": round(price, 2),
                    "Total_Sales": round(total_sales, 2),
                    "On_Promotion": on_promotion,
                }
                records.append(record)

    # Create DataFrame
    df = pd.DataFrame(records)

    return df


if __name__ == "__main__":
    # Generate one year of daily sales data
    sales_df = generate_sales_data()

    # Save to CSV
    output_path = "datasets/sales/retail_sales_data.csv"
    sales_df.to_csv(output_path, index=False)
    print(f"Generated sales data saved to: {output_path}")

    # Print some basic statistics
    print("\nDataset Overview:")
    print(f"Total Records: {len(sales_df)}")
    print(f"Date Range: {sales_df['Date'].min()} to {sales_df['Date'].max()}")
    print("\nTotal Sales by Category:")
    print(sales_df.groupby("Category")["Total_Sales"].sum())
    print("\nTotal Sales by Region:")
    print(sales_df.groupby("Region")["Total_Sales"].sum())
