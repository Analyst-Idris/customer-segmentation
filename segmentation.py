import streamlit as st
import pandas as pd
import numpy as np
import joblib 

kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")


st.title("Customer Segmentation App")   
st.write("Enter customer details to predict their segment:")    


age = st.number_input("Age", min_value=18, max_value=100, value=35)
income = st.number_input("Annual Income (k$)", min_value=0, max_value=200000, value=50000)
Total_spending = st.number_input("Total Spending (sum of purchases)",  min_value= 0, max_value=5000, value=1000)
num_web_purchases = st.number_input("Number of Web Purchases", min_value=0, max_value=100, value=10)
num_store_purchases = st.number_input("Number of Store Purchases", min_value=0, max_value=100, value=5)
num_web_visits = st.number_input("Number of Web Visits per Month", min_value=0, max_value=50, value=3)
recency = st.number_input("Recency (days since last purchase)", min_value=0, max_value=365, value=30)




input_data = pd.DataFrame({
    "Age": [age],
    "Income": [income],
    "Total_Spending": [Total_spending],
    "NumWebPurchases": [num_web_purchases],
    "NumStorePurchases": [num_store_purchases],
    "NumWebVisitsMonth": [num_web_visits],
    "Recency": [recency]
})


input_scaled = scaler.transform(input_data)

if st.button("Predict Segment"):

    cluster_map = {
    0: "Price-Sensitive Occasional Customers",
    1: "Stable Loyal Customers",
    2: "At-Risk Premium Customers",
    3: "Dormant Low-Value Customers",
    4: "VIP Champions",
    5: "Omni-Channel Enthusiasts"
}
    cluster_label = kmeans.predict(input_scaled)[0]
    segment_name = cluster_map.get(cluster_label, "Unknown Segment")
    st.success(f"The customer belongs to Segment {segment_name}") 
    st.info("This classification is based on customer spending behavior, income level, and engagement patterns.") 