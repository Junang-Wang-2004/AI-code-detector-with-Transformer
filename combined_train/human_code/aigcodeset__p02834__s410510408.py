from collections import deque
v1 = ''
'\n9 6 1\n1 2\n2 3\n3 4\n4 5\n5 6\n4 7\n7 8\n8 9\nans 5\n'
'\n5 4 1\n1 2\n2 3\n3 4\n3 5\nans 2\n'
'\n5 4 5\n1 2\n1 3\n1 4\n1 5\nans 1\n'
v1 = list(reversed(v1.strip().splitlines()))
if v1:

    def f1():
        return v1.pop()
else:

    def f1():
        return input()
v2, v3, v4 = map(int, f1().split())
v5 = [0] * (v2 - 1)
for v6 in range(v2 - 1):
    v5[v6] = tuple(map(int, f1().split()))
v7 = [[] for v6 in range(v2 + 1)]
for v8 in v5:
    v7[v8[0]].append(v8[1])
    v7[v8[1]].append(v8[0])
v9 = [None] * (v2 + 1)
v10 = [None] * (v2 + 1)
v9[v3] = 0
v10[v4] = 0
v11 = deque([v3])
v12 = deque([v4])
for v13, v14 in ((v9, v11), (v10, v12)):
    while v14:
        v15 = v14.popleft()
        for v16 in v7[v15]:
            if v13[v16] == None:
                v14.append(v16)
                v13[v16] = v13[v15] + 1
print(max((v10[v6] for v6 in range(1, v2 + 1) if v9[v6] < v10[v6])) - 1)
