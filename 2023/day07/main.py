from typing import Tuple, Literal, List
import re
from functools import cmp_to_key

hand_type_lookup_regexes = {
    "five_of_a_kind": r'^(.)\1{4}$',
    "four_of_a_kind": r'(.)\1{3}',
    "full_house": r'((.)\2{2}(.)\3{1})|((.)\5{1}(.)\6{2})',
    "three_of_a_kind": r'(.)\1{2}',
    "two_pair": r'((.)\2{1}.?(.)\3{1})',
    "one_pair": r'((.)\2{1})',
    "high_card": r'.*'
}

strength_order = ["A", "K", "Q", "J", "T",
                  "9", "8", "7", "6", "5", "4", "3", "2"]


def get_stronger_hand(hand_bid_tuple_a: Tuple[str, int], hand_bid_tuple_b: Tuple[str, int]) -> Literal[-1, 1, 0]:
    """
    Compare two hands based on their strength.

    Args:
    - hand_bid_tuple_a (Tuple[str, int]): Tuple containing a hand and its bid.
    - hand_bid_tuple_b (Tuple[str, int]): Tuple containing a hand and its bid.

    Returns:
    - Literal[-1, 1, 0]: -1 if hand_a is stronger, 1 if hand_b is stronger, 0 if equal.
    """

    hand_a, _ = hand_bid_tuple_a
    hand_b, _ = hand_bid_tuple_b

    for index, char in enumerate(hand_a):
        if (strength_order.index(char) < strength_order.index(hand_b[index])):
            return -1  # Left hand is stronger
        elif (strength_order.index(char) > strength_order.index(hand_b[index])):
            return 1  # Right hand is stronger
    return 0  # Both are equally strong


def get_new_hand_type_by_joker_amount(current_hand: str, joker_amount: int) -> str:
    """
    Get the new hand type when considering the presence of jokers.

    Args:
    - current_hand (str): The current hand type.
    - joker_amount (int): The number of jokers in the hand.

    Returns:
    - str: The new hand type.
    """

    if joker_amount == 0:
        return current_hand
    elif joker_amount == 1:
        mapping = {
            "four_of_a_kind": "five_of_a_kind",
            "three_of_a_kind": "four_of_a_kind",
            "two_pair": "full_house",
            "one_pair": "three_of_a_kind",
        }
        return mapping.get(current_hand, "one_pair")
    elif joker_amount == 2:
        mapping = {
            "three_of_a_kind": "five_of_a_kind",
            "one_pair": "four_of_a_kind",
        }
        return mapping.get(current_hand, "three_of_a_kind")
    elif joker_amount == 3:
        mapping = {
            "one_pair": "four_of_a_kind",
        }
        return "five_of_a_kind" if current_hand == "one_pair" else "four_of_a_kind"
    elif joker_amount >= 4:
        return "five_of_a_kind"


def get_hand_type(hand: str, allow_wildcards: bool = False) -> str:
    """
    Determine the type of a given hand.

    Args:
    - hand (str): The hand to be analyzed.
    - allow_wildcards (bool, optional): Whether to consider wildcards (Jokers). Defaults to False.

    Returns:
    - str: The type of the hand.
    """

    joker_amount = list(hand).count("J")
    sorted_hand = ''.join(
        sorted(hand.replace("J", "") if allow_wildcards else hand))

    for hand_type, reg in hand_type_lookup_regexes.items():
        # If regexes return a match, it means the hand type is hand_type
        if bool(re.search(reg, sorted_hand)):
            return get_new_hand_type_by_joker_amount(hand_type, joker_amount) if allow_wildcards else hand_type


def get_total_winnings(plays: List[str], allow_wildcards: bool = False) -> int:
    """
    Calculate the total winnings based on a list of plays.

    Args:
    - plays (List[str]): List of plays, where each play is a string containing a hand and a bid.
    - allow_wildcards (bool, optional): Whether to consider wildcards (Jokers). Defaults to False.

    Returns:
    - int: The total winnings.
    """

    hands_by_type = {
        "five_of_a_kind": [],
        "four_of_a_kind": [],
        "full_house": [],
        "three_of_a_kind": [],
        "two_pair": [],
        "one_pair": [],
        "high_card": [],
    }

    global strength_order
    if (allow_wildcards):
        strength_order = ["A", "K", "Q", "T", "9",
                          "8", "7", "6", "5", "4", "3", "2", "J"]
    else:
        strength_order = ["A", "K", "Q", "J", "T",
                          "9", "8", "7", "6", "5", "4", "3", "2"]

    for play in plays:
        hand, bid = play.split()
        hand_type = get_hand_type(hand, allow_wildcards)
        hands_by_type[hand_type].append((hand, int(bid)))

    for hand_type, hands in hands_by_type.items():
        if (len(hands) > 1):
            hands_by_type[hand_type] = sorted(
                hands_by_type[hand_type], key=cmp_to_key(get_stronger_hand))

    current_rank = len(plays)
    result = 0
    for hand_type, hands in hands_by_type.items():
        for hand in hands:
            result += current_rank * hand[1]
            current_rank -= 1
    return result


if __name__ == "__main__":
    print("===== Camel Cards (Day 07) - Advent of Code 2023  =====")

    try:
        from aocd import get_data
        input_items = get_data(day=7, year=2023).split("\n")
    except Exception as e:
        try:
            with open("./input.txt", encoding="utf-8") as input_file:
                input_items = input_file.readlines()
        except FileNotFoundError:
            print("Could not fetch input data from AoC and input.txt is not present.")
            exit()

    print(
        f"The first star result is {get_total_winnings(input_items)}")
    print(
        f"The second star result is {get_total_winnings(input_items, True)}")
