"Advent of Cyber 2023 - Day 05 - Exercises 01 and 02"
from typing import List, Tuple
from itertools import groupby


def get_seed_location(seed: int, almanac_maps: List[str]) -> Tuple[int, List[int]]:
    """
    Returns location and the  followed path of a given seed in the almanac maps.

    Parameters:
    - seed (int): The seed to search for.
    - almanac_maps (List[str]): List of almanac maps.

    Returns:
    Tuple[int, List[int]]: A tuple containing the final location of the seed and the path taken.
    """

    path = []
    searched_number = seed
    for almanac_map in almanac_maps[1:]:
        for map_line_index, map_line in enumerate(almanac_map[1:]):
            destination, seed_source, seed_source_amount = [
                int(k) for k in map_line.split()]

            if (searched_number >= seed_source and searched_number <= (seed_source + seed_source_amount)):
                searched_number = destination + (searched_number - seed_source)
                path.append(map_line_index)
                break
    return searched_number, path


def get_minimum_seed_location(almanac: List[str]) -> int:
    """
    Finds the minimum location of a seed in the almanac.

    Parameters:
    - almanac (List[str]): List of almanac maps.

    Returns:
    int: The minimum location of a seed in the almanac.
    """

    almanac_maps = [list(g)
                    for k, g in groupby(almanac, key=lambda x: x != "") if k]

    seeds = [int(k) for k in almanac_maps[0][0].split(": ")[1].split()]
    seeds_locations = [get_seed_location(seed, almanac_maps)[
        0] for seed in seeds]
    return min(seeds_locations)


def range_get_seed_location(range_start, range_end, almanac_parts):
    """
    Finds the seed location in the given range of the almanac.

    Parameters:
    - range_start (int): The start of the range.
    - range_end (int): The end of the range.
    - almanac_parts (List[str]): List of almanac maps.

    Returns:
    None
    """

    stack = [(range_start, range_end)]

    while stack:
        current_range_start, current_range_end = stack.pop()

        if current_range_start > current_range_end:
            continue

        current_range_start_location, current_range_start_path = get_seed_location(
            current_range_start, almanac_parts)
        _, current_range_end_path = get_seed_location(
            current_range_end, almanac_parts)

        # Here is the charm: If both ends of the range shares a same path, it means the in between numbers shares the path too
        if current_range_start_path == current_range_end_path:
            global second_star_min_number
            if current_range_start_location > 0 and (second_star_min_number is None or current_range_start_location < second_star_min_number):
                second_star_min_number = current_range_start_location
            continue

        mid = (current_range_start + current_range_end) // 2
        stack.append((current_range_start, mid - 1))
        stack.append((mid, current_range_end + 1))


second_star_min_number = None


def range_get_seed_min_location(almanac: list[str]) -> int:
    """
    Finds the minimum location of seeds in the almanac within specified ranges.

    Parameters:
    - almanac (List[str]): List of almanac maps.

    Returns:
    int: The minimum location of seeds in the almanac within specified ranges.
    """

    almanac_maps = [list(g)
                    for k, g in groupby(almanac, key=lambda x: x != "") if k]

    seeds = [int(k) for k in almanac_maps[0][0].split(": ")[1].split()]

    for index, seed in enumerate(seeds):
        if (index % 2 == 0):
            range_get_seed_location(seed, seed + seeds[index+1], almanac_maps)
        else:
            continue

    return second_star_min_number


if __name__ == "__main__":
    print("===== If You Give A Seed A Fertilizer (Day 05) - Advent of Code 2023  =====")

    try:
        from aocd import get_data
        input_items = get_data(day=5, year=2023).split("\n")
    except Exception as e:
        try:
            with open("./input.txt", encoding="utf-8") as input_file:
                input_items = input_file.readlines()
        except FileNotFoundError:
            print("Could not fetch input data from AoC and input.txt is not present.")
            exit()

    print(
        f"The first star result is {get_minimum_seed_location(input_items)}")
    print(
        f"The second star result is {range_get_seed_min_location(input_items)}")
