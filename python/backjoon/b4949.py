import sys
import re
from collections import deque
# input = sys.stdin.readline

bracket = {
    ")" : "(",
    "]" : "["
}

answers = []
while True:
    str = input()
    result = True
    if str == ".":
        break
    l = re.findall(r'[()\[\]]', str)
    d = deque() 
    for ll in l:
        if ll in ["(", "["]:
            d.append(ll)
        else:
            if d:
                k = d.pop()
                if k != bracket[ll]:
                    result = False
            else:
                result = False
                break
        
    if d:
        result = False 
    answers.append(result)

for aa in answers:
    if aa:
        print("yes")
    else:
        print("no")
