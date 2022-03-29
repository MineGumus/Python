# Task : Find out the most frequent number and its frequency.

# Write a program that;
#  Finds out the most frequent number in the given list.
#  Calculates its frequency.
#  Prints out the result.


numbers = [1, 3, 7, 4, 3, 0, 3, 6, 3]
mostCommon = max(numbers, key = numbers.count)
counts_time = numbers.count(mostCommon)
print("the most frequent number is {} and it was {} times repeated".format(mostCommon, counts_time))
