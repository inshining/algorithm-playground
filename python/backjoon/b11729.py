q = []
def hanoi(nums, from_, to_, via_):
    if nums == 1:
        q.append((from_, to_))
        return
    
    hanoi(nums-1, from_, via_, to_)
    q.append((from_, to_))
    hanoi(nums-1, via_, to_, from_)

N = int(input())

hanoi(N, 1, 3, 2)

print(len(q))
for y,x in q:
    print(y,x)