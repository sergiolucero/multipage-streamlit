import streamlit as st
import boto3
import glob

st.header('Quant Portfolio')

for fn in sorted(glob.glob('pages/*.png')):
    st.image(fn, caption=fn, use_column_width='always')

uploaded_file = st.file_uploader("upload picture")
if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
     # upload to github
     
