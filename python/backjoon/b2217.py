import sys

input = sys.stdin.readline

N = int(input())

ropes = [int(input()) for _ in range(N)]

ropes.sort(reverse=True)

result = -sys.maxsize
for i in range(N):
    result = max(result, (i+1) * ropes[i])

print(result)