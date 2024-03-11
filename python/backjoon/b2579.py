import sys
from collections import defaultdict

input = sys.stdin.readline

dp = defaultdict
N = int(input())
steps = [int(input()) for _ in range(N)]

dp = [[0,0] for _ in range(N)]
if N > 1:
    dp[0] = [steps[0], 0]
    dp[1] = [steps[1], steps[0] + steps[1]]


    for i in range(2, N):
        dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + steps[i]
        dp[i][1] = dp[i-1][0] + steps[i]

    print(max(dp[N-1][0], dp[N-1][1]))
else:
    print(steps[0])
