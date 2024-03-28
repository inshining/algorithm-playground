T = int(input())

def go(a, b, aa,bb):
    i = aa
    while True:
        if i % b == bb: 
            return i
        i += a 
        if (i-aa) % a == 0 and (i-aa) % b == 0:
            return -1
result = []
for _ in range(T):
    M, N, x, y = map(int, input().split())
    
    if M >= N:
        result.append(go(M,N,x,y))
    else:
        result.append(go(N,M, y,x))

for k in result:
    print(k)