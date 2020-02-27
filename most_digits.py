Description:

Find the number with the most digits.

If two numbers in the argument array have the same number of digits, return the first one in the array.

def find_longest(arr):
    #your code here
    max_lenght = 0
    max_index = 0
    for cur_num in arr:
        lenght = len(str(cur_num))
        if lenght > max_lenght:
            max_lenght = lenght
            max_index = arr.index(cur_num)
    return arr[max_index]
