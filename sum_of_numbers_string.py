# Description:

# We want to generate a function that computes the series starting from 0 and ending until the given number.
# Example:

# Input:

# > 6

# Output:

#     0+1+2+3+4+5+6 = 21

# Input:

# > -15

# Output:

#     -15<0

# Input:

# > 0

# Output:

#     0=0


def show_sequence(n):
    if n == 0:
        return '0=0'
    if n < 0:
        return str(n) + '<0'
    else:
        value = 0
        nums = ''
        for x in range (0, n+1):
            value += x
            print(value)
            nums += str(x) + '+'
            print(nums)
            
        nums = nums[:-1]
        nums += ' = ' + str(value)
        print(nums)
        return(nums)
            