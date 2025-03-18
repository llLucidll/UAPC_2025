"""
In recent weeks, the United Association against Property Crime (UAPC) sign has been repeatedly vandalized. Vandals remove some of the letters from UAPC to form an acronym of their choosing. For example, last month, the Unauthorized Art Collective (UAC) removed the letter P.

The UAPC is tired of manually determining which letters have been lost and need replacement. They have tasked you with creating an algorithm to automatically identify the missing letters.

Input
The first line of input contains a string 
 of length at most 
. It is guaranteed that 
 is non-empty and can be obtained by removing some characters from UAPC, while preserving the order of the remaining letters. It is guaranteed that at least one character has been removed.

Output
Output a string consisting of the characters removed from UAPC to obtain 
, listed in the order they appear in UAPC.
"""






s = input()
word = ["U", "A", "P", "C"]



for c in s:
    if c in word:
        word.pop(word.index(c))

res = ""
for i in word:
    res += i

print(res)