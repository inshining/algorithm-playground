import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
for y in range(N):
    for x in range(M):
        board[y][x] = int(board[y][x])

graph = [[[False, False] for _ in range(M)] for _ in range(N)]
graph[0][0][0] = True
graph[0][0][1] = True
dq = deque()
dq.append((0,0,0,1))
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

answer = -1
while dq:
    y,x,wall, v = dq.popleft()
    if y == N-1 and x == M-1:
        answer = v
        break

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or N <= ny or nx < 0 or M <= nx:
            continue
        if graph[ny][nx][wall] == False:
            if board[ny][nx] == 0:
                graph[ny][nx][wall] = True
                dq.append((ny,nx,wall,v+1))
            else:
                if wall == 0:
                    graph[ny][nx][wall] = True
                    dq.append((ny,nx,1,v+1))

print(answer)