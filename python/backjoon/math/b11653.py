N = int(input())


result = []
if N > 1:
    i = 2
    while i  <= N:
        while N % i == 0:
            result.append(i)
            N = N // i 
        i += 1
    for k in result:
        print(k)
    