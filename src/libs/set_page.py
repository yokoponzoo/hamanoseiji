import streamlit as st
from PIL import Image

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


# set sidebar
def set_sidebar():
    """Set the sidebar configuration."""
    # profile image
    image = Image.open(config["profile_img"])
    st.sidebar.image(
        image,
        caption="浜のせいじ@ポケカ研究員",
    )

    # sidebar links
    st.sidebar.markdown(
        """
        - [youtube](https://www.youtube.com/@hamanoseiji-pokeca)
        - [note](https://note.com/hamanoseiji)
        - [twitter](https://x.com/hamanoseiji)
        """
    )


def set_page():
    """Set the page configuration."""
    # set page config
    set_page_config()

    # set style
    load_css()

    # sidebar
    set_sidebar()
