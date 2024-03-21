import sys
import math

input = sys.stdin.readline

N  = int(input())

stars = [list(map(float, input().split())) for _ in range(N)]

edges =[]
for x in range(N):
    for y in range(x+1, N):
        d = round(math.sqrt((stars[x][0] - stars[y][0]) ** 2 + (stars[x][1] - stars[y][1]) ** 2), 2)
        edges.append((x,y,d))

edges.sort(key=lambda x : x[2])

root = [i for i in range(N)]

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

answer =0
for a,b,c in edges:
    if find(a) != find(b):
        union(a,b)
        answer += c
print(answer)