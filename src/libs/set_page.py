import streamlit as st
from PIL import Image

from libs.config import load_config

config = load_config()

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


# set page navigation
def set_page_info(page_params):
    """Set the pages for navigation."""
    page = st.Page(
        page=page_params["src"],
        title=page_params["title"],
    )
    return page


def set_pages_navigation():
    """Set the pages for navigation."""
    # set profile page
    profile_page = set_page_info(config["pages"]["profile"])

    # set research pages
    research_pages = []
    for page_num in config["pages"]["research"]:
        page_params = config["pages"]["research"][page_num]
        page = set_page_info(page_params)
        research_pages.append(page)
    pg = st.navigation(
        {
            "profile": [profile_page],
            "research": research_pages,
        }
    )
    pg.run()


def set_page():
    """Set the page configuration."""
    # set style
    load_css()

    # sidebar
    # set_sidebar()

    # NOTE: last
    set_pages_navigation()
