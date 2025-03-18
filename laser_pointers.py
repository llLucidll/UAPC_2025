
"""
Can you help me? There are pointers pointing everywhere! I’ve spilled all my laser pointers onto a 2D plane. Even worse, they’re all still turned on! At least this gives us a fun order in which to pick them up! I’d prefer if we grabbed all my pointers in ascending order of where their laser beam contacts the 
-axis. If their laser doesn’t shine across the 
-axis, then it’s not worth grabbing, and do not include it in the list. It belongs on the ground!

Each laser pointer has a name, and I’ll make sure to give you where the laser pointer is, as well as the slope of the line of the direction in which it’s pointing. I’ve never bought the same laser pointer twice, so the names are all unique. Just give me the list of names in the right order, and I’ll pick them up!

Don’t worry, we got lucky, and all laser pointers are pointing towards positive infinity on the 
-axis, and they’re all at least 
 away from the 
-axis. I did a quick scan of all the pointers, and if a laser pointer was ever going to shine on the 
-axis, then it’ll do it by at most 
. Also, the gap between where two different laser pointers hit the 
-axis is always at least 
. Whew! Imagine how annoying it would have been otherwise!

Figure 1: Illustration of the 3rd sample input and output. Lasers B,C,A,E intersect the 
-axis in that order. Laser E does not intersect the 
 axis.
Input
The first line of input contains an integer 
 (
). Then 
 lines follow, each containing three real numbers 
, with 
, 
, and 
 and then the name of the laser pointer. Here, 
 indicates the coordinates of the origin of the laser pointer, and 
 indicates the slope. All real numbers are given with exactly 
 digits of precision after the decimal. Each name is alphanumeric, contains no whitespace, is non-empty, and has at most 
 characters. At least one laser pointer is pointing towards the 
-axis.

Output
Return the list of names of laser pointers that hit the 
-axis, in ascending order of where they hit the 
-axis. Each name should be on a separate line, with no leading or trailing spaces.
"""

n = int(input())
dict = {}
list = []

for i in range(n):
    x, y, m, name = input().split(" ")
    x,y,m = float(x), float(y), float(m)
    if m == 0:
        continue
    if (y<0 and m<0) or (y>0 and m>0):
        continue
    key = -y/m + x
    if key >= 10**8:
        continue
    list.append(key)
    dict[key] = name

list.sort()


for i in list:
    print(dict[i])