"""
Given an integer n and an integer start.

Define an array nums where nums[i] = start + 2*i (0-indexed) and n == nums.length.

Return the bitwise XOR of all elements of nums.
"""

n = int(input())
x = int(input())
out = x
for i in range(1, n):
    out ^= x+2*i
print(out)
