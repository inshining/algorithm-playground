import sys
input = sys.stdin.readline
N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

result = 0

coins.reverse()

for c in coins:
    v, K = divmod(K, c)
    result += v
    if K == 0:
        break
print(result)