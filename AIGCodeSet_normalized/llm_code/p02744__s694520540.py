from string import ascii_lowercase
v1 = int(input())
v2 = {s: i for v3, v4 in enumerate(ascii_lowercase)}
v5 = [v4 for v4, v3 in v2.items()]
v6 = []

def f1(a1, a2):
    if v1 == a1:
        v6.append(a2)
    elif v1 > a1:
        for v1 in range(max([v2[c] for v2 in a2]) + 2):
            v3 = a2 + v5[v1]
            f1(a1 + 1, v3)
f1(1, 'a')
v6.sort()
for v7 in v6:
    print(v7)
