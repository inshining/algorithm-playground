import sys
from collections import deque

input = sys.stdin.readline 

board = [["."] * 6 for _ in range(12)]

N, M = 12, 6
for y in range(12):
    line = list(input().strip())
    for x in range(6):
        board[y][x] = line[x]


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def scan():
    visited = [[False] * 6 for _ in range(12) ]

    result = []
    for y in range(12):
        for x in range(6):
            if visited[y][x]:
                continue
            if board[y][x] == ".":
                visited[y][x] = True
                
            else:
                dq = deque()
                color = board[y][x]
                dq.append((y,x))
                visited[y][x] = True 
                
                temp = [(y,x)]
                while dq:
                    y,x = dq.popleft()

                    for i in range(4):
                        ny = y + dy[i]
                        nx = x + dx[i]

                        if 0 <= ny < N and 0 <= nx < M and visited[ny][nx] == False and board[ny][nx]== color:
                            visited[ny][nx] = True
                            temp.append((ny,nx))
                            dq.append((ny,nx))
                if len(temp) >= 4:
                    result.extend(temp)
    return result

def delete_pu(l):
    for y,x in l:
        board[y][x] = "."
def change():
    for x in range(M):
        line = ["."] * N 
        idx = N-1
        for y in range(N-1, -1, -1):
            if board[y][x] != ".":
                line[idx] = board[y][x]
                idx -= 1
        for y in range(N-1, -1, -1):
            board[y][x] = line[y]

step = 0
while True:
    deleted_list = scan()
    if not deleted_list:
        break
    delete_pu(deleted_list)
    change()
    step += 1
print(step)
