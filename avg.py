# Author: Isabelle Bretl
# Filename: avg.py
# Date: 04.30.2021
# Description: calculates the average of elements from a list of ints

def calcAvg(lst):
    sum = 0.0
    for i in lst:
        sum = sum + i
    avg = sum/len(lst)
    return avg