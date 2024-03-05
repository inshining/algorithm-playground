A, B, C = map(int, input().split())

def go(a,b,c):
    if b == 1:
        return a % c 

    if b % 2 == 0:
        return (go(a, b//2, c) ** 2) % c
    else:
        return (go(a, b//2, c) ** 2 * a) % c

print(go(A,B,C))