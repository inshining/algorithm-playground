#https://www.acmicpc.net/problem/1182
import sys

N, S = map(int, sys.stdin.readline().split())
l = list(map(int, sys.stdin.readline().split()))

result = 0
def go(i, tol):
    if i == N:
        if S == tol:
            global result
            result += 1
        return 
    go(i+1, tol)
    go(i+1, tol + l[i])
go(0, 0)
if S == 0:
    result -= 1

print(result)