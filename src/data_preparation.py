import pandas as pd

def load_credit_card_data(file_path: str) -> pd.DataFrame:
    """
    load credit card data from a CSV file.
    
    args:
        file_path (str): path to the CSV file containing credit card data.
    
    returns:
        pd.DataFrame: dataFrame containing the credit card data.
    """
    try:
        df = pd.read_csv(file_path)
        print(f"Successfully loaded {len(df)} credit cards.")
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

# test function directly
if __name__ == "__main__":
    df = load_credit_card_data("../data/credit_cards.csv")
    print(df.head())