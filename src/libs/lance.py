import random

import pandas as pd
import streamlit as st


def draw(hand, deck, draw_count):
    """
    Draw cards from the deck and add them to the hand.
    :param hand: List of cards in hand
    :param deck: List of cards in the deck
    :param draw_count: Number of cards to draw
    :return: Updated hand and deck
    """
    for _ in range(draw_count):
        if len(deck) > 0:
            card = deck.pop(0)
            hand.append(card)
        else:
            # print("Deck is empty, cannot draw more cards.")
            break
    return hand, deck


def sim(deck_num, basic_pokemon_num, lance_num, reciver_num, pokegear_num):
    """
    Simulate a card game scenario.
    :param deck_num: Total number of cards in the deck
    :param basic_pokemon_num: Number of basic Pokemon cards
    :param lance_num: Number of Lance cards
    :param reciver_num: Number of Reciver cards
    :param pokegear_num: Number of Pokegear cards
    :return: Simulation result
    """
    # create deck
    sim_deck_origin = (
        ["basic_pokemon"] * basic_pokemon_num
        + ["lance"] * lance_num
        + ["reciver"] * reciver_num
        + ["pokegear"] * pokegear_num
        + ["anything"]
        * (deck_num - basic_pokemon_num - lance_num - reciver_num - pokegear_num)
    )

    # prepare hand
    ready = False
    maligan = 0
    while not ready:
        # draw 7 cards
        hand = []
        sim_deck = sim_deck_origin.copy()

        # shuffle deck
        random.shuffle(sim_deck)

        # draw 7 cards
        hand, sim_deck = draw(hand, sim_deck, 7)

        # check if hand has basic_pokemon
        if "basic_pokemon" in hand:
            ready = True
        else:
            maligan += 1

    # set side card
    side = []
    side_count = 6
    side, sim_deck = draw(side, sim_deck, side_count)

    # draw 1 card
    hand, sim_deck = draw(hand, sim_deck, 1)

    # judge
    success = False
    success_detail = ""
    if "lance" in hand:
        success = True
        success_detail = "lance in hand"
    elif "reciver" in hand and "lance" in sim_deck:
        success = True
        success_detail = "reciver in hand and lance in deck"
    elif "pokegear" in hand and "lance" in sim_deck[:7]:
        success = True
        success_detail = "pokegear in hand and lance in deck[:7]"

    # create result
    result = {
        "success": success,
        "success_detail": success_detail,
        "hand": hand,
        "deck": sim_deck,
        "side": side,
        "maligan": maligan,
        "deck_num": deck_num,
        "basic_pokemon_num": basic_pokemon_num,
        "lance_num": lance_num,
        "reciver_num": reciver_num,
        "pokegear_num": pokegear_num,
    }

    return result


def try_sim(
    trial_num,
    sim_num,
    deck_num,
    basic_pokemon_num,
    lance_num,
    reciver_num,
    pokegear_num,
):
    """
    Run multiple simulations and summarize the results.
    :param trial_num: Number of trials
    :param sim_num: Number of simulations per trial
    :param deck_num: Total number of cards in the deck
    :param basic_pokemon_num: Number of basic Pokemon cards
    :param lance_num: Number of Lance cards
    :param reciver_num: Number of Reciver cards
    :param pokegear_num: Number of Pokegear cards
    :return: Raw simulation results and summary DataFrame
    """
    # init
    sim_results_raw = []
    df_sim_result_summary = []

    count = 0
    progress_count = count / (trial_num)
    print(f"{count} / {trial_num}")
    progress_bar = st.progress(progress_count, text=f"{count} / {trial_num}")

    # run simulation
    for i in range(trial_num):
        # print("trial", i)
        success = 0
        for j in range(sim_num):
            sim_result = sim(
                deck_num, basic_pokemon_num, lance_num, reciver_num, pokegear_num
            )
            sim_result["trial_no"] = i
            sim_result["sim_no"] = j
            sim_results_raw.append(sim_result)

            if sim_result["success"]:
                success += 1

        # create summary
        df_tmp_sim_result_summary = pd.DataFrame(
            columns=[
                "deck_num",
                "basic_pokemon_num",
                "lance_num",
                "reciver_num",
                "pokegear_num",
                "trial_no",
                "sim_num",
                "success_num",
                "success_rate",
            ],
            data=[
                [
                    deck_num,
                    basic_pokemon_num,
                    lance_num,
                    reciver_num,
                    pokegear_num,
                    i,
                    sim_num,
                    success,
                    success / sim_num,
                ]
            ],
        )
        df_sim_result_summary.append(df_tmp_sim_result_summary)

        # update progress bar
        count += 1
        progress_count = count / (trial_num)
        progress_bar.progress(progress_count, text=f"{count} / {trial_num}")
        print(f"{count} / {trial_num}")

    # create summary dataframe
    df_sim_result_summary = pd.concat(df_sim_result_summary, ignore_index=True)

    return sim_results_raw, df_sim_result_summary
