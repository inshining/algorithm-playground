import sys

input = sys.stdin.readline 

K, N = map(int, input().split())
lans = [int(input()) for _ in range(K)]
lans.sort()
start = 1
end = lans[-1] - lans[0]

answer = 1
while start <= end:
    mid = (start + end) // 2
    
    count = 1
    current = lans[0]

    for i in range(1, K):
        if lans[i] - current >= mid:
            current = lans[i]
            count += 1
    
    if count >= N:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)