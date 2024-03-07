# https://www.acmicpc.net/problem/15649
N, M = map(int, input().split())

issued = [False] * (N + 1)
s = [0] * M
def go(k):
    if k == M:
        print(*s)
        return 
    
    for i in range(1, 1 + N):
        if not issued[i]:
            issued[i] = True
            s[k] = i
            go(k+1)
            issued[i] = False

go(0)

# 풀이 2
"""
N, M = map(int, input().split())

l = [i for i in range(N+1)]

s = [] 
def go(s):
    if len(s) == M:
        print(*s)
        return 
    
    for i in range(1, N+1):
        if i in s:
            continue
        c = s[:]
        go(c + [i])

go(s)

"""