import sys

N = int(sys.stdin.readline())

result = 0

issued1 = [False] * N
issued2 = [False] * (N ** 2 + 1)
issued3 = [False] * (N ** 2 + 1)

def go(idx):
    if idx == N:
        global result
        result += 1
        return 
    for x in range(N):
        if not issued1[x] and not issued2[idx + x] and not issued3[idx-x+N-1]:
            issued1[x] = True
            issued2[idx+x] = True
            issued3[idx-x+N-1] = True
            go(idx+1)
            issued1[x] = False
            issued2[idx+x] = False
            issued3[idx-x+N-1] = False
go(0)
print(result)