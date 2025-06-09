import streamlit as st
import pandas as pd
import joblib

# Set page config
st.set_page_config(page_title="Lagos State House Rent Predictions", layout="centered")

# Load the trained model
model = joblib.load("ipredictor_model.pkl")  # You must train and save the model locally

# App title
st.title("🏠 Lagos State House Rent Predictions")
st.markdown("Predict estimated **yearly rent** based on key features of the house.")

# Sidebar input
st.sidebar.header("Enter House Features")

location = st.sidebar.selectbox("Location", ['Abule Egba', 'Ikeja', 'Lekki', 'Yaba', 'Surulere', 'Ajah'])  # Example values
bedrooms = st.sidebar.slider("Number of Bedrooms", 0, 10, 2)
bathrooms = st.sidebar.slider("Number of Bathrooms", 0, 10, 2)
toilets = st.sidebar.slider("Number of Toilets", 0, 10, 2)
house_type = st.sidebar.selectbox("House Type", ['FLAT', 'SELF CONTAIN', 'DETACHED', 'DUPLEX'])  # Example values

# Prediction button
if st.sidebar.button("Predict Rent"):
    # Create input DataFrame
    input_df = pd.DataFrame({
        'LOCATION': [location],
        'BEDROOMS': [bedrooms],
        'BATHROOMS': [bathrooms],
        'TOILETS': [toilets],
        'HOUSE_TYPE': [house_type]
    })

    # Make prediction
    predicted_price = model.predict(input_df)[0]
    formatted_price = f"₦{int(predicted_price):,}"

    # Display results
    st.success(f"🏡 Estimated Yearly Rent: {formatted_price}")
    st.markdown(f"""
    ### 📝 Explanation:
    - **Location:** {location}  
    - **Bedrooms:** {bedrooms}  
    - **Bathrooms:** {bathrooms}  
    - **Toilets:** {toilets}  
    - **House Type:** {house_type}  
    """)
else:
    st.info("Enter the details in the sidebar and click 'Predict Rent' to get the estimated rent.")

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit | Lagos Rent Prediction Model")
