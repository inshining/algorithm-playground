import sys

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

def go(y):
    start = 0
    end = len(A) - 1

    while start <= end:
        mid = (start + end) // 2

        if A[mid] == y:
            return mid
        
        elif A[mid] > y:
            end = mid -1
        else:
            start = mid + 1
    return -1

for b in B:
    if go(b) >= 0:
        print(1)
    else:
        print(0)
