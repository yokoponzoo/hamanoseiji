import streamlit as st

from libs.config import load_config
from libs.set_page import set_page

config = load_config()
set_page()

st.write("Page A")
