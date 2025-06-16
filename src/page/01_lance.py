import streamlit as st

from libs.config import config
from libs.lance import try_sim

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

    - [noteはこちら](https://note.com/hamanoseiji/n/n6e163d697137)
    - [note(シミュレーションコード)はこちら](https://note.com/hamanoseiji/n/nc1670195267b)
    - [YouTubeはこちら](https://youtube.com/shorts/SmJa8smPpag)
    """
)

# シミュレーションツール
st.header("シミュレーションツール")
st.subheader("シミュレーション条件の設定")
## 固定値
deck_num = 60
trial_num = 10
sim_num = 100000

## ユーザー設定値
basic_pokemon_num = st.number_input(
    "タネポケモンの数",
    min_value=1,
    max_value=60,
    value=10,
    step=1,
    help="デッキに入れるタネポケモンの数を入力してください。",
)
lance_num = st.number_input(
    "ランスの数", min_value=0, max_value=4, value=2, step=1, help="デッキに入れるランスの数を入力してください。"
)
reciver_num = st.number_input(
    "ロケット団のレシーバーの数",
    min_value=0,
    max_value=4,
    value=4,
    step=1,
    help="デッキに入れるロケット団のレシーバーの数を入力してください。",
)
pokegear_num = st.number_input(
    "ポケギアの数", min_value=0, max_value=4, value=0, step=1, help="デッキに入れるポケギアの数を入力してください。"
)

# シミュレーション条件
st.subheader("シミュレーション実行")
st.markdown(
    f"""
    【シミュレーション条件】
    - 固定条件:
        - デッキの数: {deck_num}枚
        - 試行回数: {trial_num}回
        - シミュレーション回数: {sim_num}回
    - ユーザー設定値:
        - タネポケモンの数: **{basic_pokemon_num}匹**
        - ランスの数: **{lance_num}枚**
        - ロケット団のレシーバーの数: **{reciver_num}枚**
        - ポケギアの数: **{pokegear_num}枚**
    """
)

if st.button("シミュレーション実行", type="primary"):
    # 60枚かチェック
    if basic_pokemon_num + lance_num + reciver_num + pokegear_num > deck_num:
        st.write("デッキの合計枚数が60枚を超えています。設定を見直してください。")
        st.write("現在の枚数:", basic_pokemon_num + lance_num + reciver_num + pokegear_num)
    else:
        # run simulation
        sim_results_raw, df_sim_result_summary = try_sim(
            trial_num,
            sim_num,
            deck_num,
            basic_pokemon_num,
            lance_num,
            reciver_num,
            pokegear_num,
        )

        # シミュレーション結果の表示
        success_rate = 100 * df_sim_result_summary["success_rate"].mean()
        success_rate_std = 100 * df_sim_result_summary["success_rate"].std()
        st.write(f"成功率: {success_rate:.2f}% ± {success_rate_std:.2f}%")
