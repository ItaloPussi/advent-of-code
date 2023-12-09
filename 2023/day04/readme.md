# Scratchcards (Day 04) - Advent of Code 2023 

## The First Star
Given a collection of scratchcards, each containing two lists of numbers separated by a vertical bar (|), the goal is to calculate the total points. Points are awarded based on the number of matching numbers between the winning numbers and the player's numbers. The first and second matches are worth one point, and each subsequent match doubles the point value of the card.

Example:
```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11

In this example, Card 1 has four winning numbers (48, 83, 17, and 86), cards 2 and 3 has 2, card 4 has 1 and cards 5-6 has 0. Resulting in 4 scratchcards with the total of 8 points

```

## The Second Star
Change the calculation to be card based: A scratchcard with 5 matched numbers will increase the multiplier of the next 5 cards by 1, the next one will increase the multiplier of the next N cards by its own multiplier (2). The end result is to sum all multipliers, getting the amount of scratchcards.

Example:
```
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11


In this example, the process results in a total of 30 scratchcards with the multipliers being 1, 2, 4, 8, 14, 1.

```

## Running the code
To run the code, just use the following command in this directory in a environment with Python3 installed and it will give you the result:
```
    pip install -r requirements.txt
    python3 main.py
```
Remember to configure your (AoC Session)[https://pypi.org/project/advent-of-code-data/#description]

## About
Advent of Code is an annual programming event created by the [Advent of Code](https://adventofcode.com) enterprise where you've to collect 50 stars by completing daily programmings challenges. You can learn more about this challenge [here](https://adventofcode.com/2023/day/4).
