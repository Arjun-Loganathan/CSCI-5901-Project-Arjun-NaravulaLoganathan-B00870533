# Reference:
# [1] alvarobartt, “tensorflow-serving-streamlit/ui.py at master · alvarobartt/tensorflow-serving-streamlit,” GitHub, 2021. https://github.com/alvarobartt/tensorflow-serving-streamlit/blob/master/src/streamlit/ui.py.


import streamlit as st

import requests
model_server_url = 'http://localhost:8501/v1/models/ibm-hr-analysis-attrition-dataset:predict'

st.title("Build the UI using Streamlit for this Project ✨🖼️")
st.header("Lets predict the attrition rate")

with st.form("Attrition Analysis"):
    st.write("Inside the form")
    busines_travel = st.text_input('Business Travel', 'Example: Travel_Frequently or Travel_Rarely')
    department = st.text_input('Department', 'Example: Research & Development or Sales or Human Resources')
    education_field = st.text_input("Education Field",'Example: Life Sciences or Medical or Marketing or Technical Degree or Other')
    gender = st.text_input("Gender", 'Example: Male or Female')
    job_role = st.text_input("Job Role",'Example: Sales Executive or Research Scientist or Laboratory Technician or Manufacturing Director or Healthcare Representative')
    marital_status = st.text_input("Marital Status", 'Example: Single or Married or Divorced')


    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        def predict():
            json_data = {
                'signature_name': 'serving_default',
                'instances':  [{
                    "Business Travel": [busines_travel],
                    "Department": [department],
                    "Education Field": [education_field],
                    "Gender": [gender],
                    "Job Role": [job_role],
                    "Marital Status": [marital_status]
                }]
            }
            resp = requests.post(model_server_url, json=json_data)
            return resp.json()

        pred = predict()  # request with a single example
        probs = pred['predictions'][0][0]
        print(f'\tPositive: {probs:.2f} Negative: {1-probs:.2f}')

        st.write("Outside the form")
