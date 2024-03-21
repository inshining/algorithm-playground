import sys

input = sys.stdin.readline

N = int(input())

def go(size):
    if size == 1:
        return ["*"]
    
    S = go(size//3)
    
    arr = []

    for star in S:
        arr.append(star * 3)
    
    for star in S:
        arr.append(star + " " * (size//3) + star)
    
    for star in S:
        arr.append(star * 3)
    return arr
l = go(N)
print("\n".join(l))