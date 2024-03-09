# https://www.acmicpc.net/problem/2751
import sys
input = sys.stdin.readline

N = int(input())

l = []
for _ in range(N):
    l.append(int(input()))

l.sort()
for i in l:
    print(i)