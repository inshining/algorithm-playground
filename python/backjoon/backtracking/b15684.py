import sys

input = sys.stdin.readline

N, M, H = map(int, input().split())
board = [[0] * (N+1) for _ in range(H+2)]

for _ in range(M):
    y,x = map(int, input().split())
    board[y][x] = 1
def sim(i):
    start = i
    x = i
    for y in range(1, H+1):
        if board[y][x] == 1:
            x += 1
        elif board[y][x-1] == 1:
            x -= 1
    if start != x:
        return False
    return True 

answer = 4
def go(idx, r, c):
    global answer
    wrong_num = 0
    for i in range(1, N+1):
        if not sim(i):
            wrong_num += 1
    if wrong_num > ((answer - 1 - idx) * 2):
        return 
    elif wrong_num == 0:
        answer = min(answer, idx)
        return 
    elif idx == 3 or answer <= idx:
        return 
    
    for y in range(r, H+1):
        if y == r:
            now = c
        else:
            now = 1
        for x in range(now, N):
            if board[y][x] == 1:
                continue
            if board[y][x-1] == 1:
                continue
            if board[y][x+1] == 1:
                continue

            if board[y][x-1] == 0 and board[y][x+1] == 0:
                board[y][x] = 1
                go(idx+1, r, c+2)
                board[y][x] = 0


go(0, 1, 1)
if answer == 4:
    answer = -1

print(answer)