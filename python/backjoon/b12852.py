import sys
from collections import deque, defaultdict

input = sys.stdin.readline
dp = defaultdict(int)
pre = defaultdict(int)

N = int(input())
dp[1] = 0
pre[1] = 0

for i in range(2, N+1):
    dp[i] = dp[i-1] + 1
    pre[i]  = i-1    
    
    if i % 2 == 0 and dp[i//2] + 1 < dp[i]:
        dp[i] = dp[i//2] + 1
        pre[i] = i//2
    if i % 3 == 0 and dp[i//3] + 1 < dp[i]:
        dp[i] = dp[i//3] + 1
        pre[i] = i//3

print(dp[N])
while True:
    print(N,end=" ")
    if N == 1:
        print()
        break
    N = pre[N]

    