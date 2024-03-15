import sys

input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()
C = input().rstrip()

dp = [[[0] * (len(C) +1) for _ in range(len(B)+1)] for _ in range(len(A) + 1)]

for x in range(1, len(A) + 1):
    for y in range(1, len(B)+1):
        for z in range(1, len(C) + 1):
            if A[x-1] == B[y-1] == C[z-1]:
                dp[x][y][z] = dp[x-1][y-1][z-1] + 1
            else:
                dp[x][y][z] = max(dp[x-1][z][z], dp[x][y-1][z], dp[x][y][z-1])
            

ans = -1
for x in range(len(A)+1):
    for y in range(len(B)+1):
        ans = max(ans, max(dp[x][y]))

print(ans)