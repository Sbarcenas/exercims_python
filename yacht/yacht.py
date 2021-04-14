"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.
YACHT = 'yacht'
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 'full_house'
FOUR_OF_A_KIND = 'four_of_a_kind'
LITTLE_STRAIGHT = 'little_straight'
BIG_STRAIGHT = 'big_straight'
CHOICE = 'choice'


def detect_four_of_kind(dice):
    if dice.count(dice[0]) >= 4:
        return dice[0]
    if dice.count(dice[1]) >= 4:
        return dice[1]
    return None


def is_ascending(dice):
    sortd = sorted(dice)
    diffs = list(map(lambda x: x[1] - x[0], zip(sortd[0:4], sortd[1:])))
    return diffs == [1, 1, 1, 1]


def score(dice, category):
    if category in range(1, 6 + 1):
        return category * dice.count(category)
    if category is FULL_HOUSE:
        sorted_dice = sorted(dice)
        n_min = dice.count(sorted_dice[0])
        n_max = dice.count(sorted_dice[-1])
        if (n_min, n_max) == (2, 3) or (n_min, n_max) == (3, 2):
            return sum(dice)
    if category is YACHT:
        if dice.count(dice[0]) == 5:
            return 50
    if category is FOUR_OF_A_KIND:
        detected = detect_four_of_kind(dice)
        if detected is not None:
            return detected * 4
    if category is LITTLE_STRAIGHT:
        if is_ascending(dice) and min(dice) == 1:
            return 30
    if category is BIG_STRAIGHT:
        if is_ascending(dice) and min(dice) == 2:
            return 30
    if category is CHOICE:
        return sum(dice)
    return 0