"""Oh no! You just washed ashore after a shipwreck! Time to put all of those survival skills you have learned in video games to the test.

Some items washed ashore with you, including a map of the area! The map is very crude, the region is represented by a grid and each cell is simply indicated to be “land” or “sea”. After looking at your surroundings a bit, you know which grid cell you are currently standing on. You are able to walk between two land grid cells if they are directly adjacent, i.e. either up, down, left, or right of your current cell (you cannot hop diagonally to a land cell).

The first thing you want to know is how much of the region you are able to explore. That is, your task is to determine how many land cells you are able to walk to.

Input
The first line of input contains two integers 
 (
) and 
 (
). The next 
 lines contain exactly 
 characters each. The 
’th character on the 
’th such line is # if the corresponding grid cell is land, . if the corresponding grid cell is sea, or S if you are currently standing on the grid cell.

There will be exactly one S in the input and that cell is also a land cell. Also, the entire boundary of the region will consist of sea cells. That is, the first and last line will consist entirely of . as will the first and last character of every line describing the region.

Output
Output a single integer indicating the number of land cells you are able to walk to from your starting cell. This count should also include the land cell you are initially standing on.
"""

from collections import deque

m, n = input().split(" ")
m, n = int(m), int(n)

grid = []
res = 0

for i in range(m):
    line = input()
    if "S" in line:
        r = len(grid)
        c = line.index("S")
    
    row = [i for i in line]
    grid.append(row)

q = deque()
q.append([r,c])

while q:
    coord = q.popleft()
    r, c = coord[0], coord[1]
    if r not in range(len(grid)) or c not in range(len(grid[0])):
        continue
    if grid[r][c] == "S" or grid[r][c] == "#":
        res += 1
        grid[r][c] = "."
        q.append([r+1, c])
        q.append([r-1, c])
        q.append([r, c+1])
        q.append([r, c-1])

print(res)
