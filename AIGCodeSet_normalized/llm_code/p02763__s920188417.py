import sys
sys.setrecursionlimit(10 ** 9)

def f1(a1, a2):
    a2.add(a1)
    for v1 in G[a1]:
        if v1 in a2:
            continue
        f1(v1, a2)
v1 = int(input())
v2 = input()
v3 = int(input())
v4 = [[] for v5 in range(v1)]
for v5 in range(v3):
    v6 = list(map(int, input().split()))
    if v6[0] == 1:
        v7, v8 = (v6[1] - 1, chr(v6[2]))
        if v2[v7] != v8:
            v2 = v2[:v7] + v8 + v2[v7 + 1:]
    else:
        v9, v10 = (v6[1] - 1, v6[2])
        print(len(set(v2[v9:v10 + 1])))
