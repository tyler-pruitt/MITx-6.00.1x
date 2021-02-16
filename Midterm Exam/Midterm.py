#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 15:52:49 2020

@author: tylerpruitt
"""

"""
Midterm
"""
"""
Problem 3
"""
def count7(N):
    """
    N: a non-negative integer
    """
    count = 0
    if N % 10 != 7 and len(str(N)) == 1:
        return count
    if N % 10 == 7:
        count += 1
    return count7(N // 10) + count
"""
Problem 4
"""
def getSublists(L, n):
    sublists = []
    for i in range(len(L)):
        if len(L[i:i+n]) == n:
            sublists.append(L[i:i+n])
    return sublists
"""
Problem 5
"""
def uniqueValues(aDict):
    """
    aDict: a dictionary
    """
    list_values = list(aDict.values())
    unique_values = []
    recurring_values = []
    for value in list_values:
        if value in unique_values:
            unique_values.remove(value)
            recurring_values.append(value)
        elif value not in unique_values and value not in recurring_values:
            unique_values.append(value)
    unique_keys = []
    for key, item in aDict.items():
        if item in unique_values:
            unique_keys.append(key)
    return unique_keys
"""
Problem 6
"""
def max_val(t): 
    """
    t, tuple or list
    Each element of t is either an int, a tuple, or a list
    No tuple or list is empty
    Returns the maximum int in t or (recursively) in an element of t 
    """
    int_list = []
    for element in t:
        if type(element) == int:
            int_list.append(element)
        else: #type(element) == list or tuple
            for item in element:
               if type(item) == int:
                   int_list.append(item)
               else:
                   for thing in item:
                       if type(thing) == int:
                           int_list.append(thing)
                       else:
                           for piece in thing:
                               if type(piece) == int:
                                   int_list.append(piece)
                               else:
                                   for article in piece:
                                       if type(article) == int:
                                           int_list.append(article)
                                       else:
                                           for component in article:
                                               if type(component) == int:
                                                   int_list.append(component)
                                               else: 
                                                   int_list.append(max(component))   
    return max(int_list)
"""
Problem 7
"""
def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements. Remaining elements in L
            should be in the same order.
    Returns the length of L after mutation
    """
    index = []
    for i in range(len(L)):
        if f(L[i]) == False:
            index.append(L[i])
    for j in index:
        L.remove(j)
    return len(L)

run_satisfiesF(L, satisfiesF)