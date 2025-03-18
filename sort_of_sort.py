"""Sorting takes so long... but if we don’t mind losing some data we can sort of sort much faster!

A sort of sorted list is a monotonically increasing list containing all elements of another list 
 that were originally in sorted order. That is, a sort of sorted list obtained from list 
 contains all 
 such that 
 for all 
.

Input
The first line of input contains a single integer 
, the length of the unsorted list (
). The next line contains 
 space separated integers 
 (
).

Output
Output a single line of space separated integers representing the sort of sorted list obtained from the given list 
.
"""

num = int(input())
list = input().split(" ")

res = []
last = int(list[0])

for i in range(len(list)):
    elem = int(list[i])
    if elem >= last:
        res.append(str(elem))
        last = elem
        

print(' '.join(res))

