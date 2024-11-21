import time
import streamlit as st
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

def predict_disease(symptoms, df):
    if not symptoms.strip():
        st.warning("Please enter at least one symptom.")
        return
    
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['Symptoms'])
    y = df['Disease Name']
    
    model = LogisticRegression(max_iter=1000)
    model.fit(X, y)
    
    input_vectorized = vectorizer.transform([symptoms])
    prediction = model.predict(input_vectorized)
    
    st.subheader("Predicted Disease:")
    st.write(f"**{prediction[0]}**")
