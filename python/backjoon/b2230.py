import sys

input = sys.stdin.readline

N, M = map(int, input().split()) 

L = [int(input()) for _ in range(N)]

L.sort()

result = sys.maxsize
if N == 1:
    print(0)
else:
    start = 0
    end = 0
    
    while start <= end:
        if L[end] - L[start] < M:
            if end == N-1:
                break
            end += 1
        else:
            result = min(result, L[end] - L[start])
            start += 1
    print(result)
