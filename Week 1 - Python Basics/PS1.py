#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 12:17:47 2020

@author: tylerpruitt
"""

"""
Problem Set 1
"""
"""
Problem 1
"""

s = 'azcbobobegghakl'

numVowels = 0
for char in s:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        numVowels += 1
    else:
        None
print("Number of vowels: ", numVowels)

"""
Problem 2
"""

numbob = 0
for i in range(len(s)):
    if s[i:i+3] == 'bob':
        numbob += 1
print("Number of times bob occurs is: ", numbob)

"""
Problem 3
"""

listA = ''
listB = ''
for k in range(len(s) - 1):
    if s[k] <= s[k+1]:
        if len(listA) == 0:
            listA += s[k]
        listA += s[k+1]
        if len(listA) > len(listB):
            listB = listA
    else:
        listA = ''
if len(listB) == 0:
    listB = max(s)
print('Longest substring in alphabetical order is:', listB)
