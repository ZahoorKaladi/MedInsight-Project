# MedInsight Plus

**MedInsight Plus** is an innovative web application designed to provide health predictions and insights into various diseases. Leveraging advanced predictive modeling techniques, it offers users a convenient way to analyze symptoms and learn about potential health conditions. 

⚠️ **Disclaimer:**  
MedInsight Plus is not a substitute for professional medical advice, diagnosis, or treatment. Please consult a licensed healthcare professional for any medical concerns.

---

## Table of Contents
- [Features](#features)
- [How It Works](#how-it-works)
- [Pages](#pages)
- [Screenshots](#screenshots)
- [Model Evaluation](#model-evaluation)
- [Project Team](#project-team)
- [Connect with Us](#connect-with-us)

---

## Features

- **Symptom Analysis:**  
  Predict diseases based on user-inputted symptoms using a Logistic Regression model.

- **Disease Information:**  
  Fetch detailed descriptions of diseases directly from Wikipedia.

- **Disease Demographics:**  
  Visualize disease trends, age and gender distributions, and co-occurrence heatmaps.

- **Interactive UI:**  
  Powered by **Streamlit**, with responsive design elements and real-time predictions.

---

## How It Works

1. **Dataset:**  
   Utilizes a CSV dataset (`DiseaseDataset.csv`) containing symptoms and disease names.
   
2. **Model Training:**  
   - A **Logistic Regression** model is trained using a `CountVectorizer` for feature extraction.
   - Model performance is evaluated on test data with metrics such as accuracy, classification reports, and confusion matrices.

3. **Predictions:**  
   - Users can input symptoms via text fields or select common symptoms from a sidebar.  
   - Predictions are displayed along with a recommendation to consult a doctor for confirmation.

---

## Pages

### Home Page
- Introduction to MedInsight Plus.
- Information about the application's purpose and limitations.

### Disease Demographics
- Visualizations for disease trends and demographic data:
  - **Disease Frequency** (Bar Chart)
  - **Age Distribution** (Histogram)
  - **Gender Distribution** (Pie Chart)
  - **Blood Pressure vs Cholesterol Levels** (Scatter Plot)
  - **Disease Co-occurrence Heatmap**

### Fetching Information
- Dynamically fetch disease details from **Wikipedia**.
- Stylish animations for user experience.

---

## Screenshots

### Home Page  
![Home Page  MedInsight](https://github.com/user-attachments/assets/a2671560-962f-464a-bbbe-b80b0e75d6af)


### Model Evaluation  
![Model Evualtion](https://github.com/user-attachments/assets/4a3f58bb-91dc-424b-a7b0-46c10ecd9cc7)


### Disease Demographics  
![Disease Demographics](https://github.com/user-attachments/assets/62e849bf-a7c3-4212-838c-cfc8098553cb)


### Fetching Information  
 ![Information Fetching](https://github.com/user-attachments/assets/3aa4e012-5107-4b08-9cb5-0d2226a37fbd)


---

## Model Evaluation

- **Accuracy:** Displays the model's accuracy on test data.  
- **Classification Report:** Provides a detailed performance breakdown.  
- **Confusion Matrix:** Visualizes the performance of the disease prediction model.

---

## Project Team

- **Developer:**  
  Zahoor Ahmed  
  _Final Year Computer Science Student_

- **Team Members:**  
  - Azhar Ali Sahowal  
  - Sanaullah Brohi  
  - Fayaz Laghari  

- **Supervisor:**  
  - Shah Murad Chandio  
    _Assistant Professor_

---

## Connect with Us

Feel free to connect with us on social media:

- [LinkedIn](https://www.linkedin.com/zahoor-ahmed-04b105215)
- [GitHub](https://github.com/ZahoorKaladi)
- [Twitter](https://twitter.com/your-twitter-handle)

---

© 2024 Developed by **Zahoor Ahmed & Team**
