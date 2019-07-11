"""
Given a set of numbers, return the additive inverse of each.
Each positive becomes negatives, and the negatives become positives.

invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
invert([]) == []
You can assume that all values are integers. Do not mutate the input array/list.
"""

def invert(lst):
    output = []
    for num in lst:
        if num < 0:
            output.append(int(str(num)[1:]))
        else:
            output.append(int("-" + str(num)))
    return output


# the simplest solution. I'm taken aback by its simplicity.
def invert(lst):
    return [-x for x in lst]
