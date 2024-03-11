import sys

input = sys.stdin.readline

N, M = map(int, input().split())

L = list(map(int, input().split()))

S = [0]
for v in L:
    S.append(S[-1] + v)
R = []
for _ in range(M):
    i, j = map(int, input().split())
    R.append(S[j]- S[i-1])

for r in R:
    print(r)
