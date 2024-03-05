n = int(sys.stdin.readline().strip())
ps = [sys.stdin.readline().strip() for x in range(n)]

class Node():
    def __init__(self, value, pre=None, next=None):
        self.value = value
        self.pre = pre
        self.next = next 

class Deque():
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.nums = 0
    
    def push_front(self, x):
        n = Node(x)
        if not self.head and not self.tail:
            self.head = n
            self.tail = n
        
        else:
            self.head.pre = n
            n.next = self.head
            self.head = n
        
        self.nums += 1
    
    def push_back(self, x):
        n = Node(x)
        if not self.head and not self.tail:
            self.head = n
            self.tail = n
        
        else:
            self.tail.next = n
            n.pre = self.tail
            self.tail = n
            
        self.nums += 1
    
    def pop_front(self):
        if self.head:
            node = self.head
            if self.nums > 1:
                self.head = self.head.next
            else:
                self.head = None
                self.tail = None
            self.nums -= 1
            return node.value
        
        else:
            return -1 
    
    def pop_back(self):
        if self.tail:
            node = self.tail
            if self.nums > 1:
                self.tail = self.tail.pre
            else:
                self.head = None
                self.tail = None
            self.nums -= 1
            return node.value
        
        return -1
    
    def size(self):
        return self.nums

    def empty(self):
        if self.nums:
            return 0 
        return 1
    
    def front(self):
        if self.head:
            return self.head.value
        return -1
    
    def back(self):
        if self.tail:
            return self.tail.value
        return -1

N = int(input())

d = Deque()
result = []
for _ in range(N):
    command, *arg = input().split()
    if command == "push_front":
        d.push_front(int(arg[0]))
    elif command == "push_back":
        d.push_back(int(arg[0])) 
    elif command == "pop_front":
        result.append(d.pop_front())
    elif command == "pop_back":
        result.append(d.pop_back())
    elif command == "size":
        result.append(d.size())
    elif command == "empty":
        result.append(d.empty())
    elif command == "front":
        result.append(d.front())
    elif command == "back":
        result.append(d.back())

for rr in result:
    print(rr)