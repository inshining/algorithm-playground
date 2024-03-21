import sys

input = sys.stdin.readline

N = int(input())
eggs = [list(map(int, input().split())) for _ in range(N)]

result = 0 
def go(idx, cnt):
    if idx >= N:
        global result
        result = max(result, cnt)
        return 
    
    if eggs[idx][0] <= 0 or cnt == N-1:
        go(idx+1, cnt)
        return
    temp = cnt
    for i in range(N):
        if i == idx:
            continue
        if eggs[i][0] <= 0:
            continue
        eggs[i][0] -= eggs[idx][1]
        eggs[idx][0] -= eggs[i][1]
        
        if eggs[i][0] <= 0:
            cnt += 1
        if eggs[idx][0] <= 0:
            cnt += 1
        
        go(idx+1, cnt)
        eggs[i][0] += eggs[idx][1]
        eggs[idx][0] += eggs[i][1]
        cnt = temp
go(0, 0)

print(result)