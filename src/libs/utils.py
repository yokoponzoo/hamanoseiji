import socket

import streamlit as st

from libs.config import config


def check_local():
    """check environment is local or not."""
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    print(f"Host Name: {host_name}")
    print(f"Host IP: {host_ip}")
    if host_ip == "localhost" or host_ip == "127.0.0.1":
        return True
    else:
        return False


is_local = check_local()
