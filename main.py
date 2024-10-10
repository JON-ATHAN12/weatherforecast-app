import streamlit as st
import plotly.express as px
from backend import get_data

st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place:")
days = st.slider(label="Forecast Days", min_value=1, max_value=5,
                 help="select the number of forecasted days")
option = st.selectbox(label="Select data to view",
                       options=('Temperature', 'Sky'))
st.subheader(f"{option} for the next {days} in {place}")

if place:
    # Getting the data:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperature = [dict['main']['temp'] for dict in filtered_data]
        dates = [dict["dt_txt"] for dict in filtered_data]
        figure = px.line(x=dates, y=temperature, labels={'x': "Dates", 'y': "Temperature (C)"})
        st.plotly_chart(figure)
    if option == "Sky":
        images = {"Clear": "images/clear.png", "Clouds": "images/cloud.png",
                  "Rain": "images/rain.png", "Snow": "images/snow.png"}
        sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        st.image(image_paths, width=115)

