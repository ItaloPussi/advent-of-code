# Gear Ratios (Day 03) - Advent of Code 2023 

## The First Star
Process a schematic consisting of lines of text. Each line contains some numbers and symbols. The goal is to sum all the numbers adjacent to a symbol, even diagonally. Is important to denote that dots (.) are not considered a symbol in this case.

Example:
```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.. 

In this schematic, two numbers don't count because they are not adjacent to a symbol: 114 (top right) and 58 (middle right). Every other number is adjacent to a symbol; their sum is 4361.
```

## The Second Star
Improve the created code to sum all the available gear ratios. A gear is any * symbol that is adjacent to exactly two numbers and its gear ratio is the result of multiplying those two numbers together.

Example:
```
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598.. 


In this schematic, there are two gears. The first is in the top left; it has numbers 467 and 35, so its gear ratio is 16345. The second gear is in the lower right; its gear ratio is 451490. Adding up all of the gear ratios produces 467835.
```

## Running the code
To run the code, just use the following command in this directory in a environment with Python3 installed and it will give you the result:
```
    python3 main.py
```

## About
Advent of Code is an annual programming event created by the [Advent of Code](https://adventofcode.com) enterprise where you've to collect 50 stars by completing daily programmings challenges. You can learn more about this challenge [here](https://adventofcode.com/2023/day/3).
