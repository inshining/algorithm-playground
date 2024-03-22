import sys
sys.setrecursionlimit(10**6)
T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    team = [0] + list(map(int, sys.stdin.readline().split()))
    visited = [True] + [False] * N 
    answer = N

    def go(k):
        
        cycle.append(k)
        visited[k] = True
        other = team[k]

        if visited[other]:
            if other in cycle:
                global answer 
                answer -= len(cycle[cycle.index(other):])
        else:
            go(other)
    
    for i in range(1, N+1):
        if not visited[i]:
            cycle = []
            go(i)
    
    print(answer)
