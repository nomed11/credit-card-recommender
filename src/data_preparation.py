import pandas as pd

def load_credit_card_data(file_path: str) -> pd.DataFrame:
    """
    Load credit card data from a CSV file and clean it up.
    
    Args:
        file_path (str): Path to the CSV file containing credit card data.
    
    Returns:
        pd.DataFrame: A cleaned DataFrame containing the credit card data.
    """
    try:
        # Read CSV
        df = pd.read_csv(file_path)
        
        # Clean up column names
        df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
        
        # Remove asterisks from all columns
        for col in df.columns:
            if df[col].dtype == 'object':
                df[col] = df[col].str.replace('*', '', regex=False)
            
        # Convert numeric columns
        numeric_cols = ['annual_fee', 'foreign_transaction_fee']
        for col in numeric_cols:
            df[col] = pd.to_numeric(df[col], errors='coerce')
        
        print(f"Successfully loaded and cleaned {len(df)} credit cards.")
        print("Column names:", df.columns.tolist())
        return df
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print(f"Error: The file at {file_path} is empty.")
        return pd.DataFrame()
    except pd.errors.ParserError:
        print(f"Error: Unable to parse the file at {file_path}. Make sure it's a valid CSV.")
        return pd.DataFrame()

# Test function directly
if __name__ == "__main__":
    df = load_credit_card_data("../data/credit_cards.csv")
    print(df.head())
    print("\nDataFrame Info:")
    print(df.info())