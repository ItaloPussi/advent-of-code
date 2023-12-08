# Camel Cards (Day 06) - Advent of Code 2023 

## The First Star
A Given document gives a series of plays: Each line have a camel (poker) hand and a bid. The goal is to give each play a rank based on the hand type, starting from 1 and increasing by 1 until all the hands has a rank. Repeated hand types should give a rank according with the comparison of strength of the hands. Multiply each play rank by the bid and return the sum of all the results.

Example:
```
32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483

32T3K = One Pair - Rank 1
T55J5 = Three of a Kind - Rank 4 
KK677 = Two Pair - Rank 3 (Stronger than KTJJT)
KTJJT = Two Pair - Rank 2
QQQJA - Three of a Kind - Rank 5 (Stronger than T55J5)

The result is 765 * 1 + 684 * 4 + 28 * 3 + 220 * 2 + 483 * 5 = 6440
```

## The Second Star
Now, jokers are considered wildcards and can contribute to a hand type. The rest is basically the same.

Example:
```
T55J5 = Become four of a kind
KTJJT = Become four a kind
QQQJA = Become four a kind
```

## Running the code
To run the code, just use the following command in this directory in a environment with Python3 installed and it will give you the result:
```
    python3 main.py
```

## About
Advent of Code is an annual programming event created by the [Advent of Code](https://adventofcode.com) enterprise where you've to collect 50 stars by completing daily programmings challenges. You can learn more about this challenge [here](https://adventofcode.com/2023/day/7).
