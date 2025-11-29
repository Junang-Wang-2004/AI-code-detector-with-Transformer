import sys
input = sys.stdin.readline
v1 = input().strip()
v2 = input().strip()
v3 = defaultdict(list)

def f1(a1):
    for v1, v2 in a1.items():
        if v1 != v2:
            return False
    else:
        return True
for v4, v5 in zip(v1, v2):
    if v4 not in v3:
        v3[v4] = v5
    elif v3[v4] != v5:
        print('No')
        exit()
if len(v3) != len(set(v3.values())):
    print('No')
else:
    print('Yes')
