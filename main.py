import streamlit as st

st.title("Weather Forecast for the Next Days")
place = st.text_input(label="Place:")
days = st.slider(label="Forecast Days", min_value=1, max_value=5, help="select the number of forecasted days")
options = st.selectbox(label="Select data to view", options=('Temperature', 'Skies'))
st.subheader(f"{options} for the next {days} in {place}")