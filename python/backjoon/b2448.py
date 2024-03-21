import sys

input = sys.stdin.readline

def go(size):
    if size == 3:
        return ["*", "* *", "*****"]
    
    l = go(size//2)
    arr = []
    for s in l:
        arr.append(s)
    
    for i in range(len(l)):
        arr.append(l[i] + " " * len(l[len(l)-1-i]) + l[i])
    return arr

N = int(input())
g = go(N)
for gg in g:
    ss = N* 2 -1
    print(gg.center(ss))