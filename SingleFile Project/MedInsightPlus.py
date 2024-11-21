
import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import time

def ai_typewriter(text: str, speed: int):
    container = st.empty()

    # Add CSS to create a smooth scrolling animation and AI type font style
    st.markdown(
        f"""
        <style>
            #stContainer {{
                font-family: 'IBM Plex Mono', monospace; /* AI type font style */
                overflow: hidden;
                white-space: nowrap;
                animation: type {speed}s steps(40, end);
            }}
            @keyframes type {{
            
                from {{ width: 0; }}
                to {{ width: 100%; }}
            }}
        </style>
        """,
        unsafe_allow_html=True
    )

    for index in range(len(formatted_information) + 1):
        curr_full_text = formatted_information[:index]
        container.markdown(curr_full_text, unsafe_allow_html=True)
        time.sleep(1 / speed)

# Load the dataset
df = pd.read_csv('DiseaseDataset.csv', encoding='ISO-8859-1')

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['Symptoms'], df['Disease Name'], test_size=0.2, random_state=42)

# Use CountVectorizer to convert symptoms into numerical features
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)

# Train a Logistic Regression classifier
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vectorized, y_train)

# Common symptoms to be added automatically
common_symptoms = ["Fever", "chills", "sweats", "fatigue", "High fever", "severe", "headache", "muscle", "joint pain", "rash", "fatigue"]

html_content = """
<div class="title-container">
  <h1>

  </h1>
</div>
"""
st.title("MedInsight Plus")
st.header("Disclaimer")
st.write("""
  MedInsight Plus - Your Digital Health Companion
         
MedInsight Plus is an innovative web application designed to provide health predictions and information related to various diseases. It utilizes advanced predictive modeling techniques to offer insights into potential health conditions based on user inputs. However, it is important to note that MediInsight Plus is not a substitute for professional medical advice, diagnosis, or treatment.
""")

# Sidebar with checkboxes for common symptoms
selected_symptoms = st.sidebar.multiselect("Select Common Symptoms", common_symptoms)
# Sidebar with checkboxes for common diseases
selected_diseases = st.sidebar.selectbox("Select Diagnosed Diseases", df['Disease'].unique())
# Main section for entering new symptoms
st.header("Enter New Symptoms")
new_symptoms = st.text_area("Enter symptoms (comma-separated)", ", ".join(selected_symptoms), key='new_symptoms', placeholder="e.g., Chills, Body aches")

# Option to enter additional symptoms
add_symptoms = st.text_input("Enter additional symptoms (comma-separated)", placeholder="e.g., Fever, Cold")

# Combine common symptoms, user-entered symptoms, and additional symptoms
all_symptoms = selected_symptoms + [symptom.strip() for symptom in new_symptoms.split(',')] + [symptom.strip() for symptom in add_symptoms.split(',')]

if st.button("Predict"):
    # Validate if symptoms are selected or entered
    if not new_symptoms:
        st.warning("Please select or enter at least one symptom.")
    else:
        # Display a loader while making predictions
        with st.spinner('Analyzing symptoms, please wait...'):
            time.sleep(5)
            st.write('Fetching predictions ...',)
            time.sleep(1)
            st.write("Processing information ...",)
            time.sleep(2)
            st.write("Predicting disease ...",)
            time.sleep(3)
            st.success('Diagnosed', icon="✅") # expanded=False)

            # Preprocess new symptoms
            new_symptoms_vectorized = vectorizer.transform([", ".join(all_symptoms)])

            # Make predictions on the new symptoms
            new_prediction = model.predict(new_symptoms_vectorized)

            # Replace the loader with the predicted disease in bold and large font
            st.subheader("Predicted Disease:")
            st.markdown(
                f"**{new_prediction[0]}**. Please note that this is a predicted disease. It's recommended to consult with a doctor for further evaluation.",
                unsafe_allow_html=True)

import streamlit as st
import requests
import wikipediaapi

# Streamlit App
st.header(" Disease Information ")

# Input for disease
disease_name = st.text_input("Enter Diagnosed Disease", "".join(selected_diseases), key='Disease', placeholder="e.g., Malaria, Dengue")
# st.text_input('Enter the Disease Name ') # Replace the text input with a select box using disease_name variable

st.write(f"{disease_name}")

# Function to fetch information about the disease from Wikipedia
def get_disease_info(disease):
    try:
        # Set User-Agent header with your Wikimedia username and contact information
        headers = {
            'User-Agent': 'Zahoor Kaladi /1.0 (zahoorkaladi19@gmail.com)'
        }
        wiki_wiki = wikipediaapi.Wikipedia('en', headers=headers)
        page_py = wiki_wiki.page(disease)
        return page_py.text  # Displaying the first 500 characters of the Wikipedia page

    except Exception as e:
        return f"Error fetching information: {str(e)}"


# Display information when the button is pressed
if st.button('Fetch Information'):

    if disease_name:
        information = get_disease_info(disease_name)
        # Displaying the formatted information
        with st.spinner('Fetching Informations, please wait...'):
            time.sleep(4)
        st.write('Fetching informations ...',)
        time.sleep(3)
        st.write("Processing information ...",)
        time.sleep(2)

        st.subheader("Information about the Disease:")
        st.success('Processed', icon="✅")
        speed = 20
        text=formatted_information = f"<div style='border: 2px solid #0DA27D; padding: 10px; color: white; font-family: 'Roboto',sans-sarif;font-size:16px;font-weight:normal;line-height:1.5;'>{information}</div>"
        ai_typewriter(text=text, speed=speed)

        st.markdown(formatted_information, unsafe_allow_html=True)
    else:
        st.warning('Please enter a disease name ')

# Display model evaluation results
st.title("Model Evaluation Results")
y_pred = model.predict(vectorizer.transform(X_test))
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)

st.write(f"Accuracy: {accuracy:.2%}")
st.write("Classification Report:\n", classification_rep)
st.write("Confusion Matrix:\n", confusion_mat)


import streamlit as st

css_styles = """
<style>
body {
  padding: 0;
  margin: 0;
  background-color: #f0f0f0;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

h1 {
  color: #3498db;
  font-size: 3em;
  font-weight: bold;
  font-family: 'Roboto', sans-serif;
  letter-spacing: 2px;
  text-align: center;
  margin: 0;
  padding: 0;
  white-space: nowrap;
  overflow: hidden;
  animation: typing 3s steps(25) infinite;
}

@keyframes typing {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}

.title-container {
  animation: titleAnimation 2s infinite;
}

@keyframes titleAnimation {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.1);
  }
}
</style>
"""
css_styles = """
<style>
/* Base */
body {
  padding: 0;
  margin: 0;
  background-color: #000;
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
}

h1 {
  color: hsl(0, 0%, 28%);
  font-size: 50px;
  font-weight: bold;
  font-family: monospace;
  letter-spacing: 7px;
  cursor: pointer;
}

h1 span {
  transition: 0.5s ease-out;
}

h1:hover span:nth-child(1) {
  margin-right: 5px;
}

h1:hover span:nth-child(1):after {
  content: "'";
}

h1:hover span:nth-child(2) {
  margin-left: 30px;
}

h1:hover span {
  color: #fff;
  text-shadow: 0 0 10px #fff, 0 0 20px #fff, 0 0 40px #fff;
}
</style>
"""

html_content = """
<h1>

</h1>
"""

st.markdown(css_styles, unsafe_allow_html=True)
st.markdown(html_content, unsafe_allow_html=True)
import streamlit as st
import pandas as pd
import plotly.express as px

# Function to generate Disease Demographic page
def disease_demographic_page():
    # Load the dataset
    df = pd.read_csv('DiseaseInfo.csv')

    # Sidebar for user interaction
    selected_disease = st.sidebar.selectbox("Select Disease", df['Disease'].unique())

    # Bar Chart for Disease Frequency
    st.subheader("Disease Frequency")
    disease_frequency = df['Disease'].value_counts()
    st.bar_chart(disease_frequency)

    # Age Distribution
    st.subheader("Age Distribution")
    age_distribution = px.histogram(df, x='Age', color='Disease', nbins=20)
    st.plotly_chart(age_distribution)

    # Gender Distribution
    st.subheader("Gender Distribution")
    gender_distribution = px.pie(df, names='Gender', title='Gender Distribution')
    st.plotly_chart(gender_distribution)

    # Blood Pressure and Cholesterol Levels Scatter Plot
    st.subheader("Blood Pressure vs Cholesterol Levels")
    scatter_plot = px.scatter(df, x='Blood Pressure', y='Cholesterol Level', color='Disease', size='Age')
    st.plotly_chart(scatter_plot)

    # Disease Co-occurrence Heatmap
    st.subheader("Disease Co-occurrence Heatmap")
    co_occurrence_matrix = df.groupby(['Disease', 'Disease Name']).size().unstack().fillna(0)
    heatmap = px.imshow(co_occurrence_matrix, labels=dict(x="Disease", y="Disease Name", color="Frequency"))
    st.plotly_chart(heatmap)

# Streamlit App
st.title("Disease Demographics")

# ... (rest of your code)

# Sidebar with option to select pages
selected_page = st.sidebar.radio("Select Page", ["Home", "Disease Demographic"])

# Show the selected page
if selected_page == "Disease Demographic":
    disease_demographic_page()
else:
    st.write('Welcome Home')

    st.markdown("---")

# Footer with Social Links
import streamlit as st

# Title and Introduction
st.header("Final Year Project: MedInsight Plus")
st.write("- A Project by : Zahoor Ahmed (Developer) and Team")

# Team Members
st.header("Team Members:")
st.write("- Azhar Ali Sahowal")
st.write("- Sanaullah Brohi ")
st.write("- Fayaz Laghari  ")

# Project Supervisor
st.header("Project Supervisor:")
st.write("- Shah Murad Chandio")
st.write("- Assistant Professor")

# Rest of Your Streamlit App
# ...

# Footer with Social Links
st.markdown("---")  # Horizontal line for visual separation
st.header("Connect with Us:")
st.write("Feel free to connect with us on social media:")
st.markdown("[LinkedIn](https://www.linkedin.com/zahoor-ahmed-04b105215)")
st.markdown("[GitHub](https://github.com/https:/ZahoorKaladi)")
st.markdown("[Twitter](https://twitter.com/your-twitter-handle)")
# Add other social links as needed

st.markdown("© 2024 Developed By Zahoor Ahmed & Team")
