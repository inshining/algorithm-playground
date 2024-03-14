import sys

input = sys.stdin.readline

N = int(input())
board = []
for i in range(1, N+1):
    l = list(map(int, input().split()))
    l = l + [-1] * (N - i)
    board.append(l)

graph = [[0] * (N +1)for _ in range(N+1)]
graph[0] = board[0]
for y in range(0, N):
    for x in range(y+1):
        if y + 1 < N:
            graph[y+1][x] = max(graph[y+1][x], graph[y][x] + board[y+1][x])
            graph[y+1][x+1] = max(graph[y+1][x+1], graph[y][x] + board[y+1][x+1])
        
print(max(graph[-2]))