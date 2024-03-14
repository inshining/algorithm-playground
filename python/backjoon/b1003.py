import sys
from collections import defaultdict

input = sys.stdin.readline

D = defaultdict(list)

T = int(input())

D[0] = [1,0]
D[1] = [0,1]

def go(n):
    for i in range(2, n+1):
        if not D[i]:
            a = D[i-1][0] + D[i-2][0]
            b = D[i-1][1] + D[i-2][1]
            D[i] = [a,b]
    
    return D[n]

result = []
for _ in range(T):
    n = int(input())
    result.append(go(n))

for r in result:
    print(*r)