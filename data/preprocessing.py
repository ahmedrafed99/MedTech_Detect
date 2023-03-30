

def preprocess(df):
    # Drop irrelevant columns
    df.drop('ID', axis=1, inplace=True)

    # Replace the values in the Sepssis column
    df['Sepsis'] = df['Sepsis'].replace('Negative', 0)
    df['Sepsis'] = df['Sepsis'].replace('Positive', 1)
    return df