# Load SGJobsDB into dataframe csv
import logging as lg
import pandas as pd


def load_csv_file(filepath):
    try:
        # Try reading with default parameters
        df = pd.read_csv(filepath)
        print(f"Successfully loaded {filepath}")
        print(f"Shape: {df.shape}")
        print(f"Columns: {df.columns.tolist()}")
        return df
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found")
    except pd.errors.EmptyDataError:
        print("Error: File is empty")
    except Exception as e:
        print(f"Error loading file: {str(e)}")
        # Try different encodings
        for encoding in ['latin1', 'cp1252', 'iso-8859-1']:
            try:
                df = pd.read_csv(filepath, encoding=encoding)
                print(f"Successfully loaded with {encoding} encoding")
                return df
            except:
                continue
    return None


# Main
df = load_csv_file('/Users/mohanjawahar/DataScience/data/SGJobData.csv')
if df is not None:
    # Display first few rows
    print(df.head())

    # Basic info
    print(df.info(memory_usage=True))
'''
    # Statistical summary
    print(df.describe())
'''
