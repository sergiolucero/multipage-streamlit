import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)

pending = ['mapabicis','gasolina','television','greenpeace','IPSA']

def run():
    st.set_page_config(
        page_title="Portfolio Quant.cl",
        page_icon="👋",
        layout="wide"
    )

    st.write("# Demos Streamlit! 👋")
    #st.write(str(pending))
    st.sidebar.success("Elige una demo.")

    st.markdown(
        """
        ### See more complex demos
        -  [analyze the Udacity Self-driving Car Image
          Dataset](https://github.com/streamlit/demo-self-driving)
        - Explore a [New York City rideshare dataset](https://github.com/streamlit/demo-uber-nyc-pickups)
    """
    )


if __name__ == "__main__":
    run()
