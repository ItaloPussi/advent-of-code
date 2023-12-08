# Haunted Wasteland (Day 08) - Advent of Code 2023 

## The First Star
A Given document contains a list of left/right instructions, and a network of labeled nodes.
Starting from node AAA, get the total steps required to get to ZZZ.
If there are no more directions, cycle by the directions again.

Example:
```
RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)

Starting in AAA, we should go right to CCC. From there, left to ZZZ. 2 steps in total.
```

## The Second Star
Now, consider as entrypoints all the nodes who ends with "A". The goal is to get the total steps required to all the entrypoints make to the goal. If a entrypoint is in the goal, but the others are not, it should continue the cycle until all them match.

Example:
```
LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)

Entrypoints = 11A and 22A
Goal = 11Z and 22Z
Total steps = 6
```

## Running the code
To run the code, just use the following command in this directory in a environment with Python3 installed and it will give you the result:
```
    python3 main.py
```

## About
Advent of Code is an annual programming event created by the [Advent of Code](https://adventofcode.com) enterprise where you've to collect 50 stars by completing daily programmings challenges. You can learn more about this challenge [here](https://adventofcode.com/2023/day/8).
