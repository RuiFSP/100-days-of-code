# Instructions
# time.time() will return the current time in seconds since January 1, 1970, 00:00:00
#
# Try running the starting code to see the current time printed.
#
# If you run the code after a while, you'll see a new time printed.
#
# e.g. first run:
#
# 1598524371.736911
# second run:
#
# 1598524436.357875
# The time difference = second run - first run
#
# 64.62096405029297
# (approx 1 minute)
#
# Given the above information, complete the code exercise by printing out the speed it takes to run the
# fast_function() vs the slow_function(). You will need to complete the speed_calc_decorator() function.
#
# Expected Output
#
#
# Hint
# You can use function.__name__ to get the name of the function,
#
# NOTE: There are no tests for this exercise as the speed can vary depending on many factors.
import math
import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def speed_calculation_function():
        start_time = time.time()
        function()
        end_time = time.time()
        print(f"{function.__name__} run speed: {end_time - start_time}")

    return speed_calculation_function()


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        math.pow(i, 2)


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        math.pow(i, 2)
