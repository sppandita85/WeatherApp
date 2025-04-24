import streamlit as st
import requests

st.title("This is a weather app")
st.subheader("Hang on Tight, This is a app currently being built for a LLM use case")

city = st.selectbox("Select the city",["Dubai", "London", "California"])

if st.button("Enter"):
    if city:
        cityLatLon = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid=58d77b35aca8a670c0360191ffb1d602")
        cityLatLon= cityLatLon.json()
        cityLat = cityLatLon[0]["lat"]
        cityLon = cityLatLon[0]["lon"]
        result_response = requests.get(f"http://api.weatherapi.com/v1/current.json?key=c274abef19e34018b79115808252404&q={cityLat},{cityLon}")
        result = result_response.json()
        st.write(f"The temperature of the {city} is "+str(result["current"]["temp_c"])+" Celsius")

