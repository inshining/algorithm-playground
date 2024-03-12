import sys

input = sys.stdin.readline

N = int(input())

t = [list(map(int, input().split())) for _ in range(N)]

t.sort(key=lambda x : (x[1], x[0], x[1]-x[0]))

k =0
result = 0 

for i in t:
    if k > i[0]:
        continue
    result += 1
    k = i[1]
print(result)