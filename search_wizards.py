"""
You adore word searches, and have been doing them since you were little. You do them so much, you started just picking out words whenever you see a string of text! With a target string 
 in mind, can you figure out how many times 
 occurs in the string 
?

Note that instances of 
 may overlap partially, but every occurance has a unique starting index in 
.

Input
The first line consists of a string 
 (
). The second line contains a single integer 
 (
). The third and final line contains the string 
 consisting of 
 words. Consecutive words are separated by a single space. The total length of all words in 
 is at most 
. The only characters that will appear in 
 and all words in 
 are lowercase alphabetical characters a - z.

Output
Return an integer of the number of times 
 occurs in 
, allowing for overlap.
"""

def counti(word,target):
    res = 0
    for i in range(len(word)-len(target)+1):
        # print((word[i:i+len(target)]) )
        if (word[i:i+len(target)]) == target:
            res+=1
    return res


word = input()
number = int(input())
list = input().split(" ")

count = 0

for i in list:
    count+=counti(i,word)

print(count)
