#https://www.acmicpc.net/problem/15683

import sys
import copy

input = sys.stdin.readline

N,M = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(N)]

cctv = []

d = {
    1 : [[0], [1], [2],[3]],
    2 : [[1,3], [0,2]],
    3 : [[0,1], [1,2], [2,3], [3,0]],
    4 : [[0,1,3], [0,1,2,], [1,2,3], [2,3,0]],
    5 : [[0,1,2,3]]
}

dy = [-1, 0,1,0]
dx = [0, 1, 0, -1]

for y in range(N):
    for x in range(M):
        if 0 < graph[y][x] < 6:
            cctv.append((y,x,graph[y][x]))

result = N * M 

def move(board,y,x,dd, val):
    y = dy[dd] + y
    x = dx[dd] + x
    
    while 0 <= y < N and 0 <= x < M:
        if board[y][x] <= 0:
            board[y][x] = val
        elif board[y][x] == 6:
            break
        y = dy[dd] + y
        x = dx[dd] + x

def go(idx, board):
    if idx == len(cctv):
        global result
        v = sum([board[i].count(0) for i in range(N)])
        result = min(result, v)
        return
    
    temp = copy.deepcopy(board)
    for dd in d[cctv[idx][2]]:
        for direction in dd:
            move(temp, cctv[idx][0], cctv[idx][1], direction, -1)
        go(idx+1, temp)
        temp = copy.deepcopy(board)

go(0, graph)
print(result)
# TODO: dfs 상황에서 copy와 관련된 궁금증 
""" 
        for direction in dd:
            move(temp, cctv[idx][0], cctv[idx][1], direction, -1)
        go(idx+1, temp)
        for direction in dd:
            move(temp, cctv[idx][0], cctv[idx][1], direction, 0)
"""
# 은 왜 안돼?