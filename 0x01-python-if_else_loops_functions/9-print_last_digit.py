#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    lastNumber = number % 10
    print(lastNumber, end="")
    return lastNumber
