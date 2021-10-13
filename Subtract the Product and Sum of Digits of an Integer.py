"""
Given an integer number n, return the difference between the product of its digits and the sum of its digits.
"""
import math
x = list(map(int, input()))
print(math.prod(x) - sum(x))
