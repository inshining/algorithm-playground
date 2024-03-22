import sys

input = sys.stdin.readline

T = int(input())
def dfs(i):
    visited[i] = True
    k = data[i]
    if visited[k]:
        return 
    else:
        return dfs(k)

for _ in range(T):
    N = int(input())
    data = [0] + list(map(int, input().split()))
    visited = [True] + [False] * N

    answer = 0

    for i in range(1, N+1):
        if visited[i]:
            continue
        dfs(i)
        answer += 1
    print(answer)
    