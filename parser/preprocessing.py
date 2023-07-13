

def preprocess(df):
    """
    Preprocesses the input DataFrame by performing the following operations:
    1. Drops irrelevant columns: 'ID' and 'Insurance'
    2. Converts specific columns to float data type: 'PRG', 'PL', 'PR', 'SK', 'TS', 'M11', 'BD2', and 'Age'
    3. Replaces values in the 'Sepsis' column: 'Negative' with 0 and 'Positive' with 1

    Parameters:
        df (pandas DataFrame): The input DataFrame to be preprocessed.

    Returns:
        pandas DataFrame: The preprocessed DataFrame.
    """

    df.drop(['ID', 'Insurance'], axis=1, inplace=True)

    df['PRG'] = df['PRG'].astype(float)
    df['PL'] = df['PL'].astype(float)
    df['PR'] = df['PR'].astype(float)
    df['SK'] = df['SK'].astype(float)
    df['TS'] = df['TS'].astype(float)
    df['M11'] = df['M11'].astype(float)
    df['BD2'] = df['BD2'].astype(float)
    df['Age'] = df['Age'].astype(float)

    # Replace the values in the Sepsis column
    df['Sepsis'] = df['Sepsis'].replace('Negative', 0)
    df['Sepsis'] = df['Sepsis'].replace('Positive', 1)

    return df

