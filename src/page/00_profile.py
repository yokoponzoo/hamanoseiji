import pandas as pd
import streamlit as st

from libs.config import config
from libs.utils import is_local

st.header("概要")
st.markdown(
    """
    浜のせいじ@ポケカ研究員のポケモンカード研究用のWebアプリです。
    ポケモンカードをやっていく中で、気になったことを調査していってます。
    研究内容は、[YouTube](https://www.youtube.com/@hamanoseiji-pokeca)や[note](https://note.com/hamanoseiji)で公開しています。
    ここでは研究内容のシミュレーションや、データの可視化を行うためのツールも提供しているアプリとなっています。
    """
)

st.header("研究一覧")

# research pages
df_research = []
for page_name in config["pages"]["research"]:
    # get page info
    page_title = config["pages"]["research"][page_name]["title"]
    if is_local:
        page_url = f"http://localhost:8501/{page_name}"
    else:
        page_url = f"https://{config['host_name']}/{page_name}"

    df_research.append([page_title, page_url])
df_research = pd.DataFrame(df_research, columns=["記事", "URL"])

st.dataframe(
    df_research,
    use_container_width=True,
    column_config={"URL": st.column_config.LinkColumn(display_text="記事")},
)
