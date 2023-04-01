import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from parser.preprocessing import preprocess

# Load the CSV file into a Pandas dataframe
df = pd.read_csv('../data/data_sepsis.csv')

df = preprocess(df)

# Split the dataframe into input features and target variable
features = df.drop('Sepsis', axis=1)
target = df['Sepsis']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Create a logistic regression model
model = LogisticRegression()

# Train the model using the training data
model.fit(X_train, y_train)

# Test the model using the testing data
y_pred = model.predict(X_test)

# Evaluate the performance of the model
from sklearn.metrics import accuracy_score, precision_score, recall_score
print('Accuracy:', accuracy_score(y_test, y_pred))
print('Precision:', precision_score(y_test, y_pred))
print('Recall:', recall_score(y_test, y_pred))

import joblib

# Save the trained model to a file
filename = 'sepsis_model.sav'
joblib.dump(model, filename)

def predict_sepsis(model, features):
    # Convert the features into a dataframe
    df = pd.DataFrame([features], columns=features.keys())

    # Make the prediction using the loaded model
    prediction = model.predict(df)

    # Return the prediction
    return prediction[0]




