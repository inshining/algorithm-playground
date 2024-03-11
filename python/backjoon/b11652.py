from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
l = []
for _ in range(N):
    a = input().strip()
    l.append(a)

c = Counter(l)
print(c.most_common(1)[0][0])
