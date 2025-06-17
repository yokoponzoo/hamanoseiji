import math

import pandas as pd


# 山札の上からn枚引いた時にあたりのカードがあたる確率を計算する関数
def calc_probability(draw_num, deck_size, target_count):
    # 引数の出力
    # print(f"引く枚数: {draw_num}, デッキの枚数: {deck_size}, あたりのカードの枚数: {target_count}")

    # あたりのカードがない場合は確率0
    if target_count <= 0:
        return 0.0

    # デッキの枚数がdraw_numより少ない場合は確率1
    if draw_num >= deck_size:
        return 1.0

    # デッキの数<=あたりの数の場合は確率1
    if deck_size <= target_count:
        return 1.0

    # 余事象で確率を計算
    # デッキからdraw_num枚を引く方法の総数
    total_ways = math.comb(deck_size, draw_num)

    # あたりのカードがない場合の組み合わせ
    non_target_count = deck_size - target_count
    non_target_ways = math.comb(non_target_count, draw_num)
    # あたりのカードが引かれない確率
    probability_no_target = non_target_ways / total_ways
    # あたりのカードが引かれる確率
    probability = 1 - probability_no_target

    return probability


def run_simulation(draw_num, deck_size_max, target_count_max):
    """
    シミュレーションを実行し、各パラメータの組み合わせで確率を計算する関数
    :param draw_num: 引く枚数
    :param deck_size_max: デッキの最大枚数
    :param target_count_max: あたりのカードの最大枚数
    :return: 確率を計算した結果のDataFrame
    """
    # 各パラメータの組み合わせで確率を計算
    results = []
    for deck_size in range(deck_size_max + 1):
        for target_count in range(1, target_count_max + 1):
            probability = calc_probability(draw_num, deck_size, target_count)
            results.append(
                {
                    "deck_size": deck_size,
                    "target_count": target_count,
                    "probability": probability,
                }
            )

    # 結果をDataFrameに変換
    df = pd.DataFrame(results)

    # 縦にデッキサイズ, 横にあたりの数で確率を表示
    pivot_df = df.pivot(index="deck_size", columns="target_count", values="probability")
    return pivot_df
