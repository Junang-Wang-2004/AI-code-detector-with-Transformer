from collections import deque
v1 = input()
v2 = len(v1)
v3 = deque()
v4 = 0
for v5 in v1:
    if v5 == 'C':
        v3.append('C')
    elif v5 == 'B':
        if v3:
            v3.append('B')
    elif v5 == 'A':
        if v3 and v3[-1] == 'B':
            v3.pop()
            if v3 and v3[-1] == 'B':
                v3.pop()
                v4 += 1
print(v4)
