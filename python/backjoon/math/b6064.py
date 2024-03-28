import sys
input = sys.stdin.readline
T = int(input())


def solve(n,m, x,y):
    k = x
    while k <= m * n:
        if (k-x) % n == 0 and (k-y) % m == 0:
            return k
        k += n
    return -1
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(solve(M,N,x,y))   