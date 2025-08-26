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
    # - Show column data types
    # - Show missing value summary
    # - (Stretch) Export summary to JSON

if __name__ == "__main__":
    main()

