import streamlit as st

import os

x = st.slider('Select a value')
st.write(x, 'squared is', x * x)

video_file = open('112vHirakAlger_09042021_s.mp4', 'rb')

video_bytes = video_file.read()

st.video(video_bytes)
