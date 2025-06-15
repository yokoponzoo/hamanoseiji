import streamlit as st

from libs.config import config

# get page config
page_name = __file__.split("_")[-1].replace(".py", "")
page_config = config["pages"]["research"][page_name]

# title
st.title(page_config["title"])

# はじめに
st.header("はじめに")
st.markdown(
    f"""
    noteにて今回の研究内容の詳細を公開しています。このページでは研究に使用したシミュレーションツールを使えるように公開しております。

    - [noteはこちら](https://note.com/hamanoseiji/n/n128a3d87f05e)
    - [YouTubeはこちら](https://youtube.com/shorts/SmJa8smPpag)
    """
)

# シミュレーションツール
st.header("シミュレーションツール")
st.markdown(
    """
    情報を入力して、シミュレーションを実行してください。
    """
)
