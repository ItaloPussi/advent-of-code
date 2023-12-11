"Advent of Cyber 2023 - Day 11 - Exercises 01 and 02"
from typing import List, Tuple
from itertools import combinations


def expand_columns(universe: List[str], expand_factor: int):
    """
    Expands empty columns in the universe by the specified factor.

    Parameters:
    - universe (List[str]): The 2D list representing the cosmic universe.
    - expand_factor (int): The factor by which to expand columns.

    Returns:
    None
    """

    current_column = 0

    # If all the elements in that column are spaces (.), expand it by the expand_factor
    while current_column < len(universe[0]):
        column_values = [row[current_column] for row in universe]
        only_spaces_in_column = set(column_values) == {"."}
        if only_spaces_in_column:
            for row_index, row in enumerate(universe):
                universe[row_index].insert(
                    current_column, (".", expand_factor-1))
            current_column += 1
        current_column += 1


def expand_and_compress_columns(universe: List[str], expand_factor: int) -> List[Tuple[List[Tuple[str, int]], int]]:
    """
    Expands and compresses columns in the universe.

    Parameters:
    - universe (List[str]): The 2D list representing the cosmic universe.
    - expand_factor (int): The factor by which to expand columns.

    Returns:
    List[Tuple[List[Tuple[str, int]], int]]: Compressed columns universe.
    """

    expand_columns(universe, expand_factor)
    compressed_cols_universe = []

    for row in universe:
        # Compress consecutive values into a single tuple where the first element is the value and the second is how much it repeats
        current_column = 0
        max_column = len(row)
        compressed_consecutive_elements = []

        while current_column < max_column:
            next_column = current_column+1
            while next_column < max_column and row[next_column] == row[current_column] and not isinstance(row[current_column], tuple):
                next_column += 1

            element_already_compressed = isinstance(row[current_column], tuple)
            if element_already_compressed:
                compressed_consecutive_elements.append(row[current_column])
            else:
                compressed_consecutive_elements.append(
                    (row[current_column], next_column-current_column))
            current_column = next_column

        # Now, sum the consecutive values who are equal
        current_column = 0
        max_column = len(compressed_consecutive_elements)
        combined_compressed_consecutive_elements = []
        while current_column < max_column:
            next_column = current_column + 1

            combined_sum = compressed_consecutive_elements[current_column][1]
            while next_column < max_column and compressed_consecutive_elements[next_column][0] == compressed_consecutive_elements[current_column][0]:
                combined_sum += compressed_consecutive_elements[next_column][1]
                next_column += 1

            combined_compressed_consecutive_elements.append(
                (compressed_consecutive_elements[current_column][0], combined_sum))
            current_column = next_column
        compressed_cols_universe.append(
            (combined_compressed_consecutive_elements, 1))
    return compressed_cols_universe


def expand_rows(compressed_cols_universe: List[str], expand_factor: int):
    """
    Expands empty rows in the compressed columns universe by the specified factor.

    Parameters:
    - compressed_cols_universe (List[str]): The compressed columns universe.
    - expand_factor (int): The factor by which to expand rows.

    Returns:
    List: Expanded and compressed columns universe.
    """

    for row_index, row in enumerate(compressed_cols_universe):
        if len(row[0]) == 1:
            compressed_cols_universe[row_index] = (row[0], expand_factor)
    return compressed_cols_universe


# It will compress each row of the universe in the form
# ([(v1, a1), (V2, a1), (vN, a1)], b)
# where:
# v = the value
# a = how many consecutive times the value repeats?
# b = how many rows does the pattern span?
def expand_and_compress_universe(universe: List[str], expand_factor: int) -> List[Tuple[List[Tuple[str, int]], int]]:
    """
    Expands and compresses the entire cosmic universe.

    Parameters:
    - universe (List[str]): The 2D list representing the cosmic universe.
    - expand_factor (int): The factor by which to expand columns and rows.

    Returns:
    List[Tuple[List[Tuple[str, int]], int]]: Expanded and compressed cosmic universe.
    """

    compressed_cols = expand_and_compress_columns(universe, expand_factor)
    compressed_universe = expand_rows(compressed_cols, expand_factor)
    return compressed_universe


def get_galaxy_positions(universe: List[Tuple[List[Tuple[str, int]], int]]) -> List[Tuple[int, int]]:
    """
    Retrieves the positions of galaxies in a compressed cosmic universe.

    Parameters:
    - universe (List[Tuple[List[Tuple[str, int]], int]]: The 2D list representing the compressed cosmic universe.

    Returns:
    List[Tuple[int, int]]: Positions of galaxies in the universe.
    """

    galaxy_positions = []
    for row_index, row in enumerate(universe):
        row_value = row[0]
        for element_index, element in enumerate(row_value):
            if element[0] != "#":
                continue

            galaxy_x = sum([k[1] for k in universe[0:row_index]])
            galaxy_y = sum([k[1] for k in row_value[0:element_index]])

            galaxy_positions.append((galaxy_x, galaxy_y))
    return galaxy_positions


def get_distance_between_galaxies(gal_x: Tuple[int, int], gal_y: Tuple[int, int]):
    """
    Calculates the distance between two galaxies.

    Parameters:
    - gal_x (Tuple[int, int]): Position of the first galaxy.
    - gal_y (Tuple[int, int]): Position of the second galaxy.

    Returns:
    int: Distance between the two galaxies.
    """

    return abs(gal_y[0] - gal_x[0]) + abs(gal_y[1] - gal_x[1])


def get_galaxy_shortest_path_sum(universe: List[str], expand_factor: int = 2):
    """
    Calculates the sum of shortest paths between all pairs of galaxies.

    Parameters:
    - universe (List[str]): The 2D list representing the cosmic universe.
    - expand_factor (int): The factor by which to expand columns and rows.

    Returns:
    int: The sum of shortest paths between all pairs of galaxies.
    """

    parsed_universe = [list(k) for k in universe]
    compressed_universe = expand_and_compress_universe(
        parsed_universe, expand_factor)
    galaxies_positions = get_galaxy_positions(compressed_universe)

    result = 0
    for gal_x, gal_y in combinations(galaxies_positions, 2):
        result += get_distance_between_galaxies(gal_x, gal_y)
    return result


if __name__ == "__main__":
    print("===== Cosmic Expansion (Day 11) - Advent of Code 2023  =====")

    try:
        from aocd import get_data
        input_items = get_data(day=11, year=2023).split("\n")
    except Exception as e:
        try:
            with open("./input.txt", encoding="utf-8") as input_file:
                input_items = input_file.readlines()
                input_items = [k.strip() for k in input_items]
        except FileNotFoundError:
            print("Could not fetch input data from AoC and input.txt is not present.")
            exit()

    print(
        f"The first star result is {get_galaxy_shortest_path_sum(input_items, 2)}")
    print(
        f"The second star result is {get_galaxy_shortest_path_sum(input_items, 1000000)}")
