#A* Algorithm for 8-Puzzle

import heapq

goal = (1,2,3,4,5,6,7,8,0)
start = (1,2,3,4,0,6,7,5,8)

def h(s):
    d = 0
    for i in range(1,9):
        d += abs(s.index(i)-goal.index(i))
    return d

q = [(h(start),0,start)]
visited = set()

while q:
    f,g,s = heapq.heappop(q)

    if s == goal:
        print("Goal Found")
        print("Moves:",g)
        break

    if s in visited:
        continue

    visited.add(s)

    z = s.index(0)

    for n in [z-3,z+3,z-1,z+1]:
        if 0 <= n < 9:
            t = list(s)
            t[z],t[n] = t[n],t[z]
            t = tuple(t)

            if t not in visited:
                heapq.heappush(q,(g+1+h(t),g+1,t))
