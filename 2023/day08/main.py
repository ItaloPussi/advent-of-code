"Advent of Cyber 2023 - Day 08 - Exercises 01 and 02"
from typing import Tuple, List, Dict
import re
from math import lcm


def convert_map_to_dict(map_list: list[str]) -> Dict[str, Tuple[str, str]]:
    """
    Converts a map represented as a list of strings into a dictionary where each
    key is a starting position and the corresponding value is a tuple of left and
    right positions.

    Parameters:
    - map_list (list[str]): A list of strings representing the map.

    Returns:
    - Dict[str, Tuple[str, str]]: A dictionary mapping starting positions to
      tuples of left and right positions.
    """

    dict_map = {}

    for line in map_list:
        start, left, right = re.findall(r"(\w{3})", line)
        dict_map[start] = (left, right)

    return dict_map


def get_single_total_steps(position: str, allowed_objectives: List[str], dict_map: Dict[str, Tuple[str, str]], directions: List[str]) -> int:
    """
    Calculates the number of steps needed to reach any of the allowed objectives
    from a given starting position, following the specified directions.

    Parameters:
    - position (str): The starting position.
    - allowed_objectives (List[str]): List of allowed objective positions.
    - dict_map (Dict[str, Tuple[str, str]]): A dictionary mapping starting
      positions to tuples of left and right positions.
    - directions (List[str]): List of directions to follow ("L" or "R").

    Returns:
    - int: The total number of steps needed.
    """

    steps = 0
    current_position = position
    current_direction_index = 0

    while current_position not in allowed_objectives:
        steps += 1

        direction_index = 0
        if directions[current_direction_index] == "R":
            direction_index = 1

        current_position = dict_map[current_position][direction_index]

        current_direction_index = current_direction_index + \
            1 if current_direction_index < len(directions) - 1 else 0

    return steps


def get_person_total_steps(map_list: list[str]) -> int:
    """
    Calculates the total number of steps needed for a person to reach the
    objective on the provided map.

    Parameters:
    - map_list (list[str]): A list of strings representing the map.

    Returns:
    - int: The total number of steps needed for a person to reach the objective.
    """

    directions = list(map_list[0])
    dict_map = convert_map_to_dict(map_list[2:])

    return get_single_total_steps("AAA", "ZZZ", dict_map, directions)


def get_ghost_total_steps(map_list: list[str]) -> int:
    """
    Calculates the total number of steps needed for a ghost to reach the
    objective on the provided map, considering multiple entry points.

    Parameters:
    - map_list (list[str]): A list of strings representing the map.

    Returns:
    - int: The total number of steps needed for a ghost to reach the objective.
    """

    directions = list(map_list[0])
    dict_map = convert_map_to_dict(map_list[2:])

    entry_points = list(filter(lambda x: x[-1] == "A", dict_map.keys()))
    objectives = list(filter(lambda x: x[-1] == "Z", dict_map.keys()))

    steps = [get_single_total_steps(
        k, objectives, dict_map, directions) for k in entry_points]

    return lcm(*steps)


if __name__ == "__main__":
    with open("./input.txt", encoding="utf-8") as input_file:
        input_items = [k.strip() for k in input_file.readlines()]
        print("===== Haunted Wasteland (Day 08) - Advent of Code 2023  =====")
        print(
            f"The first star result is {get_person_total_steps(input_items)}")
        print(
            f"The second star result is {get_ghost_total_steps(input_items)}")
