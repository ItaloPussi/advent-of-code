"Advent of Cyber 2023 - Day 06 - Exercises 01 and 02"
from typing import List
import math


def get_race_ways_to_beat_record_count(t: int, d: int) -> int:
    """
    Calculate the number of ways to beat a race record given the time 't' and distance 'd'.

    Parameters:
    - t (int): The time taken to complete the race.
    - d (int): The distance of the race.

    Returns:
    int: The number of ways to beat the race record.
    """

    # The calculated formula is: -x² + tx -d
    a = -1
    b = t
    c = -d

    delta = math.sqrt((b ** 2) - 4 * a * c)
    record_min_bound = (-b + delta) / -2
    record_max_bound = (-b - delta) / -2

    # Round the results to absolute seconds
    # and cut 1 from each edge (since we only want > and not =)
    return math.ceil(record_max_bound - 1) - math.floor(record_min_bound + 1) + 1


def get_total_ways_to_beat_record_count(race_items: List[str], single_race=False):
    """
    Calculate the total number of ways to beat race records based on input race items.

    Parameters:
    - race_items (List[str]): A list containing two strings representing times and distances of races.
    - single_race (bool, optional): If True, consider the input as only big single race. Defaults to False.

    Returns:
    int: The total number of ways to beat race records.
    """

    times = race_items[0].split(":")[1].split()
    distances = race_items[1].split(":")[1].split()

    if single_race:
        times = [int(''.join(times))]
        distances = [int(''.join(distances))]
    else:
        times = [int(k) for k in times]
        distances = [int(k) for k in distances]

    total_ways = 0
    for index, time in enumerate(times):
        race_ways_count = get_race_ways_to_beat_record_count(
            time, distances[index])
        if total_ways == 0:
            total_ways = race_ways_count
        else:
            total_ways *= race_ways_count
    return total_ways


if __name__ == "__main__":
    with open("./input.txt", encoding="utf-8") as input_file:
        input_items = [k.strip() for k in input_file.readlines()]
        print("===== Wait For It (Day 06) - Advent of Code 2023  =====")
        print(
            f"The first star result is {get_total_ways_to_beat_record_count(input_items)}")
        print(
            f"The second star result is {get_total_ways_to_beat_record_count(input_items, single_race=True)}")
