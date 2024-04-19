import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import SGDClassifier
from sklearn import metrics
import joblib

try:
    model = joblib.load('model.pkl')
    vectorizer = joblib.load('vectorizer.pkl')
except FileNotFoundError:
    data = pd.read_csv('results.csv')
    data = data.dropna()
    X = data['line']
    y = data['label']

    vectorizer = TfidfVectorizer()
    X_tfidf = vectorizer.fit_transform(X)
    joblib.dump(vectorizer, 'vectorizer.pkl')

    smote = SMOTE(random_state=42)
    X_resampled, y_resampled = smote.fit_resample(X_tfidf, y)

    model = SGDClassifier(loss='log', random_state=42)
    X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.1, random_state=42)
    model.partial_fit(X_train, y_train, classes=np.unique(y_resampled))
    joblib.dump(model, 'model.pkl')

def predict_and_update(text, actual_label=None):
    text_tfidf = vectorizer.transform([text])
    prediction = model.predict(text_tfidf)
    prediction_result = "Non-descriptive" if prediction[0] == 1 else "Descriptive"

    if actual_label is not None:
        model.partial_fit(text_tfidf, [actual_label])
        joblib.dump(model, 'model.pkl') 
        feedback = f"Model updated based on feedback. Prediction was: {prediction_result}"
    else:
        feedback = "No feedback provided. Prediction was: " + prediction_result

    return feedback

# Testing updates
prediction = input("Enter a line of text from an <a> tag: ")
actual_label = input("Enter the actual label (0 for descriptive, 1 for non-descriptive): ")

print(predict_and_update(prediction, actual_label=int(actual_label)))
