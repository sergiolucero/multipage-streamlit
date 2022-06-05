import streamlit as st
import glob

st.header('Quant Portfolio')

for fn in sorted(glob.glob('pages/*.png')):
    st.image(fn, caption=fn)
