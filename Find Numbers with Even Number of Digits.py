"""
Given an array nums of integers, return how many of them contain an even number of digits.
"""
a = list(input().split(','))
c = 0
for i in a:
    if len(i) % 2 == 0:
        c += 1
print(c)
