"Advent of Cyber 2023 - Day 04 - Exercises 01 and 02"
from typing import List


def calculate_scratchcard_matched_points(scratchcard: str) -> int:
    """
    Calculate the points for a scratchcard based on matching numbers.

    Parameters:
    - scratchcard (str): The string representing a scratchcard.

    Returns:
    - int: The calculated points for the scratchcard.
    """

    scratchcard_numbers = [int(k) for k in scratchcard.split(": ")[
        1].split(" | ")[1].split()]
    winning_numbers = [int(k) for k in scratchcard.split(": ")[
        1].split(" | ")[0].split()]

    points = 0
    for scratchcard_number in scratchcard_numbers:
        if scratchcard_number in winning_numbers:
            points += 1

    return points


def process_scratchcards_points_based(scratchcards: List[str]) -> int:
    """
    Process scratchcards based on matching numbers and calculate total points.

    Parameters:
    - scratchcards (List[str]): List of strings representing scratchcards.

    Returns:
    - int: The total points for all scratchcards.
    """

    output_sum = 0
    for scratchcard in scratchcards:
        points = calculate_scratchcard_matched_points(scratchcard)
        output_sum += 2 ** (points - 1) if points > 0 else 0
    return output_sum


def process_scratchcards_cards_based(scratchcards: List[str]) -> int:
    """
    Process scratchcards based on winning cards and calculate the total number of cards won.

    Parameters:
    - scratchcards (List[str]): List of strings representing scratchcards.

    Returns:
    - int: The total number of cards won.
    """

    cards_per_scratchcard_number = [1] * len(scratchcards)
    for scratch_id, scratchcard in enumerate(scratchcards):
        points = calculate_scratchcard_matched_points(scratchcard)

        multiplier = cards_per_scratchcard_number[scratch_id]
        for i in range(scratch_id+1, scratch_id+1+points):
            cards_per_scratchcard_number[i] = cards_per_scratchcard_number[i] + multiplier
    print(cards_per_scratchcard_number)
    return sum(cards_per_scratchcard_number)


if __name__ == "__main__":
    with open("./input.txt", encoding="utf-8") as input_file:
        input_items = [k.strip() for k in input_file.readlines()]
        print("===== Scratchcards (Day 04) - Advent of Code 2023  =====")
        print(
            f"The first star result is {process_scratchcards_points_based(input_items)}")
        print(
            f"The second star result is {process_scratchcards_cards_based(input_items)}")
