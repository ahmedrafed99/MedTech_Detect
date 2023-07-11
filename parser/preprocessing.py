

def preprocess(df):
    # Drop irrelevant columns
    df.drop(['ID', 'Insurance'], axis=1, inplace=True)

    # Convert specific columns to float
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
