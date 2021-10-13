"""
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.
"""
a = list(input().split(','))
c = 0
for i in range(len(a)):
    c += a[:i].count(a[i])
print(c)
