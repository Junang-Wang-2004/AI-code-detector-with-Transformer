v1 = input()
v2 = int(input())

def f1(a1):
    v1 = ''
    for v2 in a1:
        v1 += v2 * int(v2)
    return v1
for v3 in range(5 * 10 ** 15):
    v1 = f1(v1)
print(v1[v2 - 1])
v1 = input()
v2 = int(input())
v4 = max(map(int, v1))
v5 = 0
while True:
    v6 = sum((int(c) * v4 ** v5 for v7 in v1))
    if v6 >= v2:
        break
    v5 += 1
for v3 in range(v5):
    v1 = f1(v1)
print(v1[v2 - 1])
