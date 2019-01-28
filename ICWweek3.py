# Problem 1:
#
# Given a number n, return True if n is in the range 1..10, inclusive.
# Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
# Print the result returned from your function.
#
# BONUS: Get the number and outside_mode flag from User input instead of hardcoding it
#
# def in1to10(n, outside_mode):
#
# Examples of Expected Output:
#
# in1to10(5, False) → True
#
# in1to10(11, False) → False
#
# in1to10(11, True) → True


# def in1to10(n, outside_mode):

def main():
    problem()

def problem(n, outside_mode):

    if(n>1 and n<10):
        return not outside_mode
    else:
        return outside_mode or n is 10 or n is 1

if __name__ == '__main__':
    main()