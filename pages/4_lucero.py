import streamlit as st
import glob

st.write('Quant Portfolio')

for fn in glob.glob('pages/*.png'):
    st.image(fn)
