"Advent of Cyber 2023 - Day 09 - Exercises 01 and 02"
from typing import Literal, List


def extrapolate_pyramid(sequence: str) -> List[List[int]]:
    """
    Extrapolates a pyramid of integers from the given sequence.

    Parameters:
    - sequence (str): A space-separated string of integers.

    Returns:
    List[List[int]]: A list of lists representing the extrapolated pyramid.
    """

    int_sequence = [int(k) for k in sequence.split()]

    pyramid = [int_sequence]
    current_sequence = int_sequence

    while not set(current_sequence) == {0}:
        current_sequence = [current_sequence[k] - current_sequence[k-1]
                            for k in range(1, len(current_sequence))]

        pyramid.append(current_sequence)

    return pyramid


def extrapolate_right_next_number(sequence: str) -> int:
    """
    Extrapolates the next number of the sequence on the right side.

    Parameters:
    - sequence (str): A space-separated string of integers.

    Returns:
    int: The next number of the sequence.
    """

    pyramid = extrapolate_pyramid(sequence)

    for index, sequence in enumerate(reversed(pyramid)):
        if (index == 0):
            pyramid[len(pyramid) - index - 1].append(0)
            continue

        next_number = sequence[-1] + pyramid[len(pyramid) - index][-1]
        pyramid[len(pyramid) - index - 1].append(next_number)
    return next_number


def extrapolate_left_next_number(sequence: str) -> int:
    """
    Extrapolates the next number of the sequence on the left side.

    Parameters:
    - sequence (str): A space-separated string of integers.

    Returns:
    int: The next number of the sequence.
    """

    pyramid = extrapolate_pyramid(sequence)

    for index, sequence in enumerate(reversed(pyramid)):
        if (index == 0):
            pyramid[len(pyramid) - index - 1].insert(0, 0)
            continue

        next_number = sequence[0] - pyramid[len(pyramid) - index][0]
        pyramid[len(pyramid) - index - 1].insert(0, next_number)
    return next_number


def extrapolate_next_number_sum(sequences: list[str], side: Literal["left", "right"] = "right") -> int:
    """
    Calculates the sum of extrapolated next numbers based on the specified side.

    Parameters:
    - sequences (List[str]): A list of space-separated strings of integers.
    - side (Literal["left", "right"], optional): The side to extrapolate the next numbers. Defaults to "right".

    Returns:
    int: The sum of extrapolated next numbers.
    """

    output_sum = 0

    for sequence in sequences:
        output_sum += extrapolate_right_next_number(
            sequence) if side == "right" else extrapolate_left_next_number(sequence)
    return output_sum


if __name__ == "__main__":
    with open("./input.txt", encoding="utf-8") as input_file:
        input_items = [k.strip() for k in input_file.readlines()]
        print("===== Mirage Maintenance (Day 09) - Advent of Code 2023  =====")
        print(
            f"The first star result is {extrapolate_next_number_sum(input_items)}")
        print(
            f"The second star result is {extrapolate_next_number_sum(input_items, 'left')}")
