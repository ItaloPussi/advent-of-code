# Cube Conundrum (Day 02) - Advent of Code 2023 

## The First Star
Process a document consisting of lines of text. Each line contains a textual representation of a game, and the goal is to determine if each game is valid. A game is valid if during the rounds, the number of balls of a given color doesn't exceed the maximum allowed value for that color. The ultimate objective is to calculate the sum of all the IDs of the valid games.

- The ID of the game is the number before the colon(:)
- The rounds starts after the colon and are divided by a semicolon(;)

Example:
```
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
ID: 1
Round 1: 3 blue, 4 red; 1 red
Round 2: 1 red, 2 green, 6 blue
Round 3: 2 green

If the maximum amount of RGB balls are 6, 6, 5 the game would not be valid because in round 2 we have 6 blue balls (and the maximum is 5).
If the maximum amount of RGB balls are 6, 6, 6 the game would be valid because none of the balls exceed the maximum  allowed amount
```

## The Second Star
Improve the created code to instead of validating a game, calculate the multiplication of the minimum amounts of RGB balls necessary to game be valid.
Return the sum of the value of all the games.

Example:
```
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green


The minimum amount of RGB are 4, 6, 2 and the result would be 4 * 6 * 2 = 48.

```

## Running the code
To run the code, just use the following command in this directory in a environment with Python3 installed and it will give you the result:
```
    pip install -r requirements.txt
    python3 main.py
```
Remember to configure your (AoC Session)[https://pypi.org/project/advent-of-code-data/#description]

## About
Advent of Code is an annual programming event created by the [Advent of Code](https://adventofcode.com) enterprise where you've to collect 50 stars by completing daily programmings challenges. You can learn more about this challenge [here](https://adventofcode.com/2023/day/2).
