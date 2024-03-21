import sys

input = sys.stdin.readline

A = input().strip()
B = input().strip()
C = input().strip()

dp = [[[0] * (105) for _ in range(105)] for _ in range(105)]

for x in range(1, len(A) + 1):
    for y in range(1, len(B)+1):
        for z in range(1, len(C) + 1):
            if A[x-1] == B[y-1] and B[y-1] == C[z-1]:
                dp[x][y][z] = dp[x-1][y-1][z-1] + 1
            else:
                dp[x][y][z] = max(dp[x-1][y][z], dp[x][y-1][z], dp[x][y][z-1])
            
ans = -1
# print(dp[len(A)+1][len(B)+1][len(C)+1])
for x in range(len(A)+1):
    for y in range(len(B)+1):
        ans = max(ans, max(dp[x][y]))

print(ans)