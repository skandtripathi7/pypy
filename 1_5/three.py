"""Given a string:

s = "engineer"


Write a function that returns a dictionary with character frequency.

Expected Output"""

def freq_(s):
    
    freq = dict()

    for ch in s:
        if ch not in freq:
            freq[chr] = 1
        else:
            freq[chr]+= 1
    
    return freq