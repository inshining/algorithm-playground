import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N,M,G,R = map(int,input().split())
board = [list(map(int, input().split())) for _ in range(N)]

av = []
for y in range(N):
    for x in range(M):
        if board[y][x] == 2:
            av.append((y,x))
            board[y][x] = 1

green = set()

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def bfs(green, red):

    cnt = 0
    visited = [board[i][:] for i in range(N)]
    for y, x in green:
        visited[y][x] = 0
    for y, x in red:
        visited[y][x] = 0
    val = 2
    while green and red:
        gl = len(green)
        for _ in range(gl):
            y,x = green.popleft()
            if visited[y][x] < 0:
                continue
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if ny < 0 or N <= ny or nx <0 or M <= nx:
                    continue
                if visited[ny][nx] == 1:

                    visited[ny][nx] = val
                    green.append((ny,nx))
        
        rl = len(red)
        for _ in range(rl):
            y,x = red.popleft()
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if ny < 0 or N <= ny or nx <0 or M <= nx:
                    continue
                if visited[ny][nx] == 1:
                    visited[ny][nx] = -val
                    red.append((ny,nx))
                elif visited[ny][nx] == val:
                    visited[ny][nx] = -val
                    cnt += 1
        val += 1
    return cnt

result = 0
for GRlist in combinations(av, G+R):
    grlist = set(GRlist)
    for Glist in combinations(GRlist, G):
        glist = set(Glist)
        green = deque(glist)
        red = deque(grlist-glist)
        result = max(result, bfs(green, red))

print(result)