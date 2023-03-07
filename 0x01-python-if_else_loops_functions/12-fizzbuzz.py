#!/usr/bin/python3

"""Prints numbers from 1 - 100 separated by space.
    For multiples of 3, print fizz.
    For multiples of both 3 and 5, print FizzBuzz
    For multiples of 5, print Buzzz.
"""
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz ", end="")
        elif number % 3 == 0:
            print("Fizz ", end="")
        elif number % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(number), end="")
