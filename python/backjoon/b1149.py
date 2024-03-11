import sys
input = sys.stdin.readline

N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

dp = [l[0]]

for i in range(1, N):
    a = l[i][0] + min(dp[i-1][1], dp[i-1][2])
    b = l[i][1] + min(dp[i-1][0], dp[i-1][2])
    c = l[i][2] + min(dp[i-1][1], dp[i-1][0])
    dp.append([a,b,c])
print(min(dp[N-1]))