import collections
v1 = int(input())
v2 = [0] * v1
for v3 in range(v1):
    v2[v3] = int(input())
v2.sort(reverse=True)
v4 = collections.Counter(v2)

def f1():
    if v2[0] % 2:
        return True
    else:
        return v4[v2[0]] % 2 == 1 or v4[v2[0] - 1] > 0
print('first' if f1() else 'second')
