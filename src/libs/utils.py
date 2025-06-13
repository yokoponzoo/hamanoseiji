import streamlit as st

from libs.config import load_config

config = load_config()

# set page config
def set_page_config():
    st.set_page_config(
        page_title=config["pages"]["title"],
    )


# load the custom CSS
def load_css():
    with open(config["css"]) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
