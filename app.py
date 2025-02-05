import streamlit as st
import pickle
import numpy as np

model_path = "housing_model.pkl"

with open(model_path, "rb") as file:
    model = pickle.load(file)

st.title("Housing Price Prediction")

st.sidebar.header("Input Features")
sqft = st.sidebar.number_input("Square Feet", min_value=500, max_value=10000)
parking = st.sidebar.number_input("parking", min_value=0, max_value=5)
heat_air_conditioning = st.sidebar.number_input("heat_air_conditioning", min_value=0, max_value=2)
Total_rooms = st.sidebar.number_input("Totalrooms(including Bedrooms,Bathrooms,guestrooms)", min_value=0, max_value=10, value = 0)
Extra_features = st.sidebar.selectbox("Furnish Status", ["furnished", "unfurnished", "semi-furnished"])

Extra_features_mapping = {"furnished": 1, "unfurnished": 3, "semi-furnished": 2}
Extra_features_encoded = Extra_features_mapping [Extra_features]
input_data = np.array([[sqft,parking,Extra_features_encoded,heat_air_conditioning,Total_rooms]])

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Predicted Price: ${prediction:,.2f}")

# git branch -M main
# git remote add origin https://github.com/JISHUBISHI/ai_recipie_generadadd.git
# git push -u origin main
