import sys 

from collections import deque

input = sys.stdin.readline

result = 0
arr = [input().strip() for _ in range(5)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def bfs(arr1):
    v = [[True] * 5 for _ in range(5)]
    
    for r, c in arr1:
        v[r][c] = False
    
    n = 0
    
    r,c = arr1[0]
    
    t = deque()
    
    v[r][c] = True
    n += 1
    t.append((r,c))
    
    while t:
        y, x = t.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if ny < 0 or 5 <= ny or nx < 0 or 5 <= nx:
                continue
            if not v[ny][nx]:
                n += 1
                v[ny][nx] = True
                t.append((ny,nx))
    
    return n == 7

def go(start, num):
    if num >= 4:
        return 

    if len(temp) == 7:
        global result
        if bfs(temp):
            result += 1
        return
    
    
    for i in range(start, 25):
        r = i // 5
        c = i % 5
        
        temp.append((r,c))
        
        if arr[r][c] == "Y":
            go(i+1, num+1)
        else:
            go(i+1, num)
        temp.pop(-1)

temp = []

go(0,0)
print(result)