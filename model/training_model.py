import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from parser.preprocessing import preprocess
from sklearn.metrics import accuracy_score, precision_score, recall_score
import joblib

def train_model():
    """
    Trains a logistic regression model for sepsis prediction.

    Loads the data from a CSV file, preprocesses it, splits it into training and testing sets,
    trains the logistic regression model, evaluates its performance, and saves the trained model to a file.
    """

    # Load the CSV file into a Pandas dataframe
    df = pd.read_csv('data/data_sepsis.csv')

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
    print('Accuracy:', accuracy_score(y_test, y_pred))
    print('Precision:', precision_score(y_test, y_pred))
    print('Recall:', recall_score(y_test, y_pred))

    # Save the trained model to a file
    filename = 'model/sepsis_model.sav'
    joblib.dump(model, filename)

def predict_sepsis(model, features):
    """
    Predicts sepsis for a given set of features using a trained model.

    Parameters:
        model: The trained logistic regression model.
        features: The input features for sepsis prediction.

    Returns:
        int: The predicted sepsis label (0 or 1).
    """
    # Convert the features into a dataframe
    df = pd.DataFrame([features], columns=features.keys())

    # Make the prediction using the loaded model
    prediction = model.predict(df)

    # Return the prediction
    return prediction[0]


#La régression logistique prédit la probabilité qu'un événement se produise.
# Elle utilise une fonction logistique pour modéliser la relation entre les variables d'entrée et la probabilité
# d'appartenir à une classe particulière.
# Le modèle est entraîné pour trouver les meilleurs paramètres qui minimisent
# la différence entre les probabilités prédites et les étiquettes réelles.
# Les prédictions sont faites en appliquant la fonction log