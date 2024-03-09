import sys
import copy

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

result = 2

def rotate(arr):
    t = [[0] * len(arr) for _ in range(len(arr[0]))]
    for r in range(len(arr)):
        for c in range(len(arr[0])):
            t[c][len(arr) - r - 1] = arr[r][c]
    return t

def get_v(arr):
    t = []
    for row in arr:
        tt = [0] * len(arr[0])
        point = 0
        for v in row:
            if v > 0:
                if tt[point] == 0:
                    tt[point] = v
                elif tt[point] == v:
                    tt[point] = v * 2
                    point += 1
                else:
                    point += 1
                    tt[point] = v
        t.append(tt)
    return t
                    

def go(idx, arr):
    if idx == 5 or len(arr) == 1:
        global result
        result = max(result, max(sum(arr,[])))
        return
    
    temp = copy.deepcopy(arr)
    for i in range(4):
        for _ in range(i):
            temp = rotate(temp)
        
        temp = get_v(temp)
        if i > 0: 
            for _ in range(4 - i):
                temp = rotate(temp)
        go(idx+1, temp)
        temp = copy.deepcopy(arr)

go(0, board)
print(result)