# Write a function that takes an array of numbers (integers for the tests) and a target number.
# It should find two different items in the array that, when added together, give the target value.
# The indices of these items should then be returned in a tuple like so: (index1, index2).
# For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.
# The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers;
# target will always be the sum of two different items from that array).

# Based on: http://oj.leetcode.com/problems/two-sum/

def two_sum(numbers, target):

    counter_1 = 1
    counter_2 = 0

    while numbers[counter_1] + numbers[counter_2] != target:
        if counter_1 < len(numbers) - 1:
            counter_1 += 1
        else:
            counter_1 = 0
            if counter_2 < len(numbers) - 1:
                counter_2 += 1

    new_list = [counter_1, counter_2]

    return new_list
