# Complete the method which returns the number which is most frequent in the given input array. If there is a tie for most frequent number, return the largest number among them.

# Note: no empty arrays will be given.
# Examples

# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3



def highest_rank(arr):
    best = 0
    occs = 0
    for item in arr:
        times = arr.count(item)
        if times > occs:
            best = item
            occs = times
        elif times == occs:
            if best < item:
                best = item
    return best