# Wait For It (Day 06) - Advent of Code 2023 

## The First Star
A Given document gives two informations about a unspecified amount of races: the time (in ms) and the distance of the current record. The racer starts with the speed at 0 and for each millisecond they pressed the button, the speed increases by 1. While pressing, the vehicle doesn't move and speed doesn't decrease overtime.
Determine the number of ways you could beat the record in each race.

Example:
```
Time:      7  15   30
Distance:  9  40  200

The first race lasts 7 milliseconds. The record distance in this race is 9 millimeters. You win by holding the button between 2-5ms (4 ways).
The second race lasts 15 milliseconds. The record distance in this race is 40 millimeters. You win by holding the button between 4-11ms (8 ways).
The third race lasts 30 milliseconds. The record distance in this race is 200 millimeters. You win by holding the button between 11-19ms (9 ways).

The result is 4 * 8 * 9 = 288
```

## The Second Star
Now, consider everything as a single race by joining the time and distance numbers in one continuous number and return the amount of ways of winning.

Example:
```
Time:      7  15   30
Distance:  9  40  200

New Time = 71530
New Distance = 940200

You could hold the button anywhere from 14 to 71516 milliseconds and beat the record, a total of 71503 ways!
```

## Running the code
To run the code, just use the following command in this directory in a environment with Python3 installed and it will give you the result:
```
    python3 main.py
```

## About
Advent of Code is an annual programming event created by the [Advent of Code](https://adventofcode.com) enterprise where you've to collect 50 stars by completing daily programmings challenges. You can learn more about this challenge [here](https://adventofcode.com/2023/day/6).
