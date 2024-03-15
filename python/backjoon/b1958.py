import sys

input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
C = input().rstrip()

x = len(A)
y = len(B)
z = len(C)

dp = [[[0] * (z +1) for _ in range(y+1)] for _ in range(x + 1)]

for i in range(1, x + 1):
    for j in range(1, y+1):
        for k in range(1, z + 1):
            if A[i-1] == B[j-1] and B[j-1] == C[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])
            

ans = -1
for x in range(x+1):
    for y in range(y+1):
        ans = max(ans, max(dp[x][y]))

print(ans)