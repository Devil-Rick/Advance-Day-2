"""
Given a valid (IPv4) IP address, return a defanged version of that IP address.

A defanged IP address replaces every period "." with "[.]".
"""

a = list(input('Give Ip address : ').split('.'))
print('[.]'.join(a))
