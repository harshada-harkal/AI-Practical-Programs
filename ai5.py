
from collections import deque

grid = [
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,1,0],
    [1,1,0,0,0],
    [0,0,0,1,0]
]

start = (0,0)
goal = (4,4)

def bfs():
    q = deque([(start, [start])])
    visited = [start]

    while q:
        pos, path = q.popleft()

        if pos == goal:
            return path

        r, c = pos

        for dr, dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr, nc = r+dr, c+dc

            if (0 <= nr < 5 and 0 <= nc < 5
                and grid[nr][nc] == 0
                and (nr,nc) not in visited):

                visited.append((nr,nc))
                q.append(((nr,nc), path+[(nr,nc)]))

    return None

path = bfs()
print("Shortest Path:", path)
print("Number of moves:", len(path)-1 if path else 0)
