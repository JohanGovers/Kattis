#! /usr/bin/python3

import sys

def print_fizz_buzz(x, y, n):
    for i in range(1,n+1):
        if(i % x == 0):
            print("Fizz", end="")
        if(i % y == 0):
            print("Buzz", end="")
        if(not i % x == 0 and not i % y == 0):
            print(i, end="")
        print("")

for line in sys.stdin:
    nums = line.split()
    x = int(nums[0])
    y = int(nums[1])
    n = int(nums[2])

    print_fizz_buzz(x,y,n)
