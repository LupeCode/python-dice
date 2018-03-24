import random
import math


def roll_one(sides):
    return random.randint(1, sides)


def roll_dice(number, sides):
    rolls = []
    for _ in range(number):
        rolls.append(roll_one(sides))
    return rolls


def roll_low(number, sides, factor=2.0):
    rolls = roll_high(number, sides, factor)
    mod_rolls = []
    for roll in rolls:
        mod_rolls.append(sides + 1 - roll)
    return mod_rolls


def roll_high(number, sides, factor=2.0):
    sides = int(math.floor(math.pow(sides, factor)))
    rolls = []
    for _ in range(number):
        rolls.append(int(math.ceil(pow(roll_one(sides), 1 / factor))))
    return rolls
