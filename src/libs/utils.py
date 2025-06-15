import os

import streamlit as st

from libs.config import config


def check_local():
    """check environment is local or not."""
    # get environment variable STREAMLIT_ENV
    env = os.getenv("STREAMLIT_ENV")
    if env == "local":
        return True
    else:
        return False


is_local = check_local()
