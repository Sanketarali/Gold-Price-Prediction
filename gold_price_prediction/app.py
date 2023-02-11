import streamlit as st
import joblib

model = joblib.load('gold_price_final')

st.title("Gold Priice Prediction")

spx = st.number_input("SPX")
uso = st.number_input("USO")
slv = st.number_input("SLV")
eur_usd = st.number_input("EUR/USD")


if st.button("Predict"):
   
   
    result = model.predict([[spx,uso,slv,eur_usd]])
    st.write("Gold Price:" , result[0])
