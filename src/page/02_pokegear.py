import seaborn as sns
import streamlit as st

from libs.config import config
from libs.pokegear import run_simulation

# get page config
page_name = __file__.split("_")[-1].replace(".py", "")
page_config = config["pages"]["research"][page_name]

# title
st.title(page_config["title"])

# はじめに
st.header("はじめに")
st.markdown(
    f"""
    noteにて今回の研究内容の詳細を公開していますので、まずはそちらをご覧ください。
    このページでは研究に使用したシミュレーションツールを使えるように公開しております。

    - [noteはこちら](https://note.com/hamanoseiji/n/n128a3d87f05e)
    - [YouTubeはこちら](https://youtube.com/shorts/VCPk9M2U2VU)
    """
)

# シミュレーションツール
st.header("シミュレーションツール")

# シミュレーション条件の設定
st.subheader("シミュレーション条件の設定")
card_type = st.radio(
    "シャリタツとポケギアのどちらでシミュレーションを行うか選択してください。",
    ["シャリタツ", "ポケギア"],
)

if card_type == "シャリタツ":
    draw_num = 6
else:
    draw_num = 7


deck_size_max = st.slider("デッキの最大枚数を選択してください", 1, 60, 20)
target_count_max = st.slider("あたりのカードの最大枚数を選択してください", 1, 8, 4)

# シミュレーション条件
st.subheader("シミュレーション実行")
st.markdown(
    f"""
    以下の条件でシミュレーションを実行します。
    - カードタイプ: {card_type} ({draw_num}枚引き)
    - デッキ枚数: 0~{deck_size_max}
    - あたりのカードの枚数: 1~{target_count_max}
    """
)

if st.button("シミュレーション実行", type="primary"):
    pivot_df = run_simulation(draw_num, deck_size_max, target_count_max)
    st.subheader("シミュレーション結果")
    st.markdown(
        f"""
        縦軸はデッキの枚数、横軸はあたりのカードの枚数で、各セルには当たりが引ける確率が表示されています。
        """
    )
    # DataFrameを表示
    st.dataframe(pivot_df)

    # matplotlibでヒートマップを表示
    plot = sns.heatmap(
        pivot_df,
        annot=True,
        fmt=".1%",
        cmap="Greens",
        cbar_kws={"label": "Probability"},
        vmin=0,
        vmax=1,
    )
    st.pyplot(plot.figure)
