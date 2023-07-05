import streamlit as st
from PIL import Image
import requests


header_image = Image.open('references/header.png')
st.image(header_image)
st.title("Concrete Mix Design Regression")
st.subheader("Just enter variable below then clik predict button")

# create form
with st.form(key="Concrete_Regression_Form"):
    Cement = st.number_input(
        label = "1. Input your Cement Value (kg/m3):",
        help = "Example value: 530.2"
    )

    Fly_Ash = st.number_input(
        label = "2. Input your Fly Ash Value (kg/m3):",
        help = "Example value: 0 if you don't use it"
    )

    Water = st.number_input(
        label = "3. Water Value (kg/m3):",
        help = "Example value: 150.3"
    )

    Superplasticizer = st.number_input(
        label = "4. Input your Superplasticizer Value (kg/m3):",
        help = "Example value: 0 if you don't use it"
    )
    
    Coarse_Aggregate = st.number_input(
        label = "5. Input your Coarse Aggregate Value (kg/m3):",
        help = "Example value: 1040.6"
    )

    Fine_Aggregate = st.number_input(
        label = "6. Input your Fine Aggregate Value (kg/m3):",
        help = "Example value: 675.5"
    )

    Age = st.number_input(
        label = "7. Input your Age Value (Day):",
        help = "Example value: 7/14/28"
    )

    # button submit
    submitted = st.form_submit_button('predict!')

    if submitted:
        # collect data from form
        form_data = {
            "Cement": Cement,
            "Fly_Ash": Fly_Ash,
            "Water": Water,
            "Superplasticizer": Superplasticizer,
            "Coarse_Aggregate": Coarse_Aggregate,
            "Fine_Aggregate": Fine_Aggregate,
            "Age": Age
        }
        
        # sending the data to api service
        with st.spinner("Sending data to prediction server... please wait..."):
            predict_url = "http://127.0.0.1:8000/conc_predict"
            res = requests.post(predict_url, json= form_data).json()

        # parse the prediction result
        if res['status'] == 200:
            st.success(f"Concrete Strength Prediction is: {res['prediction']} MPA")
        else:
            st.error(f"ERROR predicting the data.. please check your code {res}")


