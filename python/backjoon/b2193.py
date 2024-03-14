import sys

input = sys.stdin.readline

N = int(input())

dp = [0] * 100

dp[1], dp[2], dp[3] = 1, 1, 2

for i in range(4, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N])