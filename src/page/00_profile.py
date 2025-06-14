import streamlit as st

from libs.config import load_config
from libs.set_page import set_page

config = load_config()
# set_page()

st.header("概要")
st.markdown(
    """
    浜のせいじ@ポケカ研究員のポケモンカード研究用のWebアプリです。
    ポケモンカードをやっていく中で、気になったことを調査していってます。
    研究内容は、[YouTube](https://www.youtube.com/@hamanoseiji-pokeca)や[note](https://note.com/hamanoseiji)で公開しています。
    ここでは研究内容のシミュレーションや、データの可視化を行うためのツールも提供しているアプリとなっています。
    """
)

# TODO: リスト表示して、検索できるようにする。サイドバーも同様。リストはファイルから取得して表示できるようにする。
st.header("研究一覧")
st.markdown(
    """
    - xxx
    - yyy
    - zzz
    """
)
