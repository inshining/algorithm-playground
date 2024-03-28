N = int(input())
l = list(map(int, input().split()))

result = 0
for k in l:
    i = 2
    if k == 1:
        continue
    while i * i <= k:
        if k % i == 0:
            break
        i += 1
    if i * i > k:
        result += 1
print(result)