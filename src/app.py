import streamlit as st
from PIL import Image

from libs.config import load_config
from libs.utils import load_css, set_page_config

config = load_config()

# set page config
set_page_config()

# set style
load_css()

# プロフィール
image = Image.open(config["profile_img"])
st.image(image)
st.text("浜のせいじ@ポケカ研究員")
