import sys

input = sys.stdin.readline

V, E = map(int, input().split())

egdes = [list(map(int, input().split())) for _ in range(E)]

root = [i for i in range(V+1)]

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
        return

egdes.sort(key=lambda x : x[2])
answer = 0
for f,t,c in egdes:
    if find(f) != find(t):
        union(f,t)
        answer += c
print(answer)