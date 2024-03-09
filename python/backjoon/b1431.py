import sys

input = sys.stdin.readline

N = int(input())
l = [input().strip() for _ in range(N)]

def com(a):
    v = 0
    for aa in a:
        if aa.isdigit():
            v += int(aa)
    return v

l.sort(key= lambda x : (len(x), com(x), x))
print('\n'.join(l))