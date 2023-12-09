# Trebuchet (Day 01) - Advent of Code 2023 

## The First Star
Process a document consisting of lines of text. Each line contains a sequence of characters, and the goal is to determine a calibration value for each line. The calibration value is derived by combining the first and last digits of each line to form a two-digit number. The ultimate objective is to calculate the sum of all these calibration values across the entire document. 

Example:
```
1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet

The calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142, which should be the output.
```


## The Second Star
Improve the created code to also consider written digits like three, seven, nine, etc.

Example:
```
two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen

The calibration values are 29, 83, 13, 24, 42, 14, and 76. Adding these together produces 281.
```

## Running the code
To run the code, just use the following command in this directory in a environment with Python3 installed and it will give you the result:
```
    pip install -r requirements.txt
    python3 main.py
```
Remember to configure your (AoC Session)[https://pypi.org/project/advent-of-code-data/#description]

For this challenge, I've used the TDD methodology. Tests can be run with:
```
    python3 tests.py
```

## About
Advent of Code is an annual programming event created by the [Advent of Code](https://adventofcode.com) enterprise where you've to collect 50 stars by completing daily programmings challenges. You can learn more about this challenge [here](https://adventofcode.com/2023/day/1)
