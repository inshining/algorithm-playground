from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
graph = [[int(k) for k in list(sys.stdin.readline().strip())] for _ in range(N)]

visited = [[0] * M for _ in range(N)]


def bfs(y,x):
    visited[y][x] = 1 
    d = deque()
    d.append((y,x))
    
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    
    while d:
        y,x = d.popleft()
    
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < N and 0 <= nx < M:
                if graph[ny][nx] and not visited[ny][nx]:
                    visited[ny][nx] = visited[y][x] + 1
                    d.append((ny,nx))
    
bfs(0,0)
print(visited[N-1][M-1])
        
    