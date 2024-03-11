import sys
from collections import defaultdict

input = sys.stdin.readline

T = int(input())

D = defaultdict(int)

D[1] = 1
D[2] = 2
D[3] = 4
result = []
for _ in range(T):
    N = int(input())
    for i in range(4, N+1):
        if not D[i]:
            D[i] = D[i-1] + D[i-2] + D[i-3]
    result.append(D[N])

for r in result:
    print(r)