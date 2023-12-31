# Cosmic Expansion (Day 11) - Advent of Code 2023 

## The First Star
Given a universe represented by a matrix containing dots (space) and number signs (galaxies), expand the columns and rows without galaxies by 2 and calculate the sum of smallest distance between every pair of galaxies.

Example:
```
...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....

Expanded Version (by 2):
....a........
.........b...
#............
.............
.............
........#....
.#...........
............#
.............
.............
.........#...
#....#.......

Distance between a and b: 6
Repeat for each pair and the sum is 374
```

## The Second Star
Now the expand factor is 1 million. The rest is the same.

## Running the code
To run the code, just use the following command in this directory in a environment with Python3 installed and it will give you the result:
```
    pip install -r requirements.txt
    python3 main.py
```
Remember to configure your (AoC Session)[https://pypi.org/project/advent-of-code-data/#description]

## About
Advent of Code is an annual programming event created by the [Advent of Code](https://adventofcode.com) enterprise where you've to collect 50 stars by completing daily programmings challenges. You can learn more about this challenge [here](https://adventofcode.com/2023/day/11).
