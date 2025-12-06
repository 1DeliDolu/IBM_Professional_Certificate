import pandas as pd
import requests
import os

def download_file(url, filename):
    """
    Downloads a file from a URL if it doesn't already exist locally.
    """
    if not os.path.exists(filename):
        print(f"Downloading {filename}...")
        try:
            response = requests.get(url)
            response.raise_for_status()  # Check for HTTP errors
            with open(filename, "wb") as f:
                f.write(response.content)
            print("Download complete.")
        except requests.exceptions.RequestException as e:
            print(f"Failed to download {filename}: {e}")
    else:
        print(f"{filename} already exists.")

def main():
    # --- Part 1: Loading CSV ---
    print("\n=== 1. Loading CSV Data ===")
    csv_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv"
    csv_filename = "TopSellingAlbums.csv"

    download_file(csv_url, csv_filename)
    
    if os.path.exists(csv_filename):
        df = pd.read_csv(csv_filename)
        print("First 5 rows of the CSV DataFrame:")
        print(df.head())
        
        # --- Part 2: Accessing Data ---
        print("\n=== 2. Accessing Data ===")
        
        # Access 'Length' column
        print("\nAccessing 'Length' column (as DataFrame):")
        x = df[['Length']]
        print(x.head())

        # Access 'Length' column as Series
        print("\nAccessing 'Length' column (as Series):")
        x_series = df['Length']
        print(x_series.head())

        # Access Multiple Columns
        print("\nAccessing Multiple Columns (Artist, Length, Genre):")
        y = df[['Artist', 'Length', 'Genre']]
        print(y.head())

        # Access using iloc
        print("\nAccessing specific elements using iloc:")
        print(f"Row 0, Col 0: {df.iloc[0, 0]}")
        print(f"Row 1, Col 0: {df.iloc[1, 0]}")
        print(f"Row 0, Col 2: {df.iloc[0, 2]}")

        # Access using loc
        print("\nAccessing specific elements using loc:")
        print(f"Row 1, Artist: {df.loc[1, 'Artist']}")

        # Slicing
        print("\nSlicing the dataframe (Rows 0-1, Cols 0-2):")
        print(df.iloc[0:2, 0:3])

    # --- Part 3: Loading Excel ---
    print("\n=== 3. Loading Excel Data ===")
    xlsx_url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/jupyterlite/files/Module%205/data/TopSellingAlbums.xlsx"
    xlsx_filename = "TopSellingAlbums.xlsx"

    download_file(xlsx_url, xlsx_filename)

    if os.path.exists(xlsx_filename):
        try:
            df_excel = pd.read_excel(xlsx_filename)
            print("First 5 rows of the Excel DataFrame:")
            print(df_excel.head())
        except Exception as e:
            print(f"Error reading Excel file: {e}")

if __name__ == "__main__":
    main()