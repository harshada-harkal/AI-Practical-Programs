from collections import deque

grid = [
 ['S',0,0,'X'],
 [0,'X',0,0],
 [0,0,0,'X'],
 ['X',0,0,'G']
]

start = (0,0)
goal = (3,3)

q = deque([start])
visited = {start}

while q:
    r,c = q.popleft()

    if (r,c) == goal:
        print("Goal Reached!")
        break

    for dr,dc in [(0,1),(1,0),(0,-1),(-1,0)]:
        nr,nc = r+dr,c+dc

        if 0<=nr<4 and 0<=nc<4:
            if grid[nr][nc] != 'X' and (nr,nc) not in visited:
                visited.add((nr,nc))
                q.append((nr,nc))
else:
    print("Goal Not Found")

print("Visited:", visited)
