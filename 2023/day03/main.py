"Advent of Cyber 2023 - Day 03 - Exercises 01 and 02"
from typing import List, Tuple
import re


def does_text_contains_symbols(text: str) -> bool:
    """
    Checks if the given text contains symbols (except dots).

    Parameters:
    - text (str): The input text to check.

    Returns:
    - bool: True if symbols are present, False otherwise.
    """

    text_without_digits_and_dots = ''.join(
        [i for i in text if not i.isdigit() and not i == "."])
    if len(text_without_digits_and_dots) > 0:
        return True
    return False


def get_valid_adjacent_lines(current_index: str, schematic: str) -> List[int]:
    """
    Get the valid adjacent lines for a given index in the schematic.

    Parameters:
    - current_index (int): The current index.
    - schematic (List[str]): The list of schematic lines.

    Returns:
    - List[int]: A list of valid adjacent lines indices.
    """

    valid_adjacent_lines = [
        current_index - 1 if current_index > 0 else 0,
        current_index,
        current_index + 1 if current_index < len(schematic) - 1 else None
    ]

    return [x for x in valid_adjacent_lines if x is not None]


def get_adjacent_bounds(x: int, y: int) -> Tuple[int, int]:
    """
    Get the adjacent bounds for a given range.

    Parameters:
    - x (int): The starting index.
    - y (int): The ending index.

    Returns:
    - Tuple[int, int]: The start and end indices for adjacency.
    """

    start_index = 0 if x == 0 else x - 1
    end_index = y + 1
    return start_index, end_index


def get_schematic_line_numbers_with_symbols_adjacency_sum(current_index: str, schematic: List[str]) -> int:
    """
    Get the sum of numbers adjacent to symbols in a schematic line.

    Parameters:
    - current_index (int): The current index.
    - schematic (List[str]): The list of schematic lines.

    Returns:
    - int: The sum of numbers adjacent to symbols in the line.
    """

    current_schematic_line = schematic[current_index]

    # Gets all the group of numbers present in the line
    schematic_line_numbers = re.finditer(r"(\d+)", current_schematic_line)

    numbers_with_symbols_adjacency = []

    for schematic_line_number in schematic_line_numbers:

        # For the adjacency validations, we must add one more cell to left and right of bounds
        adjacency_start_index, adjacency_end_index = get_adjacent_bounds(
            *schematic_line_number.span())

        valid_adjacent_lines = get_valid_adjacent_lines(
            current_index, schematic)

        for adjacent_line in valid_adjacent_lines:
            # For each line, validate if it contains a symbol within the bounds.
            # If True, add it to the result list and break
            if does_text_contains_symbols(schematic[adjacent_line][adjacency_start_index:adjacency_end_index]):
                numbers_with_symbols_adjacency.append(
                    int(schematic_line_number.group(0)))
                break
    return sum(numbers_with_symbols_adjacency)


def get_adjacency_numbers_sum(schematic: str) -> int:
    """
    Get the sum of all part numbers in the engine schematic.

    Parameters:
    - schematic (List[str]): The list of schematic lines.

    Returns:
    - int: The sum of all part numbers in the engine schematic.
    """

    output_sum = 0
    for index, _ in enumerate(schematic):
        schematic_line_valid_numbers_sum = get_schematic_line_numbers_with_symbols_adjacency_sum(
            index, schematic)
        output_sum += schematic_line_valid_numbers_sum
    return output_sum


def get_gear_numbers(current_index, schematic: str):
    """
    Get the gear ratios for a given index in the schematic.

    Parameters:
    - current_index (int): The current index.
    - schematic (List[str]): The list of schematic lines.

    Returns:
    - int: The sum of gear ratios for the line.
    """

    schematic_line = schematic[current_index]
    schematic_line_gears = re.finditer(r"(\*)", schematic_line)
    result = []

    for schematic_line_gear in schematic_line_gears:
        numbers = []

        bound_x, bound_y = get_adjacent_bounds(*schematic_line_gear.span())
        gear_bounds_range = set(range(bound_x, bound_y))

        valid_adjacent_lines = get_valid_adjacent_lines(
            current_index, schematic)

        for adjacent_line in valid_adjacent_lines:
            line_numbers = re.finditer(
                r"(\d+)", schematic[adjacent_line])
            for number in line_numbers:
                x, y = number.span()
                number_range = set(range(x, y))
                if len(gear_bounds_range.intersection(number_range)) > 0:
                    numbers.append(int(number.group(0)))

        # Business Logic: Only consider if it has exactly 2 adjancent numbers
        if len(numbers) == 2:
            result.append(numbers[0] * numbers[1])
    return sum(result)


def get_gear_numbers_sum(schematic: str) -> int:
    """
    Get the sum of all gear ratios in the engine schematic.

    Parameters:
    - schematic (List[str]): The list of schematic lines.

    Returns:
    - int: The sum of all gear ratios in the engine schematic.
    """
    output_sum = 0
    for index, _ in enumerate(schematic):
        schematic_line_valid_numbers_sum = get_gear_numbers(
            index, schematic)
        output_sum += schematic_line_valid_numbers_sum
    return output_sum


if __name__ == "__main__":
    with open("./input.txt", encoding="utf-8") as input_file:
        input_items = [k.strip() for k in input_file.readlines()]
        print("===== Gear Ratios (Day 03) - Advent of Code 2023  =====")
        print(
            f"The first star result is {get_adjacency_numbers_sum(input_items)}")
        print(
            f"The second star result is {get_gear_numbers_sum(input_items)}")
