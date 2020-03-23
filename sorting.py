#!/bin/python3
'''
Python provides built-in sort/sorted functions that use timsort internally.
You cannot use these built-in functions anywhere in this file.

Every function in this file takes a comparator `cmp` as input which controls how the elements of the list should be compared against each other.
If cmp(a,b) returns -1, then a<b;
if cmp(a,b) returns  1, then a>b;
if cmp(a,b) returns  0, then a==b.
'''

import random

def cmp_standard(a,b):
    '''
    used for sorting from lowest to highest
    '''
    if a<b:
        return -1
    if b<a:
        return 1
    return 0


def cmp_reverse(a,b):
    '''
    used for sorting from highest to lowest
    '''
    if a<b:
        return 1
    if b<a:
        return -1
    return 0


def cmp_last_digit(a,b):
    '''
    used for sorting based on the last digit only
    '''
    return cmp_standard(a%10,b%10)


def _merged(left, right, cmp=cmp_standard):
    '''
    Assumes that both xs and ys are sorted,
    and returns a new list containing the elements of both xs and ys.
    Runs in linear time.
    '''
    if len(left) == 0:
        return right
    if len(right)== 0:
        return left
    
    lo=0
    hi=0
    x=0

    xs = left + right
    while lo < len(left) and hi < len(right):
        if cmp(left[lo],right[hi] == -1:
               xs[x] = left[lo]
               lo += 1
        else:
               xs[x] = right[hi]
               r+=1
        x += 1
    while lo < len(left):
        xs[x] = left[lo]
        lo += 1
        x += 1
    while hi < len(right):
        xs[x] = right[hi]
        hi += 1
        x+= 1
  
               
    return xs

def merge_sorted(xs, cmp=cmp_standard):
    '''
    Merge sort is the standard O(n log n) sorting algorithm.
    Recall that the merge sort pseudo code is:

        if xs has 1 element
            it is sorted, so return xs
        else
            divide the list into two halves left,right
            sort the left
            sort the right
            merge the two sorted halves

    You should return a sorted version of the input list xs
    '''
    if len(xs) <= 1:
        return xs
    else:
        mid = len(xs)//2
        left = xs[:mid]
        right = xs[mid:]
        return _merged(merge_sorted(left,cmp),merge_sorted(right,cmp),cmp)

def quick_sorted(xs, cmp=cmp_standard):
    '''
    Quicksort is like mergesort,
    but it uses a different strategy to split the list.
    Instead of splitting the list down the middle,
    a "pivot" value is randomly selected, 
    and the list is split into a "less than" sublist and a "greater than" sublist.

    The pseudocode is:

        if xs has 1 element
            it is sorted, so return xs
        else
            select a pivot value p
            put all the values less than p in a list
            put all the values greater than p in a list
            sort both lists recursively
            return the concatenation of (less than, p, and greater than)

    You should return a sorted version of the input list xs
    '''
    if len(xs) <= 1:
        return xs
    else:
        rand = random.randrange(len(xs))
        lower = xs[:rand]
        higher= xs[rand:]
        return _merged(merge_sorted(lower,cmp),merge_sorted(higher,cmp),cmp)

