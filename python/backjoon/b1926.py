import sys 
from collections import deque
input = sys.stdin.readline


N, M = map(int, input().split())

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

dy = [-1, 0, 1, 0]
dx = [0, 1, 0 ,-1]
def bfs(y,x):
    board[y][x] = True
    d = deque()
    d.append((y,x))
    size = 1
    while d:
        y,x = d.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or N <= ny or nx < 0 or M <= nx:
                continue
            
            if not board[ny][nx] and graph[ny][nx]:
                board[ny][nx] = True
                size += 1
                d.append((ny,nx))

    return size

board = [[False] * M for _ in range(N)]

result = 0 
nums = 0
for y in range(N):
    for x in range(M):
        if graph[y][x] and not board[y][x]:
            nums += 1
            result = max(result, bfs(y,x))
print(nums)
print(result)