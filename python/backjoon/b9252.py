import sys

input = sys.stdin.readline

A = input().rstrip()
B = input().rstrip()

dp = [[0] *(1005) for _ in range(1005)]

for i in range(1, len(A) + 1):
    for j in range(1, len(B) + 1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            

result = "" 
last_v = dp[len(A)][len(B)]
for i in range(len(A), 0, -1):
    for j in range(len(B), 0, -1):
        if dp[i][j] == last_v:
            if A[i-1]==B[j-1]:
                result += A[i-1]
                last_v -= 1
                break

print(dp[len(A)][len(B)])
print(result[::-1])