import sys
from collections import defaultdict

input = sys.stdin.readline

N = int(input())

D = defaultdict(int)
D[1] = 0
for i in range(2, N+1):
    num = D[i-1] + 1
    if i % 3 == 0:
        num = min(num, D[i//3] + 1)
    if i % 2 == 0:
        num = min(num, D[i//2] + 1)
    D[i] = num
print(D[N])
    

# def go(n, idx):
#     if n <= 1:
#         return idx
#     num = go(n-1, idx+1)
#     if n % 3 == 0 or n % 2 == 0:
#         if n % 3 == 0:
#             num = go(n//3, idx+1)
#         if n % 2 == 0:
#             num = min(go(n//2, idx+1), num)
#     else:
        
#     return num

    