# https://www.acmicpc.net/problem/18808
import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
stickers = []
for _ in range(K):
    r, c = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(r)]
    stickers.append(a)

board = [[0] * M for _ in range(N)]

def on_fit(r,c, arr):
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            if board[y+r][x+c] + arr[y][x] > 1:
                return False
    return True

def find_position(arr):
    for y in range(N-len(arr) + 1):
        for x in range(M - len(arr[0]) + 1):
            # 이미 boar에 1이 있는 경우, 
            if on_fit(y,x, arr):
                return y,x

    return -1, -1

def stick(y,x,arr):
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            board[r+y][c+x] += arr[r][c] 

def rotate(arr):
    temp = [[0] * len(arr) for _ in range(len(arr[0]))]
    
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            temp[c][len(arr) - 1- r] = arr[r][c]
    return temp

for arr in stickers:
    for _ in range(4):
        y, x= find_position(arr)
        if y >= 0 and x >= 0:
            stick(y,x, arr)
            break
        arr = rotate(arr)
        
print(list(sum(board,[])).count(1))