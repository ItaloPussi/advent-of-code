"Advent of Cyber 2023 - Day 02 - Exercises 01 and 02"
from typing import List, Literal
import re


def extract_colors_counts(game: str, ball_color: Literal['red', "green", "blue"]) -> List[int]:
    """
        Given a game and a color, extract the amount of balls of the color

        Parameters:
        - game (str): The text representation of the game.
        - ball_color (Literal['red', "green", "blue"]): The ball color.

        Returns:
        - List[int]: A list containing the amount of balls of that color
    """
    return [int(k) for k in re.findall(rf"(\d+) {ball_color}", game)]


def is_game_possible(game: str, max_rgb_balls: List[int]) -> bool:
    """
        Validate if a game is valid given the max amount of RGB balls.

        Parameters:
        - game (str): The text representation of the game.
        - max_rgb_balls (List[int]): The max allowed number of red, green and blue balls.

        Returns:
        - bool: True if the game is possible, False otherwise.
    """

    max_red_balls, max_green_balls, max_blue_balls = max_rgb_balls

    red_balls = extract_colors_counts(game, "red")
    is_red_valid = max_red_balls >= max(red_balls)

    green_balls = extract_colors_counts(game, "green")
    is_green_valid = max_green_balls >= max(green_balls)

    blue_balls = extract_colors_counts(game, "blue")
    is_blue_valid = max_blue_balls >= max(blue_balls)

    return is_red_valid and is_blue_valid and is_green_valid


def get_possible_games_sum(games: List[str]) -> int:
    """
    Given a list of games, calculates the sum of the IDs of all the valid ones.

    Parameters:
    - games (List[str): A list of games.

    Returns:
    - int: The sum of the IDs of all the valid games.
    """
    output_sum = 0
    for game in games:
        game_possible = is_game_possible(game, [12, 13, 14])
        if game_possible:
            game_id = re.search(r"Game (\d+)", game).group(1)
            output_sum += int(game_id)
    return output_sum


def get_game_balls_min_amount(game: str) -> int:
    """
        Given a game, the multiplication of the minimum amount of balls for the game be valid.

        Parameters:
        - game (str): The text representation of the game.

        Returns:
        - int: The multiplication of the RGB amount
    """

    red_amount = max(extract_colors_counts(game, "red"))
    green_amount = max(extract_colors_counts(game, "green"))
    blue_amount = max(extract_colors_counts(game, "blue"))

    return red_amount * green_amount * blue_amount


def get_game_balls_min_amount_sum(games: str) -> int:
    """
        Given a list of games, the sum of the result of the function 
        get_game_balls_min_amount for each game.

        Parameters:
        - games (List[str): A list of games.

        Returns:
        - int: The sum of the result of the function get_game_balls_min_amount for each game.
    """

    output_sum = 0
    for game in games:
        game_power = get_game_balls_min_amount(game)
        output_sum += game_power
    return output_sum


if __name__ == "__main__":
    print("===== Cube Conundrum (Day 02) - Advent of Code 2023  =====")

    try:
        from aocd import get_data
        input_items = get_data(day=2, year=2023).split("\n")
    except Exception as e:
        try:
            with open("./input.txt", encoding="utf-8") as input_file:
                input_items = input_file.readlines()
        except FileNotFoundError:
            print("Could not fetch input data from AoC and input.txt is not present.")
            exit()

    print(
        f"The first star result is {get_possible_games_sum(input_items)}")
    print(
        f"The second star result is {get_game_balls_min_amount_sum(input_items)}")
