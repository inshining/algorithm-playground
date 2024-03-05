from collections import deque
import sys

input = sys.stdin.readline

N, M = map(int, input().split())
answer = list(map(int, input().split()))

d  = deque([x for x in range(1, N+1)])

result = 0
for a in answer:
    left = 0
    while d[0] != a:
        d.rotate(-1)
        left += 1
    
    d.rotate(left)
    right = 0
    while d[0] != a:
        d.rotate(1)
        right += 1
    
    d.rotate(-right)
    
    if left <= right:
        d.rotate(-left)
        result += left
    else:
        d.rotate(right)
        result += right

    d.popleft()
print(result)
    