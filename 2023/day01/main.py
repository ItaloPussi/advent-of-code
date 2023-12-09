"Advent of Cyber 2023 - Day 01 - Exercises 01 and 02"

from typing import Union, List

# Maps the digit in the text form to its numerical representation
mapped_text_representation_to_digit = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}


def get_calibration_value(text: str, allow_written_digits=False) -> Union[int, None]:
    """
        Given a input, get a two digits value from it formed by the first and last digit present.

        Parameters:
        - text (str): The text representation of a number.
        - allow_written_digits (bool): Tells if the function should consider written digits (three, one...)

        Returns:
        - Union[int, None]: The two digits representation, or None if no valids numbers are found.
    """

    text = str(text)

    output_str = ""
    last_digit = ""

    for index, character in enumerate(text):
        if character.isdigit():
            last_digit = character
            if output_str == "":
                output_str += character
        elif (allow_written_digits):
            for text_digit, digit in mapped_text_representation_to_digit.items():
                if text.find(text_digit, index) == index:
                    last_digit = digit

            if output_str == "":
                output_str += last_digit
    output_str += last_digit

    return int(output_str) if output_str != "" else None


def get_calibration_items_sum(items: List[str], allow_written_digits=False) -> int:
    """
    Calculates the sum of the numerical representations obtained from a list of text items.

    Parameters:
    - items (List[str]): List of text items for the calibration function.
    - allow_written_digits (bool): Tells if the function should consider written digits (three, one...)


    Returns:
    - int: The sum of numerical representations obtained from the calibration process.
    """
    output_sum = 0
    for item in items:
        calibration_value = get_calibration_value(item, allow_written_digits)
        if calibration_value is not None:
            output_sum += calibration_value
    return output_sum


if __name__ == "__main__":
    print("===== Trebuchet (Day 01) - Advent of Code 2023  =====")

    try:
        from aocd import get_data
        input_items = get_data(day=1, year=2023).split("\n")
    except Exception as e:
        try:
            with open("./input.txt", encoding="utf-8") as input_file:
                input_items = input_file.readlines()
        except FileNotFoundError:
            print("Could not fetch input data from AoC and input.txt is not present.")
            exit()

    print(
        f"The first star result is {get_calibration_items_sum(input_items)}")
    print(
        f"The second star result is {get_calibration_items_sum(input_items, True)}")
