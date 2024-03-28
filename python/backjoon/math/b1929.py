M, N = map(int, input().split())

board = [True] * (N+1)

board[1] = False
for i in range(2, N+1):
    if not board[i]:
        continue
    for j in range(i * i, N+1, i):
        board[j] = False

for i in range(M, N+1):
    if board[i]:
        print(i)