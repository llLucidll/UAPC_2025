"""
LEDs are an amazing technology, in part due to their longevity. But they can’t last forever right? So you decide to put it to the test; you turn on an LED, and a machine periodically records the time in milliseconds since you started. Eventually it turns off! Your machine kept recording though, and unforunately your data is all jumbled up! What is the first time the machine recorded the LED being off?

Note that the LED may turn back on; you want to find the very first time the LED was recorded being off.

Input
The first line of input contains the integer 
 (
). The following 
 lines consist of 2 integers 
 (
) and 
 (
), where 
 is the time this recording was taken in milliseconds, and 
 denotes whether the LED was on or off. The number 
 corresponds to the LED being on, and 
 off.

Output
Output a single integer denoting the time of the first recording where the LED was off, or output 
 if it was never off for any recording.
 """

from collections import defaultdict

N = int(input())
store = {0:[], 1:[]}

for i in range(N):
    time, stat = input().split(" ")
    time, stat = int(time), int(stat)
    store[stat].append(time)

if store[0] == []:
    print(-1)
else:
    arr = store[0]
    arr.sort()
    
    print(arr[0])