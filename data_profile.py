import pandas as pd
import argparse

def load_data(file_path):
    """Load a CSV file into a Pandas DataFrame."""
    try:
        df = pd.read_csv(file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        exit(1)
    except Exception as e:
        print(f"Error loading file: {e}")
        exit(1)

def main():
    # CLI argument parser
    parser = argparse.ArgumentParser(description="Simple Data Profiler")
    parser.add_argument("file", help="Path to CSV file")
    args = parser.parse_args()

    # Load data
    df = load_data(args.file)

    # Basic outputs (starting point)
    print("=== Data Profile Report ===")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")

    # TODO: Add functionality:
    # - Show top 5 rows
    print("\n=== Top 5 rows ===")
    print(df.head())
    # - Show column data types
    print("\n=== Column data types ===")
    print(df.dtypes)
    # - Show missing value summary
    missing_summary = df.isnull().sum() # counts each columns missing data
    missing_percent = (df.isnull().mean() * 100).round(2) # percentage per column

    # make a new data frame to put the values into columns 
    summary_df = pd.DataFrame({
        "Missing Values": missing_summary,
        "Percent Missing": missing_percent
    })

    print("\n=== Missing value summary ===")
    print(summary_df)
    print("\nTotal missing values in dataset:", missing_summary.sum())
    # - (Stretch) Export summary to JSON

if __name__ == "__main__":
    main()

