from random import randint
from itertools import repeat

"""
Implementing parts of 
https://www.geeknative.com/61483/12-different-ways-roll-dnd-character/
"""

def best_rolls(num_rolls, top=3, discard_ones=False, base=6, advantage=True):
    """
    Returns sum of top number of specified roles for a given base
    """
    rolls = list()
    
    for _ in repeat(None, num_rolls):
        if discard_ones:
            rolls.append(randint(2, base))
        else:
            rolls.append(randint(1, base))

    rolls.sort(reverse=advantage)

    return sum(rolls[:top])


def three_d6(count=6):
    """
    Roll 3d6 and assign the totals to your attributes in any order you want
    """
    stats = list()

    for _ in repeat(None, count):
        roll = best_rolls(num_rolls=3, top=3, discard_ones=False)
        stats.append(roll)

    stats.sort(reverse=True)

    return stats


def four_d6_drop_worst(count=6):
    """
    Roll 4d6, drop the lowest in each roll
    """
    stats = list()

    for _ in repeat(None, count):
        roll = best_rolls(num_rolls=4, top=3, discard_ones=False)
        stats.append(roll)

    stats.sort(reverse=True)

    return stats


def five_d6_drop_worst(count=6):
    """
    Roll 3d6 and assign the totals to your attributes in any order you want
    """
    stats = list()

    for _ in repeat(None, count):
        roll = best_rolls(num_rolls=5, top=3, discard_ones=False)
        stats.append(roll)

    stats.sort(reverse=True)

    return stats


def four_d6_drop_worst_best_of_n(tries= 8, top=6):
    """
    Roll 4d6, drop the lowest die in each roll and do it 8 times. 
    Assign the best 6 totals to your attributes
    """
    stats = list()

    for _ in repeat(None, tries):
        roll = best_rolls(num_rolls=4, top=3, discard_ones=False)
        stats.append(roll)

    stats.sort(reverse=True)

    return stats[:top]


def four_d6_reroll_below_n(count=6, min_stat=8):
    """
    Roll 4d6, drop the lowest die and 
    re-roll any total that is below 8. 
    """
    stats = list()

    for _ in repeat(None, count):
        roll = min_stat - 1
        while (roll < min_stat):
            roll = best_rolls(num_rolls=4, top=3, discard_ones=False)
        stats.append(roll)

    stats.sort(reverse=True)

    return stats


def four_d6_replace_below_n(count=6, min_stat=8):
    """
    Roll 4d6, drop the lowest die and 
    re-roll any total that is below 8. 
    """
    stats = list()

    for _ in repeat(None, count):
        roll = best_rolls(num_rolls=4, top=3, discard_ones=False)
        stats.append(max(roll, min_stat))

    stats.sort(reverse=True)

    return stats


def reroll_if_no_stat_above_x(x=15):
    """
    Roll 4d6, drop the lowest die 
    but reroll the entire collection if no total is above 15.
    """
    max_stat = 0

    while (max_stat < x):
        stats = four_d6_drop_worst()
        max_stat = max(stats)

    return stats


def reroll_if_total_below_x(x=70):
    """
    Roll 4d6, drop the lowest die and reroll the lowest total 
    until the cumulative total value is over 70 (or 75, etc)
    """
    total = 0

    while (total < x):
        stats = four_d6_drop_worst()
        total = sum(stats)
    
    return stats


def four_d6_drop_worst_reroll_1s(count=6):
    """
    Roll 4d6, reroll 1s and drop the lowest die
    """
    stats = list()

    for _ in repeat(None, count):
        roll = best_rolls(num_rolls=4, top=3, discard_ones=True)
        stats.append(roll)

    stats.sort(reverse=True)

    return stats


def four_d6_drop_worst_only_one_above_x(x=16, count=6):
    """
    Roll 4d6s, drop the lowest and assign as required 
    however only one stat can be 16 or higher.
    Note: This could iterate many times, but should be fast enough for humans
    """
    stats = list()
    count_above_max = 0

    while(count_above_max != 1):
        stats = four_d6_drop_worst()
        count_above_max = sum(i > x for i in stats)

    return stats


def roll_2d6_plus6(count=6):
    """
    Roll 2d6+6 and assign as required
    """
    stats = list()

    for _ in repeat(None, count):
        stat = best_rolls(num_rolls=2, top=2, discard_ones=False, base=6) + 6
        stats.append(stat)
    
    stats.sort(reverse=True)

    return stats


## Try and print all techniques

print "3d6: \t\t\t\t", three_d6()
print "4d6: \t\t\t\t", four_d6_drop_worst()
print "5d6: \t\t\t\t", five_d6_drop_worst()
print "2d6+6\t\t\t\t", roll_2d6_plus6()
print "4d6 (6 of 8):\t\t\t", four_d6_drop_worst_best_of_n()
print "4d6, reroll below 8:\t\t", four_d6_reroll_below_n()
print "4d6, never below 8:\t\t", four_d6_replace_below_n()
print "4d6, reroll if none > 15:\t", reroll_if_no_stat_above_x()
print "4d6, reroll if total < 70:\t", reroll_if_total_below_x()
print "4d6, reroll 1s:\t\t\t", four_d6_drop_worst_reroll_1s()
print "4d6, only one can be > 16:\t", four_d6_drop_worst_only_one_above_x()


