import sys

input = sys.stdin.readline

N, M = map(int, input().split())

root = [i for i in range(N+1)]
routes = [list(map(int, input().split())) for _ in range(M)]  

def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def union(x,y):
    x = find(x)
    y = find(y)
    if x != y:
        root[y] = x
    
routes.sort(key=lambda x : x[2])
answer = 0
last_e = 0
for a,b,c in routes:
    if find(a) != find(b):
        answer += c
        last_e = c
        union(a,b)
        
print(answer- last_e)