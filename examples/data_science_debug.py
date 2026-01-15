"""Example script for debugging data science code with pandas and numpy.

This script demonstrates the debug_inspect_variable tool which provides
smart inspection of DataFrames, arrays, dicts, and lists.

Suggested debugging prompt for your AI agent:
--------------------------------------------
Debug examples/data_science_debug.py and set a breakpoint at line 45.
When it pauses, inspect the variables `df`, `totals`, `normalized`, and
`sales_by_region` to understand the data shapes, types, and statistics.
Identify why there might be NaN values in the calculations.

The debug_inspect_variable tool will show:
- DataFrame: shape, columns, dtypes, memory usage, head rows, null counts
- Series: length, dtype, statistics (min/max/mean/std)
- ndarray: shape, dtype, sample values, statistics
- dict: keys, value types, sample items
"""

import numpy as np
import pandas as pd


def load_sales_data() -> pd.DataFrame:
    """Load sample sales data with some missing values."""
    return pd.DataFrame(
        {
            "product": [
                "Widget",
                "Gadget",
                "Gizmo",
                "Widget",
                "Gadget",
                "Gizmo",
                "Widget",
                "Gadget",
            ],
            "region": ["East", "West", "East", "West", "East", "West", "East", "West"],
            "sales": [100.0, 200.0, None, 150.0, 250.0, 175.0, None, 225.0],  # Note: None values
            "units": [10, 20, 15, 15, 25, 17, 12, 22],
            "date": pd.date_range("2024-01-01", periods=8, freq="D"),
        }
    )


def analyze_sales(df: pd.DataFrame) -> dict:
    """Analyze sales data and return summary statistics."""
    # Group by product
    totals = df.groupby("product")["sales"].sum()

    # Normalize sales (this will propagate NaN!)
    normalized = np.array(df["sales"]) / df["sales"].max()

    # Sales by region
    sales_by_region = df.groupby("region")["sales"].agg(["sum", "mean", "count"]).to_dict()

    # Set breakpoint here (line 45) to inspect variables
    print(f"Analysis complete. Found {df['product'].nunique()} products.")  # Line 45

    return {
        "totals": totals,
        "normalized": normalized,
        "by_region": sales_by_region,
    }


def create_random_matrix(rows: int, cols: int) -> np.ndarray:
    """Create a random matrix for demonstration."""
    np.random.seed(42)
    matrix = np.random.randn(rows, cols)
    # Add some structure
    matrix[:, 0] = np.arange(rows)  # First column is sequential
    matrix[:, -1] = np.random.choice([0, 1], size=rows)  # Last column is binary
    return matrix


def main():
    """Main analysis pipeline."""
    print("Data Science Debug Example")
    print("=" * 50)

    # Load data
    print("\n1. Loading sales data...")
    df = load_sales_data()
    print(f"   Loaded {len(df)} rows, {len(df.columns)} columns")
    print(f"   Columns: {list(df.columns)}")

    # Check for missing values
    print("\n2. Checking data quality...")
    null_counts = df.isnull().sum()
    print(f"   Missing values:\n{null_counts[null_counts > 0].to_string()}")

    # Analyze
    print("\n3. Analyzing sales...")
    results = analyze_sales(df)

    # Create a larger array for inspection demo
    print("\n4. Creating random matrix (100x50)...")
    matrix = create_random_matrix(100, 50)
    print(f"   Matrix shape: {matrix.shape}")
    print(f"   Matrix dtype: {matrix.dtype}")

    # Create some nested data structures
    print("\n5. Building summary...")
    summary = {
        "metadata": {
            "source": "sales_db",
            "version": "1.0",
            "records": len(df),
        },
        "products": df["product"].unique().tolist(),
        "regions": df["region"].unique().tolist(),
        "date_range": [str(df["date"].min()), str(df["date"].max())],
    }

    # Mixed-type list
    audit_log = [
        "Started analysis",
        {"timestamp": "2024-01-01", "action": "load"},
        42,
        True,
        ["nested", "list", "items"],
    ]

    # Another good breakpoint location (line 99)
    print("\n" + "=" * 50)  # Line 99
    print("Analysis complete!")
    print(f"Total sales: {results['totals'].sum():.2f}")

    return results, matrix, summary, audit_log


if __name__ == "__main__":
    results, matrix, summary, audit_log = main()
