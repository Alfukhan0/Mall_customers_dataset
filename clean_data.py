import pandas as pd

def clean_data(input_file, output_file):
    # Load the dataset
    df = pd.read_csv(input_file)
    
    # 1. Clean column names (strip trailing/leading spaces)
    df.columns = df.columns.str.strip()
    
    # 2. Check and remove duplicates
    initial_shape = df.shape
    df = df.drop_duplicates()
    duplicates_dropped = initial_shape[0] - df.shape[0]
    
    # 3. Check and handle missing values
    missing_values = df.isnull().sum().sum()
    if missing_values > 0:
        # Dropping rows with missing values for now
        df = df.dropna()
    
    # Save the cleaned dataset
    df.to_csv(output_file, index=False)
    print(f"Dataset cleaned successfully!")
    print(f"- Rows dropped due to duplicates: {duplicates_dropped}")
    print(f"- Rows dropped due to missing values: {missing_values}")
    print(f"- Cleaned dataset saved to: {output_file}")

if __name__ == "__main__":
    input_csv = "Mall_Customers (1).csv"
    output_csv = "Cleaned_Mall_Customers.csv"
    clean_data(input_csv, output_csv)
